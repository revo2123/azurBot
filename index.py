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
#input variables
totalTimesInput = int(input('Total Runs: '))
#init screenSize
screenSize = Screen()
#init mouse
mouse = Controller()
#continue Button
cntBtn = Btn(int(percentToPixel(screenSize.width, 0.7104)), int(percentToPixel(screenSize.height, 0.8258)), 90, 142, 214)
#go Buttons
goBtn1 = Btn(int(percentToPixel(screenSize.width, 0.744)), int(percentToPixel(screenSize.height, 0.704)), 90, 142, 214) # input correct color values for go buttons
goBtn2 = Btn(int(percentToPixel(screenSize.width, 0.829)), int(percentToPixel(screenSize.height, 0.81)), 90, 142, 214)


#main function
def main():
    print('-- Started --')
    runCount = 0
    
    isGoBtn = pyscreeze.pixelMatchesColor(goBtn1.x, goBtn1.y, (goBtn1.color.r, goBtn1.color.g, goBtn1.color.b), tolerance=10)
    if isGoBtn:
        clickBtn(goBtn1)
        print('Go_1 Clicked')
        time.sleep(0.5)
        clickBtn(goBtn2)
        print('Go_2 Clicked')
    runCount += 1
    
    while True:
        if runCount < totalTimesInput:
            #check for continue button
            isCntBtn = pyscreeze.pixelMatchesColor(cntBtn.x, cntBtn.y, (cntBtn.color.r, cntBtn.color.g, cntBtn.color.b), tolerance=10)
            #if continue button is visible
            if isCntBtn:
                clickBtn(cntBtn)
                runCount += 1
                print('Continue clicked')
            time.sleep(1)
        else:
            print('-- Finnished --')
            break

#calling main function
main()
