input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showString("HAPPY!")
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    basic.showNumber(randint(1, 6))
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showNumber(input.temperature())
})
pins.servoWritePin(AnalogPin.P0, 90)
basic.forever(function () {
    basic.showIcon(IconNames.Asleep)
    if (pins.analogReadPin(AnalogPin.P1) > 500) {
        basic.showIcon(IconNames.Heart)
        pins.servoWritePin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P0, 90)
        basic.showIcon(IconNames.Happy)
        basic.showLeds(`
            . . . . .
            . # . . .
            . . . . .
            # . . . #
            . # # # .
            `)
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
