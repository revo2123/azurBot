#Disclaimer: might just buy some useless shit on accident, no warranty of function given
#dev

#import libs
from pynput.mouse import Button, Controller
import time


#init global variables
width = float(input('Width: '))
height = float(input('Height: '))
totalTimesInput = int(input('Total Runs: '))
mouse = Controller()


#helperfunctions
def percentToPixel(size, percent):
    return (size * percent / 100)

def leftClick():
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickGo():
    #Click "GO" 1
    mouse.position = (percentToPixel(width, 74.4), percentToPixel(height, 70.4))
    leftClick()
    time.sleep(0.5)
    #Click "GO" 2
    mouse.position = (percentToPixel(width, 82.9), percentToPixel(height, 81))
    leftClick()
    
def clickContinue():
    #Click "Continue"
    mouse.position = (percentToPixel(width, 65), percentToPixel(height, 82))
    leftClick()


#init
def main():
    runCount = 0
    time.sleep(1)
    #clickGo()
    runCount += 1
    # startTime = time.time() TODO: add time counter
    print('\nRun_Nr.: ' + str(runCount) + ' (' + str(time.strftime('%H:%M:%S')) + ')')
    while (runCount < totalTimesInput):
        #clickContinue()
        #TODO: if first time click "GO" if any other time click "continue", track time in between clicks, register end of stage
        runCount += 1
        print('Run_Nr.: ' + str(runCount) + ' (' + str(time.strftime('%H:%M:%S')) + ')')


#calling main function
main()

