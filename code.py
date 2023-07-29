import board
import hardware_utils
import digitalio

button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if not button.value:
        while not button.value:
            pass
        hardware_utils.jiggle_mouse()