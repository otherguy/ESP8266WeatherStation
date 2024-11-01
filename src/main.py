# -*- coding: utf-8 -*-
#
# main.py
#
from machine import Pin, Signal, SPI, reset, ADC
from utime import sleep, ticks_ms, localtime
from max7219 import Matrix8x8
from network import WLAN, STA_IF
from ntptime import settime
import secrets
import symbols
import urequests as requests
import gc

# #############################################################################
# ### Configuration
# #############################################################################
#
# This is fairly static and does not need to be changed when deploying.
#

# How often to check for weather updates (milliseconds)
QUERY_DELAY   = 1800000 # 30 minutes

# How often to blink the LED (milliseconds)
BLINK_DELAY   =   30000 # 30 seconds

# How many failed attempts to fetch weather before displaying an error
FAILURE_THRESHOLD = 5

# Definitions
NUM_MATRICES  = 3  # How many 8x8 matrices are connected
CS_PIN        = 15 # GPIO 15 = D8 = CS
LED_0_PIN     = 2  # GPIO  2 = internal LED of the ESP8266
LED_1_PIN     = 5  # GPIO  5 = D1
LED_2_PIN     = 4  # GPIO  4 = D2
INSERTION_PIN = 0  # GPIO  0 = D3
SPI_BAUDRATE  = 10000000 # 10Mhz baudrate (default is 80Mhz)

# #############################################################################
# #############################################################################
# #############################################################################

