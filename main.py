def on_forever():
    basic.show_leds("""
        . . # . .
        . # . . .
        # # # # #
        . # . . .
        . . # . .
        """)
    basic.show_leds("""
        # . . . .
        . . . . .
        # # # . .
        . . . . .
        # . . . .
        """)
    basic.clear_screen()
    if pins.analog_read_pin(AnalogPin.P1) > 500:
        for index in range(2):
            basic.show_icon(IconNames.HEART)
            pins.servo_write_pin(AnalogPin.P0, 110)
            basic.pause(100)
            pins.servo_write_pin(AnalogPin.P0, 0)
            basic.pause(100)
        basic.clear_screen()
        basic.show_icon(IconNames.HAPPY)
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            # . . . #
            . # # # .
            """)
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . #
            . . . # .
            . . # # #
            . . . # .
            . . . . #
            """)
        pins.servo_write_pin(AnalogPin.P0, 0)
basic.forever(on_forever)
