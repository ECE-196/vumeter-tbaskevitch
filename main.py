import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value
    print(volume)

    thresholds = [38000, 37000, 36000, 35000, 34000, 33000, 32000, 31000, 30000, 29000, 28000]

    for i in range(10, -1, -1):
        if volume > thresholds[10 - i]:
            leds[i].value = 1
            
        else:
            if leds[i].value == 1:
                sleep(0.06)
                
            leds[i].value = 0
        

