# symbols.py
#
# https://xantorohara.github.io/led-matrix-editor/#185a66bddb663c00|894218bc3d184291|001ea1a919a6c0ec|00007e818999710e|152a547e8191710e|0a04087e8191710e|55aa55aa55aa55aa|a542a51818a542a5|180018183c3c1800|1800183860663c00

# WiFi Symbol
WIFI = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 1, 1, 0, 0 ],
    [ 0, 1, 1, 0, 0, 1, 1, 0 ],
    [ 1, 1, 0, 1, 1, 0, 1, 1 ],
    [ 1, 0, 1, 1, 1, 1, 0, 1 ],
    [ 0, 1, 1, 0, 0, 1, 1, 0 ],
    [ 0, 1, 0, 1, 1, 0, 1, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ]
]

# Clear / Sunny
CONDITIONS_SUNNY = [
    [ 1, 0, 0, 0, 1, 0, 0, 1 ],
    [ 0, 1, 0, 0, 0, 0, 1, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 1, 0, 1, 1, 1, 1, 0, 0 ],
    [ 0, 0, 1, 1, 1, 1, 0, 1 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 1, 0, 0, 0, 0, 1, 0 ],
    [ 1, 0, 0, 1, 0, 0, 0, 1 ]
]

# Sun/Cloud
CONDITIONS_OVERCAST = [
    [ 0, 0, 1, 1, 0, 1, 1, 1 ],
    [ 0, 0, 0, 0, 0, 0, 1, 1 ],
    [ 0, 1, 1, 0, 0, 1, 0, 1 ],
    [ 1, 0, 0, 1, 1, 0, 0, 0 ],
    [ 1, 0, 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 0, 0, 0, 1, 0, 1 ],
    [ 0, 1, 1, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ]
]

 # Cloudy
CONDITIONS_CLOUDY = [
    [ 0, 1, 1, 1, 0, 0, 0, 0 ],
    [ 1, 0, 0, 0, 1, 1, 1, 0 ],
    [ 1, 0, 0, 1, 1, 0, 0, 1 ],
    [ 1, 0, 0, 1, 0, 0, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 1 ],
    [ 0, 1, 1, 1, 1, 1, 1, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ]
]

# Rain
CONDITIONS_RAIN = [
    [ 0, 1, 1, 1, 0, 0, 0, 0 ],
    [ 1, 0, 0, 0, 1, 1, 1, 0 ],
    [ 1, 0, 0, 0, 1, 0, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 1 ],
    [ 0, 1, 1, 1, 1, 1, 1, 0 ],
    [ 0, 0, 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1, 0, 0 ],
    [ 1, 0, 1, 0, 1, 0, 0, 0 ]
]

# Thunderstorm
CONDITIONS_STORM = [
    [ 0, 1, 1, 1, 0, 0, 0, 0 ],
    [ 1, 0, 0, 0, 1, 1, 1, 0 ],
    [ 1, 0, 0, 0, 1, 0, 0, 1 ],
    [ 1, 0, 0, 0, 0, 0, 0, 1 ],
    [ 0, 1, 1, 1, 1, 1, 1, 0 ],
    [ 0, 0, 0, 1, 0, 0, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0 ],
    [ 0, 1, 0, 1, 0, 0, 0, 0 ]
]

# Fog
CONDITIONS_FOG = [
    [ 0, 1, 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0, 1, 0 ],
    [ 0, 1, 0, 1, 0, 1, 0, 1 ],
    [ 1, 0, 1, 0, 1, 0, 1, 0 ]
]

# Snow
CONDITIONS_SNOW = [
    [ 1, 0, 1, 0, 0, 1, 0, 1 ],
    [ 0, 1, 0, 0, 0, 0, 1, 0 ],
    [ 1, 0, 1, 0, 0, 1, 0, 1 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 1, 0, 1, 0, 0, 1, 0, 1 ],
    [ 0, 1, 0, 0, 0, 0, 1, 0 ],
    [ 1, 0, 1, 0, 0, 1, 0, 1 ]
]

# Exclamation Mark
EXCLAMATION_MARK = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 1, 1, 1, 1, 0, 0 ],
    [ 0, 0, 1, 1, 1, 1, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ]
]

# Question Mark
QUESTION_MARK = [
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 1, 1, 1, 1, 0, 0 ],
    [ 0, 1, 1, 0, 0, 1, 1, 0 ],
    [ 0, 0, 0, 0, 0, 1, 1, 0 ],
    [ 0, 0, 0, 1, 1, 1, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 1, 1, 0, 0, 0 ]
]

# Fn: draw()
def draw(symbol, matrix, display=0, clear=False):
    """
    Draws a symbol on a given LED matrix display. The parameter `clear`
    is set to `False` by default, meaning neither will the matrix be
    cleared, nor will `display()` be called. This is required if multiple
    calls to `draw()` are being made to draw onto different matrix displays.

    :param symbol:  The symbol to draw (8x8 array)
    :param matrix:  The matrix object
    :param display: The number of the display in the series to draw onto
    :param clear:   Whether the matrix should be cleared before drawing
    """

    # If clear is set to True, clear the whole matrix
    if clear:
        matrix.fill(0)

    for row in range(0,8):
        for col in range(0,8):
            # The displays are rotated 180°, so it's `7 - [actual row/col]`
            matrix.pixel(7-col+(display*8), 7-row, symbol[row][col])

    # If clear is set to True, display the matrix
    if clear:
        matrix.show()

    row = None
    col = None
