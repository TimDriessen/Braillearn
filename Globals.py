from Dicts import *
import os
import Constant as c
import RPi.GPIO as GPIO

# Global states:
#  0 = Tutoiral
#  1 = Main program
#  To be continued
globalState = 0
taskRunning = False
abort = False

WRITE_PINS = []
buttonState = [0,0,0,0] # In order: [RST, NXT, LVLUP, LVLDOWN]
brailleState = [0,0,0,0,0,0]
binInput = 0
lastBinInput = 0

task = 1
taskFile = '' 
TaskDir = './Tasks'
taskCount = len([name for name in os.listdir(TaskDir) if os.path.isfile(os.path.join(TaskDir,name))])

GPIO.setmode(GPIO.BOARD)
for pin in range(len(c.BRAILLE_WRITE_PAD)):
    GPIO.setup(c.BRAILLE_WRITE_PAD[pin],GPIO.OUT)
    WRITE_PINS.append(GPIO.PWM(c.BRAILLE_WRITE_PAD[pin],40000))
    WRITE_PINS[pin].start(0)

#Global callbacks to call when buttons are pressed

def callback0(channel):
    global binInput
    global brailleState
    if brailleState[0] == 0:
        binInput += 1
        brailleState[0] = 1
    WRITE_PINS[0].ChangeDutyCycle(60)
    print(brailleState)

def callback1(channel):
    global binInput
    global brailleState
    if brailleState[1] == 0:
        binInput += 2
        brailleState[1] = 1
    WRITE_PINS[1].ChangeDutyCycle(60)
    print(brailleState)

def callback2(channel):
    global binInput
    global brailleState
    if brailleState[2] == 0:
        binInput += 4
        brailleState[2] = 1
    WRITE_PINS[2].ChangeDutyCycle(60)
    print(brailleState)

def callback3(channel):
    global binInput
    global brailleState
    if brailleState[3] == 0:
        binInput += 8
        brailleState[3] = 1
    WRITE_PINS[3].ChangeDutyCycle(60)
    print(brailleState)

def callback4(channel):
    global binInput
    global brailleState
    if brailleState[4] == 0:
        binInput += 16
        brailleState[4] = 1
    WRITE_PINS[4].ChangeDutyCycle(60)
    print(brailleState)

def callback5(channel):
    global binInput
    global brailleState
    if brailleState[5] == 0:
        binInput += 32
        brailleState[5] = 1
    WRITE_PINS[5].ChangeDutyCycle(60)
    print(brailleState)

def callbackRST(channel):
    global binInput
    global brailleState
    global buttonState
    brailleState = [0,0,0,0,0,0]
    binInput = 0
    buttonState[0] = 1
    for pin in range(len(WRITE_PINS)):
        WRITE_PINS[pin].ChangeDutyCycle(0)

def callbackNXT(channel):
    global binInput
    global brailleState
    global lastBinInput
    global buttonState
    lastBinInput = binInput
    brailleState = [0,0,0,0,0,0]
    binInput = 0
    buttonState[1] = 1
    for pin in range(len(WRITE_PINS)):
        WRITE_PINS[pin].ChangeDutyCycle(0)
        
def callbackLVLUP(channel):
    global buttonState
    global abort
    print('callbackLVLUP called')
    #callbackNXT(channel)
    buttonState[2] = 1
    
    if (globalState == 1): # To make abort action immediately take effect
        abort = True

def callbackLVLDOWN(channel):
    global buttonState
    global abort
    print('callbackLVLDOWN called')
    #callbackNXT(channel)
    buttonState[3] = 1
    
    if (globalState == 1): # To make abort action immediately take effect
        abort = True

# c h e c k S t a t e (button_name)
# ===============================
# Returns state of button 'button_name'
#
def checkBtnState(button_name):
    state = False
    
    if (button_name == 'RST'):
       state = buttonState[0]
    elif (button_name == 'NXT'):
        state = buttonState[1]
    elif (button_name == 'LVLUP'):
        state = buttonState[2]
    elif (button_name == 'LVLDOWN'):
        state = buttonState[3]
        
    return state

# s e t S t a t e (button_name)
# ===============================
# Returns state of button 'button_name'
#
def setBtnState(button_name, state):
    global buttonState
    
    if (button_name == 'RST'):
       buttonState[0] = state
    elif (button_name == 'NXT'):
        buttonState[1] = state 
    elif (button_name == 'LVLUP'):
        buttonState[2] = state 
    elif (button_name == 'LVLDOWN'):
        buttonState[3] = state
        
# n u m b e r O f P r e s s e s ()
# ===============================
# Returns number of buttons which have been pressed (and not reset)
#
def numberOfBtnPresses():
    presses = 0
    for i in buttonState:
        if (i == True):
            presses += 1
    return presses

# r e s e t B u t t o n S t a t e s ()
# ===============================
# Resets all button states to 0
#
def resetBtnStates():
    global buttonState
    buttonState = [0,0,0,0]