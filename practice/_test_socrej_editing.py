#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Thu Oct 15 16:13:31 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.4'
expName = 'SocaMotivePractice'  # from the Builder filename that created this script
expInfo = {'Subject': '999','Version': '1A', 'Run': ' '}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['Subject'], expName, expInfo['date'], expInfo['Version'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mruiz/Documents/GitHub/Rejection_induction/practice/SocaMRI_DF_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstrText = visual.TextStim(win=win, name='InstrText',
    text="Participants at other study sites rated whether they liked you based on your picture. \n\n\nDuring this task, your job is to guess whether or not each person liked you. After that, you will be shown what they said.\n\n\n\n\n\nPress 'Yes' to see a demonstration.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
InstrContinue = keyboard.Keyboard()

# Initialize components for Routine "PracticeDirections"
PracticeDirectionsClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text="First, you'll see a picture of another participant.",
    font='Arial',
    pos=[0, 0.5], height=0.07, wrapWidth=2.0, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
scalePic = visual.ImageStim(
    win=win,
    name='scalePic', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, -75], size=[506,582],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
moreDirections = visual.TextStim(win=win, name='moreDirections',
    text="Then, you'll guess whether they\nliked you by pressing Yes or No.",
    font='Arial',
    pos=[-.7,0.5], height=0.07, wrapWidth=1.7, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Yes',
    font='Arial',
    pos=[-.7, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-3.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='(Your guess)',
    font='Arial',
    pos=[-0.7, -0.2], height=0.06, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='After that, you will be shown\nwhat they said.',
    font='Arial',
    pos=[0.7, 0.5], height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-5.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Yes',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-6.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='(What they said)',
    font='Arial',
    pos=[0.7, -0.2], height=0.06, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-7.0);
understand = keyboard.Keyboard()
text_23 = visual.TextStim(win=win, name='text_23',
    text="Do you have any questions?\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress 'Yes' to continue.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "go"
goClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text="Now, let's try a practice round.\n\n\n\n\n\nPress 'Yes' to continue.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "Cue"
CueClock = core.Clock()
peerPhotoCue = visual.ImageStim(
    win=win,
    name='peerPhotoCue', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Prediction_Response = keyboard.Keyboard()
allowable_keys = {
    '1': 'Yes',
    '2': 'No'
}
PredictText = visual.TextStim(win=win, name='PredictText',
    text='default text',
    font='Arial',
    pos=[-0.70, 0], height=.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-3.0);
text_41 = visual.TextStim(win=win, name='text_41',
    text='(Make a guess)',
    font='Arial',
    pos=[-0.7, -0.2], height=0.07, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Slow"
SlowClock = core.Clock()
slowText = visual.TextStim(win=win, name='slowText',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Motvation"
MotvationClock = core.Clock()
motivePhoto = visual.ImageStim(
    win=win,
    name='motivePhoto', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
motiveText = visual.TextStim(win=win, name='motiveText',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
PeerPhotoFeedback = visual.ImageStim(
    win=win,
    name='PeerPhotoFeedback', units='pix',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
peerEval = visual.TextStim(win=win, name='peerEval',
    text='default text',
    font='Arial',
    pos=[.70, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-1.0);
predictText = visual.TextStim(win=win, name='predictText',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Finished_"
prac_endClock = core.Clock()
prac_end_msg = visual.TextStim(win=win, name='prac_end_msg',
    text='Any questions?\n\n\n\n\nPlease let the experimenter know if you would like to try the practice again.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
prac_endKeyboard = keyboard.Keyboard();
#Initialize components for Routine "end" 

Exp_Finished_Clock = core.Clock()
endmsg = visual.TextStim(win=win, name='endmsg',
    text="Thank you for participating! \n\n\n\n\nPlease press 'space' to exit.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
endKeyboard = keyboard.Keyboard();
    

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
InstrContinue.keys = []
InstrContinue.rt = []
_InstrContinue_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstrText, InstrContinue]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *InstrText* updates
    if InstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.tStart = t  # local t and not account for scr refresh
        InstrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrText, 'tStartRefresh')  # time at next scr refresh
        InstrText.setAutoDraw(True)

    # *InstrContinue* updates
    waitOnFlip = False
    if InstrContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstrContinue.frameNStart = frameN  # exact frame index
        InstrContinue.tStart = t  # local t and not account for scr refresh
        InstrContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstrContinue, 'tStartRefresh')  # time at next scr refresh
        InstrContinue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(InstrContinue.clock.reset)  # t=0 on next screen flip
    if InstrContinue.status == STARTED and not waitOnFlip:
        theseKeys = InstrContinue.getKeys(keyList=['1', '2'], waitRelease=False)
        _InstrContinue_allKeys.extend(theseKeys)
        if len(_InstrContinue_allKeys):
            InstrContinue.keys = _InstrContinue_allKeys[-1].name  # just the last key pressed
            InstrContinue.rt = _InstrContinue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstrText.started', InstrText.tStartRefresh)
thisExp.addData('InstrText.stopped', InstrText.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeDirections"-------
continueRoutine = True
# update component parameters for each repeat
scalePic.setImage('stim/Smile_1.jpg')
understand.keys = []
understand.rt = []
_understand_allKeys = []
# keep track of which components have finished
PracticeDirectionsComponents = [text_3, scalePic, moreDirections, text_17, text_37, text_15, text_18, text_38, understand, text_23]
for thisComponent in PracticeDirectionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeDirectionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeDirections"-------
while continueRoutine:
    # get current time
    t = PracticeDirectionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeDirectionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)

    # *scalePic* updates
    if scalePic.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        scalePic.frameNStart = frameN  # exact frame index
        scalePic.tStart = t  # local t and not account for scr refresh
        scalePic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scalePic, 'tStartRefresh')  # time at next scr refresh
        scalePic.setAutoDraw(True)

    # *moreDirections* updates
    if moreDirections.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        moreDirections.frameNStart = frameN  # exact frame index
        moreDirections.tStart = t  # local t and not account for scr refresh
        moreDirections.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(moreDirections, 'tStartRefresh')  # time at next scr refresh
        moreDirections.setAutoDraw(True)
    if moreDirections.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 11-frameTolerance:
            # keep track of stop time/frame for later
            moreDirections.tStop = t  # not accounting for scr refresh
            moreDirections.frameNStop = frameN  # exact frame index
            win.timeOnFlip(moreDirections, 'tStopRefresh')  # time at next scr refresh
            moreDirections.setAutoDraw(False)

    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 9-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)

    # *text_37* updates
    if text_37.status == NOT_STARTED and tThisFlip >= 9-frameTolerance:
        # keep track of start time/frame for later
        text_37.frameNStart = frameN  # exact frame index
        text_37.tStart = t  # local t and not account for scr refresh
        text_37.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
        text_37.setAutoDraw(True)

    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 11-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    if text_15.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 17-frameTolerance:
            # keep track of stop time/frame for later
            text_15.tStop = t  # not accounting for scr refresh
            text_15.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
            text_15.setAutoDraw(False)

    # *text_18* updates
    if text_18.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)

    # *text_38* updates
    if text_38.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
        # keep track of start time/frame for later
        text_38.frameNStart = frameN  # exact frame index
        text_38.tStart = t  # local t and not account for scr refresh
        text_38.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
        text_38.setAutoDraw(True)

    # *understand* updates
    waitOnFlip = False
    if understand.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        understand.frameNStart = frameN  # exact frame index
        understand.tStart = t  # local t and not account for scr refresh
        understand.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(understand, 'tStartRefresh')  # time at next scr refresh
        understand.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(understand.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(understand.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if understand.status == STARTED and not waitOnFlip:
        theseKeys = understand.getKeys(keyList=['1', '2'], waitRelease=False)
        _understand_allKeys.extend(theseKeys)
        if len(_understand_allKeys):
            understand.keys = _understand_allKeys[-1].name  # just the last key pressed
            understand.rt = _understand_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # *text_23* updates
    if text_23.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        text_23.frameNStart = frameN  # exact frame index
        text_23.tStart = t  # local t and not account for scr refresh
        text_23.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeDirectionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeDirections"-------
for thisComponent in PracticeDirectionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('scalePic.started', scalePic.tStartRefresh)
thisExp.addData('scalePic.stopped', scalePic.tStopRefresh)
thisExp.addData('moreDirections.started', moreDirections.tStartRefresh)
thisExp.addData('moreDirections.stopped', moreDirections.tStopRefresh)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
thisExp.addData('text_37.started', text_37.tStartRefresh)
thisExp.addData('text_37.stopped', text_37.tStopRefresh)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
thisExp.addData('text_38.started', text_38.tStartRefresh)
thisExp.addData('text_38.stopped', text_38.tStopRefresh)
# check responses
if understand.keys in ['', [], None]:  # No response was made
    understand.keys = None
thisExp.addData('understand.keys',understand.keys)
if understand.keys != None:  # we had a response
    thisExp.addData('understand.rt', understand.rt)
thisExp.addData('understand.started', understand.tStartRefresh)
thisExp.addData('understand.stopped', understand.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)
# the Routine "PracticeDirections" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "go"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
goComponents = [text_31, key_resp_10]
for thisComponent in goComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "go"-------
while continueRoutine:
    # get current time
    t = goClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_31* updates
    if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_31.frameNStart = frameN  # exact frame index
        text_31.tStart = t  # local t and not account for scr refresh
        text_31.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)

    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['1', '2'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "go"-------
for thisComponent in goComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "go" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/Final_ShortSocaMotivePracticeEncodeConditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # set up handler to look after randomisation of conditions etc
    ensureResponse = data.TrialHandler(nReps=5, method='sequential',
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ensureResponse')
    thisExp.addLoop(ensureResponse)  # add the loop to the experiment
    thisEnsureResponse = ensureResponse.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse.rgb)
    if thisEnsureResponse != None:
        for paramName in thisEnsureResponse:
            exec('{} = thisEnsureResponse[paramName]'.format(paramName))

    for thisEnsureResponse in ensureResponse:
        currentLoop = ensureResponse
        # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse.rgb)
        if thisEnsureResponse != None:
            for paramName in thisEnsureResponse:
                exec('{} = thisEnsureResponse[paramName]'.format(paramName))

        # ------Prepare to start Routine "Cue"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        peerPhotoCue.setImage(Cue)
        Prediction_Response.keys = []
        Prediction_Response.rt = []
        _Prediction_Response_allKeys = []
        responseMsg = ''
        # keep track of which components have finished
        CueComponents = [peerPhotoCue, Prediction_Response, PredictText, text_41]
        for thisComponent in CueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        CueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CueClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=CueClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *peerPhotoCue* updates
            if peerPhotoCue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                peerPhotoCue.frameNStart = frameN  # exact frame index
                peerPhotoCue.tStart = t  # local t and not account for scr refresh
                peerPhotoCue.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(peerPhotoCue, 'tStartRefresh')  # time at next scr refresh
                peerPhotoCue.setAutoDraw(True)
            if peerPhotoCue.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > peerPhotoCue.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    peerPhotoCue.tStop = t  # not accounting for scr refresh
                    peerPhotoCue.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(peerPhotoCue, 'tStopRefresh')  # time at next scr refresh
                    peerPhotoCue.setAutoDraw(False)

            # *Prediction_Response* updates
            waitOnFlip = False
            if Prediction_Response.status == NOT_STARTED and tThisFlip >= 0.25-frameTolerance:
                # keep track of start time/frame for later
                Prediction_Response.frameNStart = frameN  # exact frame index
                Prediction_Response.tStart = t  # local t and not account for scr refresh
                Prediction_Response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Prediction_Response, 'tStartRefresh')  # time at next scr refresh
                Prediction_Response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Prediction_Response.clock.reset)  # t=0 on next screen flip
            if Prediction_Response.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Prediction_Response.tStop = t  # not accounting for scr refresh
                    Prediction_Response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Prediction_Response, 'tStopRefresh')  # time at next scr refresh
                    Prediction_Response.status = FINISHED
            if Prediction_Response.status == STARTED and not waitOnFlip:
                theseKeys = Prediction_Response.getKeys(keyList=['1', '2'], waitRelease=False)
                _Prediction_Response_allKeys.extend(theseKeys)
                if len(_Prediction_Response_allKeys):
                    Prediction_Response.keys = _Prediction_Response_allKeys[0].name  # just the first key pressed
                    Prediction_Response.rt = _Prediction_Response_allKeys[0].rt
            if Prediction_Response.keys:
                responseMsg = allowable_keys[Prediction_Response.keys]

            # *PredictText* updates
            if PredictText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                PredictText.frameNStart = frameN  # exact frame index
                PredictText.tStart = t  # local t and not account for scr refresh
                PredictText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PredictText, 'tStartRefresh')  # time at next scr refresh
                PredictText.setAutoDraw(True)
            if PredictText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PredictText.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    PredictText.tStop = t  # not accounting for scr refresh
                    PredictText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PredictText, 'tStopRefresh')  # time at next scr refresh
                    PredictText.setAutoDraw(False)
            if PredictText.status == STARTED:  # only update if drawing
                PredictText.setText(responseMsg, log=False)

            # *text_41* updates
            if text_41.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_41.frameNStart = frameN  # exact frame index
                text_41.tStart = t  # local t and not account for scr refresh
                text_41.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
                text_41.setAutoDraw(True)
            if text_41.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_41.tStartRefresh + 3.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_41.tStop = t  # not accounting for scr refresh
                    text_41.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_41, 'tStopRefresh')  # time at next scr refresh
                    text_41.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Cue"-------
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ensureResponse.addData('peerPhotoCue.started', peerPhotoCue.tStartRefresh)
        ensureResponse.addData('peerPhotoCue.stopped', peerPhotoCue.tStopRefresh)
        # check responses
        if Prediction_Response.keys in ['', [], None]:  # No response was made
            Prediction_Response.keys = None
        ensureResponse.addData('Prediction_Response.keys',Prediction_Response.keys)
        if Prediction_Response.keys != None:  # we had a response
            ensureResponse.addData('Prediction_Response.rt', Prediction_Response.rt)
        ensureResponse.addData('Prediction_Response.started', Prediction_Response.tStartRefresh)
        ensureResponse.addData('Prediction_Response.stopped', Prediction_Response.tStopRefresh)
        ensureResponse.addData('PredictText.started', PredictText.tStartRefresh)
        ensureResponse.addData('PredictText.stopped', PredictText.tStopRefresh)
        ensureResponse.addData('text_41.started', text_41.tStartRefresh)
        ensureResponse.addData('text_41.stopped', text_41.tStopRefresh)

        # ------Prepare to start Routine "Slow"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        SlowComponents = [slowText]
        for thisComponent in SlowComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        SlowClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1

        # -------Run Routine "Slow"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SlowClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=SlowClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *slowText* updates
            if slowText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slowText.frameNStart = frameN  # exact frame index
                slowText.tStart = t  # local t and not account for scr refresh
                slowText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slowText, 'tStartRefresh')  # time at next scr refresh
                slowText.setAutoDraw(True)
            if slowText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > slowText.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    slowText.tStop = t  # not accounting for scr refresh
                    slowText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(slowText, 'tStopRefresh')  # time at next scr refresh
                    slowText.setAutoDraw(False)
            if Prediction_Response.keys:
                continueRoutine=False
                ensureResponse.finished=True

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SlowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "Slow"-------
        for thisComponent in SlowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ensureResponse.addData('slowText.started', slowText.tStartRefresh)
        ensureResponse.addData('slowText.stopped', slowText.tStopRefresh)
        thisExp.nextEntry()

    # completed 5 repeats of 'ensureResponse'


    # ------Prepare to start Routine "Motvation"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    motivePhoto.setImage(Cue)
    motiveText.setText(responseMsg)
    # keep track of which components have finished
    MotvationComponents = [motivePhoto, motiveText]
    for thisComponent in MotvationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MotvationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Motvation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MotvationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MotvationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *motivePhoto* updates
        if motivePhoto.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            motivePhoto.frameNStart = frameN  # exact frame index
            motivePhoto.tStart = t  # local t and not account for scr refresh
            motivePhoto.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(motivePhoto, 'tStartRefresh')  # time at next scr refresh
            motivePhoto.setAutoDraw(True)
        if motivePhoto.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > motivePhoto.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                motivePhoto.tStop = t  # not accounting for scr refresh
                motivePhoto.frameNStop = frameN  # exact frame index
                win.timeOnFlip(motivePhoto, 'tStopRefresh')  # time at next scr refresh
                motivePhoto.setAutoDraw(False)

        # *motiveText* updates
        if motiveText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            motiveText.frameNStart = frameN  # exact frame index
            motiveText.tStart = t  # local t and not account for scr refresh
            motiveText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(motiveText, 'tStartRefresh')  # time at next scr refresh
            motiveText.setAutoDraw(True)
        if motiveText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > motiveText.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                motiveText.tStop = t  # not accounting for scr refresh
                motiveText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(motiveText, 'tStopRefresh')  # time at next scr refresh
                motiveText.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MotvationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Motvation"-------
    for thisComponent in MotvationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('motivePhoto.started', motivePhoto.tStartRefresh)
    trials.addData('motivePhoto.stopped', motivePhoto.tStopRefresh)
    trials.addData('motiveText.started', motiveText.tStartRefresh)
    trials.addData('motiveText.stopped', motiveText.tStopRefresh)

    # ------Prepare to start Routine "Feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    PeerPhotoFeedback.setSize([676,777])
    PeerPhotoFeedback.setImage(Cue)
    predictText.setText(responseMsg)
    # keep track of which components have finished
    FeedbackComponents = [PeerPhotoFeedback, peerEval, predictText]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *PeerPhotoFeedback* updates
        if PeerPhotoFeedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PeerPhotoFeedback.frameNStart = frameN  # exact frame index
            PeerPhotoFeedback.tStart = t  # local t and not account for scr refresh
            PeerPhotoFeedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PeerPhotoFeedback, 'tStartRefresh')  # time at next scr refresh
            PeerPhotoFeedback.setAutoDraw(True)
        if PeerPhotoFeedback.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 2.0-frameTolerance:
                # keep track of stop time/frame for later
                PeerPhotoFeedback.tStop = t  # not accounting for scr refresh
                PeerPhotoFeedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PeerPhotoFeedback, 'tStopRefresh')  # time at next scr refresh
                PeerPhotoFeedback.setAutoDraw(False)

        # *peerEval* updates
        if peerEval.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            peerEval.frameNStart = frameN  # exact frame index
            peerEval.tStart = t  # local t and not account for scr refresh
            peerEval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(peerEval, 'tStartRefresh')  # time at next scr refresh
            peerEval.setAutoDraw(True)
        if peerEval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > peerEval.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                peerEval.tStop = t  # not accounting for scr refresh
                peerEval.frameNStop = frameN  # exact frame index
                win.timeOnFlip(peerEval, 'tStopRefresh')  # time at next scr refresh
                peerEval.setAutoDraw(False)
        if peerEval.status == STARTED:  # only update if drawing
            peerEval.setText(Eval, log=False)

        # *predictText* updates
        if predictText.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            predictText.frameNStart = frameN  # exact frame index
            predictText.tStart = t  # local t and not account for scr refresh
            predictText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(predictText, 'tStartRefresh')  # time at next scr refresh
            predictText.setAutoDraw(True)
        if predictText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > predictText.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                predictText.tStop = t  # not accounting for scr refresh
                predictText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(predictText, 'tStopRefresh')  # time at next scr refresh
                predictText.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('PeerPhotoFeedback.started', PeerPhotoFeedback.tStartRefresh)
    trials.addData('PeerPhotoFeedback.stopped', PeerPhotoFeedback.tStopRefresh)
    trials.addData('peerEval.started', peerEval.tStartRefresh)
    trials.addData('peerEval.stopped', peerEval.tStopRefresh)
    trials.addData('predictText.started', predictText.tStartRefresh)
    trials.addData('predictText.stopped', predictText.tStopRefresh)

    # ------Prepare to start Routine "Cross"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrossComponents = [fix]
    for thisComponent in CrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "Cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Cross"-------
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix.started', fix.tStartRefresh)
    trials.addData('fix.stopped', fix.tStopRefresh)
    thisExp.nextEntry()

# completed 1 repeats of 'trials'


# completed 0 repeats of 'trials_4'


# ------Prepare to start Routine "Finished_"-------
continueRoutine = True
# update component parameters for each repeat
prac_endKeyboard.keys = []
prac_endKeyboard.rt = []
_prac_endKeyboard_allKeys = []
# keep track of which components have finished
Finished_Components = [prac_end_msg]
for thisComponent in Finished_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Finished_"-------
while continueRoutine:
    # get current time
    t = prac_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *prac_end_msg* updates
    if prac_end_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_end_msg.frameNStart = frameN  # exact frame index
        prac_end_msg.tStart = t  # local t and not account for scr refresh
        prac_end_msg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_end_msg, 'tStartRefresh')  # time at next scr refresh
        prac_end_msg.setAutoDraw(True)
