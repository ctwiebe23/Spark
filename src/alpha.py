import board

FRQ = 50

GROVE_PIN = {
    9 : (board.GP2 , board.GP3 ),
    10: (board.GP4 , board.GP5 ),
    11: (board.GP16, board.GP17),
    12: (board.GP6 , board.GP26),
    13: (board.GP26, board.GP27),
}

largemotors = []
smallmotors = []

# for reversing servos and dc motors
reversed = -1