#Disclaimer: might just buy some useless shit on accident, no warranty of function given


#import libsfrom pynput.mouse import Button, Controller
from pynput.mouse import Button, Controller
from win32api import GetSystemMetrics
import pyscreeze
import time


#class definition
class Btn:
    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.color = Color(r, g, b)

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class Screen:
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
        
#helper functions
def percentToPixel(size, percent):
    return (size * percent)

def leftClick():
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickBtn(btn):
    mouse.position = (btn.x, btn.y)
    leftClick()


#init global variables
#startup message
print('PG -- Azur Bot -- v.1.0.0\n')
#input variables
totalTimesInput = int(input('Total Runs: '))
#init screenSize
screenSize = Screen()
#init mouse
mouse = Controller()
#continue Button
cntBtn = Btn(int(percentToPixel(screenSize.width, 0.7104)), int(percentToPixel(screenSize.height, 0.8258)), 90, 142, 214)
#go Buttons
goBtn1 = Btn(int(percentToPixel(screenSize.width, 0.811)), int(percentToPixel(screenSize.height, 0.679)), 247, 202, 66) # input correct color values for go buttons
goBtn2 = Btn(int(percentToPixel(screenSize.width, 0.896)), int(percentToPixel(screenSize.height, 0.7925)), 247, 202, 66)


#main function 
def main():
    time.sleep(5)
    runCount = 0
    print('-- Started --')
    isGoBtn = pyscreeze.pixelMatchesColor(goBtn1.x, goBtn1.y, (goBtn1.color.r, goBtn1.color.g, goBtn1.color.b), tolerance=10)
    if isGoBtn:
        print('\tStarting / Run_Nr.: ' + str(runCount + 1))
        clickBtn(goBtn1)
        print('\t\tGo_1 Clicked (' + time.strftime("%H:%M:%S") + ')')
        time.sleep(0.5)
        clickBtn(goBtn2)
        print('\t\tGo_2 Clicked (' + time.strftime("%H:%M:%S") + ')')
        runCount += 1
    
    while True:
        #check for continue button
        isCntBtn = pyscreeze.pixelMatchesColor(cntBtn.x, cntBtn.y, (cntBtn.color.r, cntBtn.color.g, cntBtn.color.b), tolerance=10)
        #if continue button is visible
        if runCount < totalTimesInput:
            if isCntBtn:
                print('\tStarting / Run_Nr.: ' + str(runCount + 1))
                clickBtn(cntBtn)
                runCount += 1
                print('\t\tContinue clicked (' + time.strftime("%H:%M:%S") + ')')
                time.sleep(1)
        else:
            if isCntBtn:
                print('-- Finnished --')
                break
            
#calling main function
main()
