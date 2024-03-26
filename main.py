# Python code
basic.show_icon(IconNames.HAPPY)
basic.show_string("vamos começar")

def on_forever():
    if input.sound_level() < 50:
        pins.servo_write_pin(AnalogPin.P2, 72)
    else:
        pins.servo_write_pin(AnalogPin.P2, 0)
basic.forever(on_forever)