# Fn: remap()
def remap(value, out_min=0.0, out_max=1.0, in_min=0.0, in_max=1024.0):
    """
    Maps a value from a given range (default 0-1024) to a new
    range (default 0.0 - 1.0). Works with int and float values.

    :param value:    The value to remap
    :param out_min:  The lower end of the output range
    :param out_max:  The upper end of the output range
    :param in_min:   The lower end of the input range
    :param in_max:   The upper end of the output range

    :return: The remapped value
    """
    return float(min(out_max, max(out_min, (float(value) - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)))

# Fn: set_matrix_brightness()
def set_matrix_brightness(pot, display, old_brightness_value, min_brightness=0, max_brightness=15):
    """
    Fetches the daily weather forecast for a given
    location from OpenWeatherMap.

    :param pot:                  The trim potentiometer object to read the analog value from
    :param display:              The LED matrix display object to set the brightness on
    :param old_brightness_value: The previous brightness value
    :param min_brightness:       The minimum brightness supported by the LED matrix
    :param max_brightness:       The maximum brightness supported by the LED matrix

    :return: The brightness value

    :see: https://openweathermap.org/api/one-call-api#example
    """

    brightness_value = int(remap(pot.read(), min_brightness, max_brightness))

    if old_brightness_value != brightness_value:
        print("Read " + str(pot.read()) + " from A0, mapped to brightness " + str(brightness_value) + " (old value was " + str(old_brightness_value) + ")")
        display.brightness(brightness_value)

    return brightness_value

# Fn: get_weather()
def get_weather(lat, lon, api_key):
    """
    Fetches the daily weather forecast for a given
    location from OpenWeatherMap.

    :param lat:     Latitude of the location for which you want the forecast
    :param lon:     Longitude of the location for which you want the forecast
    :param api_key: API Key for [OpenWeatherMap](https://openweathermap.org)

    :return: response object

    :see: https://openweathermap.org/api/one-call-api#example
    """
    request_url = 'https://api.openweathermap.org/data/3.0/onecall' + \
        '?lat=' + str(lat) + \
        '&lon=' + str(lon) + \
        '&appid=' + str(api_key) + \
        '&exclude=current,minutely,hourly,alerts' + \
        '&units=metric' + \
        '&lang=en'

    try:
        response = requests.get(request_url)

        # If the response was not successful, return
        if response.status_code != 200:
            print("Weather API error:", str(response.status_code))
            return None

        # Get daily forecast part
        json_data = response.json()['daily']

        # Return just the daily forecasts for the next 3 days (memory reasons)
        return [ json_data[0], json_data[1], json_data[2] ]
    except Exception as err:
        print ("Exception in request:", err.__class__.__name__, err)
        raise err



# Map from OpenWeatherMap 'Main' conditions to 8x8 icons
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
conditions_map = {
    'Thunderstorm': 'CONDITIONS_STORM',
    'Drizzle':      'CONDITIONS_RAIN',
    'Rain':         'CONDITIONS_RAIN',
    'Snow':         'CONDITIONS_SNOW',
    'Mist':         'CONDITIONS_FOG',
    'Smoke':        'CONDITIONS_FOG',
    'Haze':         'CONDITIONS_FOG',
    'Dust':         'CONDITIONS_FOG',
    'Fog':          'CONDITIONS_FOG',
    'Sand':         'EXCLAMATION_MARK',
    'Ash':          'EXCLAMATION_MARK',
    'Squall':       'EXCLAMATION_MARK',
    'Tornado':      'EXCLAMATION_MARK',
    'Clear':        'CONDITIONS_SUNNY',
    'Clouds':       'CONDITIONS_CLOUDY'
}

# #############################################################################
# #############################################################################
# #############################################################################

# Declarations
spi     = SPI(1, baudrate=SPI_BAUDRATE, polarity=0, phase=0)
display = Matrix8x8(spi, Pin(CS_PIN, Pin.OUT), NUM_MATRICES)
wifi    = WLAN(STA_IF)
pot     = ADC(0)

# Leds
led_0 = Signal(LED_0_PIN, Pin.OUT, invert=True)
led_2 = Signal(LED_2_PIN, Pin.OUT, invert=False)
led_1 = Signal(LED_1_PIN, Pin.OUT, invert=False)

# Insertion detection
insertion = Signal(INSERTION_PIN, Pin.IN)

# Read brightness from trim pot at A0 and set it
brightness = set_matrix_brightness(pot, display, 0)

# Draw WiFi symbol
led_0.on()
led_2.on()
symbols.draw(symbols.WIFI, matrix=display, display=1, clear=True)
sleep(0.5)

# Enable garbage collector
gc.enable()

# Connect to WiFi
if not wifi.isconnected():
    print("Connecting to WiFI '" + secrets.WIFI_SSID + '"')
    wifi.active(True)
    wifi.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
    while not wifi.isconnected():
        pass

    print('WiFi connected. Local IP: ', wifi.ifconfig()[0])

# Print free memory
print("Free memory: " + str(gc.mem_free()) + " bytes.")

# Set two timer
update_time = ticks_ms() - QUERY_DELAY
blink_time  = ticks_ms() - BLINK_DELAY

# Turn off all LEDs
led_2.off()
led_1.off()
led_0.off()

# Set time from NTP server
print('Setting time from NTP...')
try:
    settime()
except OSError as error:
    print('Failed to set time from NTP: ' + str(error))
    pass
print('Now: {}'.format(localtime()))

# #############################################################################

# Main loop
while True:

    # Prepare a failure counter
    failure_count = 0

    # If power jack is removed, lower brightness
    if insertion.value() == 0:
        display.brightness(0)
    else:
        # Read brightness from trim pot at A0 and set on display
        brightness = set_matrix_brightness(pot, display, brightness)

    # Turn off the display at night (if configured)
    current_hour = localtime()[3]
    if(current_hour >= secrets.DISPLAY_OFF_START or current_hour < secrets.DISPLAY_OFF_END):
        # If we're in night mode, turn off the display
        display.off()
    else:
        # If the display was off, turn it on and reset update_time to trigger a refresh
        if display.is_off():
            display.on()
            update_time = ticks_ms() + QUERY_DELAY

    # If we lose WiFi connection, reboot ESP8266
    if not wifi.isconnected():
        symbols.draw(symbols.WIFI, matrix=display, display=1, clear=True)
        sleep(3)
        print("WiFi disconnected, resetting.")
        led_2.on()
        led_1.on()
        sleep(1)
        reset()

    # Query and get weather JSON every QUERY_DELAY ms
    if ticks_ms() - update_time >= QUERY_DELAY:
        # Turn on LED
        led_1.on()

        # Set time from NTP server
        print('Setting time from NTP...')
        try:
            settime()
        except OSError as error:
            print('Failed to set time from NTP: ' + str(error))
            pass
        print('Now: {}'.format(localtime()))

        print('Fetching weather for ' + secrets.GEO_NAME + '...')
        try:
            weather = get_weather(secrets.GEO_LAT, secrets.GEO_LON, secrets.OW_API_KEY)
            print("Fetched weather successfully")

            # Clear failure counter
            failure_count = 0

        except Exception as err:
            print("Failed to fetch weather!")
            failure_count += 1
            weather = None

        # If the response failed FAILURE_THRESHOLD times, display ! ! !
        if weather == None and failure_count >= FAILURE_THRESHOLD:
            print("Failed to fetch weather " + str(FAILURE_THRESHOLD) + " times!")

            # Clear display
            display.fill(0)

            if not display.is_off():
                # Loop: 0, 1, 2
                for day in range(0, NUM_MATRICES):
                    symbols.draw(symbols.EXCLAMATION_MARK, matrix=display, display=day)

            # Display symbols
            display.show()

        # If the response was successful, update the LED matrices
        if weather != None:

            # Clear display
            display.fill(0)

            if not display.is_off():
                # Loop: 0, 1, 2
                for day in range(0, NUM_MATRICES):
                    condition = weather[day]['weather'][0]['main']
                    symbol_name = conditions_map.get(condition, symbols.QUESTION_MARK)
                    print("Day " + str(day) + ": " + condition + ' (' + symbol_name + ')')
                    symbol_data = getattr(symbols, symbol_name)
                    symbols.draw(symbol_data, matrix=display, display=day)

            # Display symbols
            display.show()

        # Turn off LED
        led_1.off()

        # Clean up
        response  = None
        condition = None

        # Collect garbage
        gc.collect()

        # Print free memory
        print("Free memory: " + str(gc.mem_free()) + " bytes.")

        # Reset update time
        update_time = ticks_ms()

    # Blink LED 2 led if BLINK_DELAY ms have passed since last blink
    if ticks_ms() - blink_time >= BLINK_DELAY:
        led_2.on()
        sleep(0.05)
        led_2.off()
        blink_time = ticks_ms()

    # Sleep
    sleep(0.1)
