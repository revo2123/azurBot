#Disclaimer: might just buy some useless shit on accident, no warranty of function given
#startup message
print('PG -- Azur Bot -- v.1.1.0 -- Script\n')

#import libsfrom pynput.mouse import Button, Controller
from pynput.mouse import Button, Controller
import pyscreeze
import time
#importing classes
from classes.Screen import Screen
from classes.Button import Btn
        
#helper functions
def percentToPixel(size, percent):
    return (size * percent)

def leftClick():
    mouse.press(Button.left)
    mouse.release(Button.left)

def clickBtn(btn):
    mouse.position = (btn.x, btn.y)
    leftClick()
    
def calcTime(startRunTime, endRunTime):
    showMinutes = 0
    
    timeDiff = endRunTime - startRunTime
    leftOverSec = timeDiff
    showSec = timeDiff
    while leftOverSec >= 60:
        showMinutes += 1
        leftOverSec -= 60
        showSec = timeDiff % 60

    if str(len(str(int(showSec)))) == '1':
        timeToClear = str(showMinutes) + ':0' + str(int(showSec))
    else:
        timeToClear = str(showMinutes) + ':' + str(int(showSec))
    return timeToClear


#init global variables
#input variables
totalTimesInput = int(input('\nTotal Runs: '))
#init screenSize
screenSize = Screen()
#init mouse
mouse = Controller()
#continue Button
cntBtn = Btn(int(percentToPixel(screenSize.width, 0.7104)), int(percentToPixel(screenSize.height, 0.8258)), 90, 142, 214)
#go Buttons
goBtn1 = Btn(int(percentToPixel(screenSize.width, 0.811)), int(percentToPixel(screenSize.height, 0.679)), 247, 202, 66)
goBtn2 = Btn(int(percentToPixel(screenSize.width, 0.896)), int(percentToPixel(screenSize.height, 0.7925)), 247, 202, 66)


#main function 
def main():
    #time counters
    startRunTime = None
    endRunTime = None
    
    time.sleep(5)
    
    runCount = 0
    print('\n-- Started --')
    
    isGoBtn = pyscreeze.pixelMatchesColor(goBtn1.x, goBtn1.y, (goBtn1.color.r, goBtn1.color.g, goBtn1.color.b), tolerance=0)
    if isGoBtn:
        print('\tStarting / Run_Nr.: ' + str(runCount + 1))
        
        #click first go_button
        clickBtn(goBtn1)
        print('\t\tGo_1 Clicked (' + time.strftime("%H:%M:%S") + ')')
        time.sleep(0.5)
        
        #click second go_button
        clickBtn(goBtn2)
        print('\t\tGo_2 Clicked (' + time.strftime("%H:%M:%S") + ')')
        
        #start timer
        startRunTime = time.time()
    
    while True:
        #check for continue button
        isCntBtn = pyscreeze.pixelMatchesColor(cntBtn.x, cntBtn.y, (cntBtn.color.r, cntBtn.color.g, cntBtn.color.b), tolerance=0)
        
        if runCount < totalTimesInput:
            #if continue button is visible
            if isCntBtn:
                #set endRunTime if startRunTime is already set and calculate passed time
                if startRunTime:
                    runCount += 1
                    endRunTime = time.time()
                    print('\tFinnished / Run_Nr.: ' + str(runCount) + '\tTime: ' + calcTime(startRunTime, endRunTime))
                
                #start new run
                print('\tStarting / Run_Nr.: ' + str(runCount + 1))
                
                #set start time
                startRunTime = time.time()
                
                #click continue button
                clickBtn(cntBtn)
                print('\t\tContinue clicked (' + time.strftime("%H:%M:%S") + ')')
                
                #update runCount
                runCount += 1
                
                #timeout
                time.sleep(1)
        else:
            #if continue button is visible
            if isCntBtn:
                #set final end time and calculate passed time
                endRunTime = time.time()
                print('\tFinnished / Run_Nr.: ' + str(runCount) + '\tTime: ' + calcTime(startRunTime, endRunTime))
                
                #end loop
                print('-- Finnished --')
                break
            
            
#calling main function
main()
