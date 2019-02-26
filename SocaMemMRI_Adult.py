#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03), Tue Oct 13 11:47:47 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle, seed
import os  # handy system and path functions
from copy import deepcopy
import itertools

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SocaMemMRIAdult'  # from the Builder filename that created this script
expInfo = {u'Version': u'1A', u'mriMode': u'on', u'Subject': u'SocaMRI'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['Subject'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
endExpNow = False  # flag for 'escape' or other condition => quit the exp
#onsFile_Cue=open(_thisDir + os.sep + 'onsets/%s_%s_cue_%s.txt' %(expInfo['Subject'], expInfo['Version'], expInfo['date']),'w')
# Start Code - component code to be run before the window creation

# Setup the Window
if expInfo['mriMode']=='on':
    win = visual.Window(size=(1280, 1024), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        )
else:
    win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
        monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
        blendMode='avg', useFBO=True,
        )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstrText = visual.TextStim(win=win, ori=0, name='InstrText',
    text="Welcome to the First Impressions Task!\n\nOther participants rated whether they liked you based on your picture. \n\nDuring this task, your job is to guess whether or not the other person liked you. After that, you will be shown what they actually said.\n\n\n\n\nPress 'Yes' to begin.",    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.6,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
m = event.Mouse()
m.setVisible(False)

# Initialize components for Routine "Get_Ready"
Get_ReadyClock = core.Clock()
getReadyText = visual.TextStim(win=win, ori=0, name='getReadyText',
    text='default text',    font='Arial',
    pos=[0, 0], height=.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "WaitScanner"
WaitScannerClock = core.Clock()
waitScannerText = visual.TextStim(win=win, ori=0, name='waitScannerText',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=.08, wrapWidth=None,
    color=[0.600,0.600,0.600], colorSpace='rgb', opacity=1,
    depth=-2.0)

trigger = 'usb'
# for GSR sync
import serial
class HvdSerial(serial.Serial):
    DEVICES = {0:'BNC',1:'Parallel'}
    def __init__(self,**args):
        try:
            self._device_present = True
            super(HvdSerial,self).__init__(**args)
            logging.exp('Created device %s' % args['port'])
        except serial.SerialException:
            self._device_present = False
            logging.warn('No Serial Device Found.')

    def writeUSB(self,dest,val):
        if self._device_present:
            self.write(chr(dest))
            self.write(chr(val))
        logging.exp('Serial: Wrote %s (%s) to %s (%s)'%(
            val, "{0:08b}".format(val), dest, self.DEVICES[dest]
        ))

ser = HvdSerial(port='/dev/tty.usbmodem12341',timeout=1)
# Zero Out Parallel & BNC
ser.writeUSB(0,0)
core.wait(.3)
ser.writeUSB(1,0)
core.wait(.3)

CUE_PINS = int('00000001', 2)
DELAY_ACCEPT_PINS = int('00000010', 2)
DELAY_REJECT_PINS = int('00000100', 2)
FEEDBACK_CONACCEPT = int('00001000',2)
FEEDBACK_CONREJECT = int('00010000', 2)
FEEDBACK_INCONACCEPT = int('00100000',2)
FEEDBACK_INCONREJECT = int('01000000',2)
MISSED = int('10000000',2)

# Initialize components for Routine "Cue"
CueClock = core.Clock()
peerPhotoCue = visual.ImageStim(win=win, name='peerPhotoCue', units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[542,620],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
allowable_keys = {
    '1': 'Yes',
    '2': 'No'
}
PredictText = visual.TextStim(win=win, ori=0, name='PredictText',
    text='default text',    font='Arial',
    pos=[-0.75, 0], height=.18, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "Delay"
DelayClock = core.Clock()
delay = visual.ImageStim(win=win, name='delay', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
delayText = visual.TextStim(win=win, ori=0, name='delayText',
    text='default text',    font='Arial',
    pos=[0,0], height=0.18, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
polygon_2 = visual.Polygon(win=win, name='polygon_2',
    edges = 90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
PeerPhotoFeedback = visual.ImageStim(win=win, name='PeerPhotoFeedback', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
peerEval = visual.TextStim(win=win, ori=0, name='peerEval',
    text='default text',    font='Arial',
    pos=[.75, 0], height=0.18, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
predictText = visual.TextStim(win=win, ori=0, name='predictText',
    text='default text',    font='Arial',
    pos=[-0.75, 0], height=0.18, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
polygon = visual.Polygon(win=win, name='polygon',
    edges = 90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,interpolate=True)
polygon_3 = visual.Polygon(win=win, name='polygon_3',
    edges = 90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,interpolate=True)

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, ori=0, name='fix',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "EndRun"
EndRunClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
scannerStart = core.Clock()


#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
InstrContinue = event.BuilderKeyResponse()  # create an object of type KeyResponse
InstrContinue.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(InstrText)
InstructionsComponents.append(InstrContinue)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if t >= 0.0 and InstrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText.tStart = t  # underestimates by a little under one frame
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.setAutoDraw(True)
    
    # *InstrContinue* updates
    if t >= 0.0 and InstrContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrContinue.tStart = t  # underestimates by a little under one frame
        InstrContinue.frameNStart = frameN  # exact frame index
        InstrContinue.status = STARTED
        # keyboard checking is just starting
    if InstrContinue.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
runLooper = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('conditions/runLooperFile.xlsx'),
    seed=None, name='runLooper')
thisExp.addLoop(runLooper)  # add the loop to the experiment
thisRunLooper = runLooper.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRunLooper.rgb)
if thisRunLooper != None:
    for paramName in thisRunLooper.keys():
        exec(paramName + '= thisRunLooper.' + paramName)

for thisRunLooper in runLooper:
    currentLoop = runLooper
    # abbreviate parameter names if possible (e.g. rgb = thisRunLooper.rgb)
    if thisRunLooper != None:
        for paramName in thisRunLooper.keys():
            exec(paramName + '= thisRunLooper.' + paramName)
    
    #------Prepare to start Routine "Get_Ready"-------
    t = 0
    Get_ReadyClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    getReadyText.setText('Get Ready!')
    advanceScreen = event.BuilderKeyResponse()  # create an object of type KeyResponse
    advanceScreen.status = NOT_STARTED
    # keep track of which components have finished
    Get_ReadyComponents = []
    Get_ReadyComponents.append(getReadyText)
    Get_ReadyComponents.append(advanceScreen)
    for thisComponent in Get_ReadyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Get_Ready"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Get_ReadyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *getReadyText* updates
        if t >= 0.0 and getReadyText.status == NOT_STARTED:
            # keep track of start time/frame for later
            getReadyText.tStart = t  # underestimates by a little under one frame
            getReadyText.frameNStart = frameN  # exact frame index
            getReadyText.setAutoDraw(True)
        
        # *advanceScreen* updates
        if t >= 0.0 and advanceScreen.status == NOT_STARTED:
            # keep track of start time/frame for later
            advanceScreen.tStart = t  # underestimates by a little under one frame
            advanceScreen.frameNStart = frameN  # exact frame index
            advanceScreen.status = STARTED
            # keyboard checking is just starting
            advanceScreen.clock.reset()  # now t=0
        if advanceScreen.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                advanceScreen.keys = theseKeys[-1]  # just the last key pressed
                advanceScreen.rt = advanceScreen.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Get_ReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Get_Ready"-------
    for thisComponent in Get_ReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if advanceScreen.keys in ['', [], None]:  # No response was made
       advanceScreen.keys=None
    # store data for runLooper (TrialHandler)
    runLooper.addData('advanceScreen.keys',advanceScreen.keys)
    if advanceScreen.keys != None:  # we had a response
        runLooper.addData('advanceScreen.rt', advanceScreen.rt)
    
    #------Prepare to start Routine "WaitScanner"-------
    t = 0
    WaitScannerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    scannerAdvance = event.BuilderKeyResponse()  # create an object of type KeyResponse
    scannerAdvance.status = NOT_STARTED
    waitScannerText.setText('Waiting for scanner...')
    # keep track of which components have finished
    WaitScannerComponents = []
    WaitScannerComponents.append(scannerAdvance)
    WaitScannerComponents.append(waitScannerText)
    for thisComponent in WaitScannerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "WaitScanner"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = WaitScannerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *scannerAdvance* updates
        if t >= 0.0 and scannerAdvance.status == NOT_STARTED:
            # keep track of start time/frame for later
            scannerAdvance.tStart = t  # underestimates by a little under one frame
            scannerAdvance.frameNStart = frameN  # exact frame index
            scannerAdvance.status = STARTED
            # keyboard checking is just starting
            scannerAdvance.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if scannerAdvance.status == STARTED:
            theseKeys = event.getKeys(keyList=['equal'])
         
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                scannerAdvance.keys = theseKeys[-1]  # just the last key pressed    
                scannerAdvance.rt = scannerAdvance.clock.getTime()
                scannerStart.reset()
                # a response ends the routine
                continueRoutine = False
                
                # Tell the GSR the task is started by raising all pins to 1
                ser.writeUSB(0,1)  # Raise BNC
                ser.writeUSB(1,int('11111111',2))  # Raise all pins for Parallel
                CueClock.reset()

        # *waitScannerText* updates
        if t >= 0.0 and waitScannerText.status == NOT_STARTED:
            # keep track of start time/frame for later
            waitScannerText.tStart = t  # underestimates by a little under one frame
            waitScannerText.frameNStart = frameN  # exact frame index
            waitScannerText.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WaitScannerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "WaitScanner"-------
    for thisComponent in WaitScannerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #expInfo['triggerWallTime'] = time.ctime()
# check responses
    if scannerAdvance.keys in ['', [], None]:  # No response was made
        scannerAdvance.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('scannerAdvance.keys',scannerAdvance.keys)
    if scannerAdvance.keys != None:  # we had a response
        thisExp.addData('scannerAdvance.rt', scannerAdvance.rt)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=data.importConditions(_thisDir + os.sep + 'conditions/SocaMRIConditions_Version%s_%s.xlsx' %(expInfo['Version'], Run)),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        #------Prepare to start Routine "Cue"-------
        t = 0
        CueClock.reset()  # clock 
        frameN = -1
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        peerPhotoCue.setImage(Cue)
        Prediction_Response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        Prediction_Response.status = NOT_STARTED
        responseMsg = ''
        # keep track of which components have finished
        CueComponents = []
        CueComponents.append(peerPhotoCue)
        CueComponents.append(Prediction_Response)
        CueComponents.append(PredictText)
        for thisComponent in CueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Cue"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            responseMsg = ''
            t = CueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if frameN== 0:
                ser.writeUSB(1, CUE_PINS)

            # *peerPhotoCue* updates
            if t >= 0.0 and peerPhotoCue.status == NOT_STARTED:
                event.clearEvents(eventType='keyboard')
                # keep track of start time/frame for later
                peerPhotoCue.tStart = t  # underestimates by a little under one frame
                peerPhotoCue.start = scannerStart.getTime()
                peerPhotoCue.frameNStart = frameN  # exact frame index
                peerPhotoCue.setAutoDraw(True)
                
            if peerPhotoCue.status == STARTED and t >= (0.0 + (3.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                peerPhotoCue.end = scannerStart.getTime()
                #onsFile_Cue.write('%f\t%f\t1\n'%(peerPhotoCue.start,(peerPhotoCue.end-peerPhotoCue.start)))
                peerPhotoCue.setAutoDraw(False)
            
            # *Prediction_Response* updates
            if t >= 0.0 and Prediction_Response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Prediction_Response.tStart = t  # underestimates by a little under one frame
                Prediction_Response.frameNStart = frameN  # exact frame index
                Prediction_Response.status = STARTED
                # keyboard checking is just starting
                Prediction_Response.clock.reset()  # now t=0
            if Prediction_Response.status == STARTED and t >= (3.0-win.monitorFramePeriod*0.75): #most of one frame period left
                Prediction_Response.status = STOPPED
            if Prediction_Response.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if Prediction_Response.keys == []:  # then this was the first keypress
                        Prediction_Response.keys = theseKeys[0]  # just the first key pressed
                        Prediction_Response.rt = Prediction_Response.clock.getTime()
                        if Prediction_Response.keys=='1':
                            pins = DELAY_ACCEPT_PINS
                        elif Prediction_Response.keys == '2':
                            pins = DELAY_REJECT_PINS
                        else:
                            raise StandardError("Not expecting key %s" % Prediction_Response.keys)
                        ser.writeUSB(1, pins)
            if Prediction_Response.keys:
                responseMsg = allowable_keys[Prediction_Response.keys]
                Prediction=True
            else:
                Prediction=False
            
            # *PredictText* updates
            if t >= 0 and PredictText.status == NOT_STARTED:
                # keep track of start time/frame for later
                PredictText.tStart = t  # underestimates by a little under one frame
                PredictText.frameNStart = frameN  # exact frame index
                PredictText.setAutoDraw(True)
            if PredictText.status == STARTED and t >= (3.0-win.monitorFramePeriod*0.75): #most of one frame period left
                PredictText.setAutoDraw(False)
            if PredictText.status == STARTED:  # only update if being drawn
                PredictText.setText(responseMsg, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Cue"-------
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Prediction_Response.keys in ['', [], None]:  # No response was made
           Prediction_Response.keys=None
        # store data for trials (TrialHandler)
        trials.addData('Prediction_Response.keys',Prediction_Response.keys)
        if Prediction_Response.keys != None:  # we had a response
            trials.addData('Prediction_Response.rt', Prediction_Response.rt)
        pins = int('00000000',2)
        ser.writeUSB(1,pins)
        
        #------Prepare to start Routine "Delay"-------
        t = 0
        DelayClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        delay.setImage(Cue)
        delay.setSize([542,620])
        delayText.setText(responseMsg)
        delayText.setPos([-0.75, 0])
        polygon_2.setFillColor([1,1,1])
        polygon_2.setPos([-.75, 0])
        polygon_2.setLineColor([1,1,1])
        polygon_2.setSize([.25, .25])
        # keep track of which components have finished
        DelayComponents = []
        DelayComponents.append(delay)
        DelayComponents.append(delayText)
        DelayComponents.append(polygon_2)
        for thisComponent in DelayComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Delay"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = DelayClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *delay* updates
            if t >= 0.0 and delay.status == NOT_STARTED:
                # keep track of start time/frame for later
                delay.tStart = t  # underestimates by a little under one frame
                delay.frameNStart = frameN  # exact frame index
                delay.setAutoDraw(True)
            if delay.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                delay.setAutoDraw(False)
            
            # *delayText* updates
            if (t>=0 and Prediction==True) and delayText.status == NOT_STARTED:
                # keep track of start time/frame for later
                delayText.tStart = t  # underestimates by a little under one frame
                delayText.frameNStart = frameN  # exact frame index
                delayText.setAutoDraw(True)
            if delayText.status == STARTED and t >= (delayText.tStart + 1.0):
                delayText.setAutoDraw(False)
            
            # *polygon_2* updates
            if (t>=0 and Prediction==False) and polygon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_2.tStart = t  # underestimates by a little under one frame
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.setAutoDraw(True)
            if polygon_2.status == STARTED and t >= (polygon_2.tStart + 1.0):
                polygon_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in DelayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Delay"-------
        for thisComponent in DelayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        #------Prepare to start Routine "Feedback"-------
        t = 0
        FeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        PeerPhotoFeedback.setImage(Cue)
        PeerPhotoFeedback.setSize([542,620])
        peerEval.setText(Eval)
        predictText.setText(responseMsg)
        polygon.setPos([.75, 0])
        polygon.setSize([.25, .25])
        polygon_3.setPos([-.75, 0])
        polygon_3.setSize([.25, .25])
        # keep track of which components have finished
        FeedbackComponents = []
        FeedbackComponents.append(PeerPhotoFeedback)
        FeedbackComponents.append(peerEval)
        FeedbackComponents.append(predictText)
        FeedbackComponents.append(polygon)
        FeedbackComponents.append(polygon_3)
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Feedback"-------
        if Prediction_Response.keys == "1" and Eval == "Yes":
            pins = FEEDBACK_CONACCEPT
        elif Prediction_Response.keys == "2" and Eval == "No":
            pins = FEEDBACK_CONREJECT
        elif Prediction_Response.keys == "2" and Eval == "Yes":
            pins = FEEDBACK_INCONACCEPT
        elif Prediction_Response.keys == "1" and Eval == "No":
            pins = FEEDBACK_INCONREJECT
        elif Prediction_Response.keys == None:
            pins = MISSED
        ser.writeUSB(1, pins)
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PeerPhotoFeedback* updates
            if t >= 0.0 and PeerPhotoFeedback.status == NOT_STARTED:
                # keep track of start time/frame for later
                PeerPhotoFeedback.tStart = t  # underestimates by a little under one frame
                PeerPhotoFeedback.frameNStart = frameN  # exact frame index
                PeerPhotoFeedback.setAutoDraw(True)
            if PeerPhotoFeedback.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
                PeerPhotoFeedback.setAutoDraw(False)
            
            # *peerEval* updates
            if (t>=0 and Prediction==True) and peerEval.status == NOT_STARTED:
                # keep track of start time/frame for later
                peerEval.tStart = t  # underestimates by a little under one frame
                peerEval.frameNStart = frameN  # exact frame index
                peerEval.setAutoDraw(True)
            if peerEval.status == STARTED and t >= (peerEval.tStart + 2.0):
                peerEval.setAutoDraw(False)
            
            # *predictText* updates
            if t >= 0.0 and predictText.status == NOT_STARTED:
                # keep track of start time/frame for later
                predictText.tStart = t  # underestimates by a little under one frame
                predictText.frameNStart = frameN  # exact frame index
                predictText.setAutoDraw(True)
            if predictText.status == STARTED and t >= (2.0-win.monitorFramePeriod*0.75): #most of one frame period left
                predictText.setAutoDraw(False)
            
            # *polygon* updates
            if (t>=0 and Prediction==False) and polygon.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon.tStart = t  # underestimates by a little under one frame
                polygon.frameNStart = frameN  # exact frame index
                polygon.setAutoDraw(True)
            if polygon.status == STARTED and t >= (polygon.tStart + 2.0):
                polygon.setAutoDraw(False)
            
            # *polygon_3* updates
            if (t>=0 and Prediction==False) and polygon_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_3.tStart = t  # underestimates by a little under one frame
                polygon_3.frameNStart = frameN  # exact frame index
                polygon_3.setAutoDraw(True)
            if polygon_3.status == STARTED and t >= (polygon_3.tStart + 2.0):
                polygon_3.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "Feedback"-------
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        pins=int('00000000',2) 
        ser.writeUSB(1,pins)

        #------Prepare to start Routine "Cross"-------
        t = 0
        CrossClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        fix.setText('+')
        # keep track of which components have finished
        CrossComponents = []
        CrossComponents.append(fix)
        for thisComponent in CrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "Cross"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = CrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            if t >= 0 and fix.status == NOT_STARTED:
                # keep track of start time/frame for later
                fix.tStart = t  # underestimates by a little under one frame
                fix.frameNStart = frameN  # exact frame index
                fix.setAutoDraw(True)
            if fix.status == STARTED and t >= (0 + (Jitter-win.monitorFramePeriod*0.75)): #most of one frame period left
                fix.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Cross"-------
        for thisComponent in CrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    #------Prepare to start Routine "EndRun"-------
    t = 0
    EndRunClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    #runOffsetLogged = False
    #Run.addData('runOffset', fmriClock.getTime())
    # keep track of which components have finished
    EndRunComponents = []
    for thisComponent in EndRunComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "EndRun"-------
    pins='00000000' 
    ser.writeUSB(1,int(pins,2))
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = EndRunClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndRunComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "EndRun"-------
    for thisComponent in EndRunComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'runLooper'

# reset GSR pins at the end of the task
ser.writeUSB(0,0)
ser.writeUSB(1,0)
ser.close()
win.close()
core.quit()