# *prac_endKeyboard* updates
    waitOnFlip = False
    if prac_endKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_endKeyboard.frameNStart = frameN  # exact frame index
        prac_endKeyboard.tStart = t  # local t and not account for scr refresh
        prac_endKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_endKeyboard, 'tStartRefresh')  # time at next scr refresh
        prac_endKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prac_endKeyboard.clock.reset)  # t=0 on next screen flip
    if prac_endKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = prac_endKeyboard.getKeys(keyList=['1', '2'], waitRelease=False)
        _prac_endKeyboard_allKeys.extend(theseKeys)
        if len(_prac_endKeyboard_allKeys):
            prac_endKeyboard.keys = _prac_endKeyboard_allKeys[-1].name  # just the last key pressed
            prac_endKeyboard.rt = _prac_endKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Finished_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finished_"-------
for thisComponent in Finished_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_end_msg.started', prac_end_msg.tStartRefresh)
thisExp.addData('prac_end_msg.stopped', prac_end_msg.tStopRefresh)
# the Routine "Finished_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# -------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endKeyboard.keys = []
endKeyboard.rt = []
_endKeyboard_allKeys = []
# keep track of which components have finished
endComponents = [endmsg, endKeyboard]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1



# -------Run Routine "end"-------

while continueRoutine:
    # get current time
    t = Exp_Finished_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Exp_Finished_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endmsg* updates
    if endmsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endmsg.frameNStart = frameN  # exact frame index
        endmsg.tStart = t  # local t and not account for scr refresh
        endmsg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endmsg, 'tStartRefresh')  # time at next scr refresh
        endmsg.setAutoDraw(True)
    if endmsg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endmsg.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            endmsg.tStop = t  # not accounting for scr refresh
            endmsg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endmsg, 'tStopRefresh')  # time at next scr refresh
            endmsg.setAutoDraw(False)
    
    # *endKeyboard* updates
    waitOnFlip = False
    if endKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endKeyboard.frameNStart = frameN  # exact frame index
        endKeyboard.tStart = t  # local t and not account for scr refresh
        endKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endKeyboard, 'tStartRefresh')  # time at next scr refresh
        endKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = endKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _endKeyboard_allKeys.extend(theseKeys)
        if len(_endKeyboard_allKeys):
            endKeyboard.keys = _endKeyboard_allKeys[-1].name  # just the last key pressed
            endKeyboard.rt = _endKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endmsg.started', endmsg.tStartRefresh)
thisExp.addData('endmsg.stopped', endmsg.tStopRefresh)
# check responses
if endKeyboard.keys in ['', [], None]:  # No response was made
    endKeyboard.keys = None
thisExp.addData('endKeyboard.keys',endKeyboard.keys)
if endKeyboard.keys != None:  # we had a response
    thisExp.addData('endKeyboard.rt', endKeyboard.rt)
thisExp.addData('endKeyboard.started', endKeyboard.tStartRefresh)
thisExp.addData('endKeyboard.stopped', endKeyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

