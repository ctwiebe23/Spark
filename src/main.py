import make


forward  = make.button( 1 )
backward = make.button( 2 )
servo    = make.smallmotor( 3 )


while True:  # loops forever

    if forward.pressed():
        servo.spin( 100 )

    if backward.pressed():
        servo.spin( -100 )

    if forward.pressed() and backward.pressed():
        servo.stop()

    make.pause()  # pause briefly before looping
