from pynput.mouse import Button, Controller
import pyscreeze
import time

mouse = Controller()

def percentToPixel(size, percent):
    return (size * percent)

mouse.position = (1363, 990)

while True:
    print('Pixel: ' +  str(mouse.position))
    print('Color: ' + str(pyscreeze.pixel(mouse.position[0], mouse.position[1])) + '\n')
    time.sleep(0.1)
