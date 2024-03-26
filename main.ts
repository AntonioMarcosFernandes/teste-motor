// Python code
basic.showIcon(IconNames.Happy)
basic.showString("vamos começar")
basic.forever(function () {
    if (input.soundLevel() < 50) {
        pins.servoWritePin(AnalogPin.P2, 72)
    } else {
        pins.servoWritePin(AnalogPin.P2, 0)
    }
})
