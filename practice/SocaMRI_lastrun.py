#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Tue Mar 12 10:51:41 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SocaMotivePractice'  # from the Builder filename that created this script
expInfo = {u'Version': u'1A', u'Subject': u'999'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s_%s' %(expInfo['Subject'], expName, expInfo['date'], expInfo['Version'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/Rejection_induction/practice/SocaMRI.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstrText = visual.TextStim(win=win, name='InstrText',
    text="Participants at other study sites rated whether they liked you based on your picture. \n\n\nDuring this task, your job is to guess whether or not each person liked you. After that, you will be shown what they said.\n\n\n\n\n\nPress 'Yes' to see a demonstration.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracticeDirections"
PracticeDirectionsClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text="First, you'll see a picture of another participant.",
    font='Arial',
    pos=[0, 0.5], height=0.07, wrapWidth=2.0, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
scalePic = visual.ImageStim(
    win=win, name='scalePic',units='pix', 
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
    depth=-2.0);
text_17 = visual.TextStim(win=win, name='text_17',
    text='Yes',
    font='Arial',
    pos=[-.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='(Your guess)',
    font='Arial',
    pos=[-0.7, -0.2], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
text_15 = visual.TextStim(win=win, name='text_15',
    text='After that, you will be shown\nwhat they said.',
    font='Arial',
    pos=[0.7, 0.5], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Yes',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-6.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='(What they said)',
    font='Arial',
    pos=[0.7, -0.2], height=0.06, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0);
text_23 = visual.TextStim(win=win, name='text_23',
    text="Do you have any questions?\n\n\n\n\n\n\n\n\n\n\n\n\n\nPress 'Yes' to continue.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0);

# Initialize components for Routine "go"
goClock = core.Clock()
text_31 = visual.TextStim(win=win, name='text_31',
    text="Now, let's try a practice round.\n\n\n\n\n\nPress 'Yes' to continue.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Cue"
CueClock = core.Clock()
peerPhotoCue = visual.ImageStim(
    win=win, name='peerPhotoCue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
allowable_keys = {
    '1': 'Yes',
    '2': 'No'
}
PredictText = visual.TextStim(win=win, name='PredictText',
    text='default text',
    font='Arial',
    pos=[-0.70, 0], height=.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
text_41 = visual.TextStim(win=win, name='text_41',
    text='(Make a guess)',
    font='Arial',
    pos=[-0.7, -0.2], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Slow"
SlowClock = core.Clock()
slowText = visual.TextStim(win=win, name='slowText',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Motvation"
MotvationClock = core.Clock()
motivePhoto = visual.ImageStim(
    win=win, name='motivePhoto',units='pix', 
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
    depth=-1.0);

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
PeerPhotoFeedback = visual.ImageStim(
    win=win, name='PeerPhotoFeedback',units='pix', 
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
    depth=-1.0);
predictText = visual.TextStim(win=win, name='predictText',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "AllInstructions"
AllInstructionsClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text="Now, let's do one last practice.\n\nThis time, you will not have directions as you go along, so make sure to begin by making a guess.\n\nIf you do not make a guess in the alotted time, you will be shown a circle for your prediction. You will not be shown what your peer said about you, and you will be shown a circle instead.\n\n\nPress 'Yes' to continue.",
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "CueMotive"
CueMotiveClock = core.Clock()
CueMotivePic = visual.ImageStim(
    win=win, name='CueMotivePic',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

PredText = visual.TextStim(win=win, name='PredText',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Motivation2"
Motivation2Clock = core.Clock()
MotiveCue = visual.ImageStim(
    win=win, name='MotiveCue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
MotiveText2 = visual.TextStim(win=win, name='MotiveText2',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
polygon = visual.Polygon(
    win=win, name='polygon',
    edges=90, size=[0.25, 0.25],
    ori=0, pos=[-0.7, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Initialize components for Routine "Feedback2"
Feedback2Clock = core.Clock()
cueFdbk = visual.ImageStim(
    win=win, name='cueFdbk',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_10 = visual.TextStim(win=win, name='text_10',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='default text',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[-.7, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_6 = visual.Polygon(
    win=win, name='polygon_6',
    edges=90, size=[1.0, 1.0],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Finished_"
Finished_Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Any questions?\n\n\n\n\nPlease let the experimenter know if you would like to try the practice again.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrContinue = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [InstrText, InstrContinue]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if t >= 0.0 and InstrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText.tStart = t
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.setAutoDraw(True)
    
    # *InstrContinue* updates
    if t >= 0.0 and InstrContinue.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrContinue.tStart = t
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

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeDirections"-------
t = 0
PracticeDirectionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
scalePic.setImage('stim/Smile_1.jpg')
understand = event.BuilderKeyResponse()
# keep track of which components have finished
PracticeDirectionsComponents = [text_3, scalePic, moreDirections, text_17, text_37, text_15, text_18, text_38, understand, text_23]
for thisComponent in PracticeDirectionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PracticeDirections"-------
while continueRoutine:
    # get current time
    t = PracticeDirectionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 5.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # *scalePic* updates
    if t >= 3.0 and scalePic.status == NOT_STARTED:
        # keep track of start time/frame for later
        scalePic.tStart = t
        scalePic.frameNStart = frameN  # exact frame index
        scalePic.setAutoDraw(True)
    
    # *moreDirections* updates
    if t >= 5 and moreDirections.status == NOT_STARTED:
        # keep track of start time/frame for later
        moreDirections.tStart = t
        moreDirections.frameNStart = frameN  # exact frame index
        moreDirections.setAutoDraw(True)
    frameRemains = 11 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if moreDirections.status == STARTED and t >= frameRemains:
        moreDirections.setAutoDraw(False)
    
    # *text_17* updates
    if t >= 9 and text_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_17.tStart = t
        text_17.frameNStart = frameN  # exact frame index
        text_17.setAutoDraw(True)
    
    # *text_37* updates
    if t >= 9 and text_37.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_37.tStart = t
        text_37.frameNStart = frameN  # exact frame index
        text_37.setAutoDraw(True)
    
    # *text_15* updates
    if t >= 11 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)
    frameRemains = 17 - win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_15.status == STARTED and t >= frameRemains:
        text_15.setAutoDraw(False)
    
    # *text_18* updates
    if t >= 14 and text_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_18.tStart = t
        text_18.frameNStart = frameN  # exact frame index
        text_18.setAutoDraw(True)
    
    # *text_38* updates
    if t >= 14 and text_38.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_38.tStart = t
        text_38.frameNStart = frameN  # exact frame index
        text_38.setAutoDraw(True)
    
    # *understand* updates
    if t >= 22 and understand.status == NOT_STARTED:
        # keep track of start time/frame for later
        understand.tStart = t
        understand.frameNStart = frameN  # exact frame index
        understand.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(understand.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if understand.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            understand.keys = theseKeys[-1]  # just the last key pressed
            understand.rt = understand.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_23* updates
    if t >= 23 and text_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_23.tStart = t
        text_23.frameNStart = frameN  # exact frame index
        text_23.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeDirectionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeDirections"-------
for thisComponent in PracticeDirectionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if understand.keys in ['', [], None]:  # No response was made
    understand.keys=None
thisExp.addData('understand.keys',understand.keys)
if understand.keys != None:  # we had a response
    thisExp.addData('understand.rt', understand.rt)
thisExp.nextEntry()
# the Routine "PracticeDirections" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "go"-------
t = 0
goClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
goComponents = [text_31, key_resp_10]
for thisComponent in goComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "go"-------
while continueRoutine:
    # get current time
    t = goClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_31* updates
    if t >= 0.0 and text_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_31.tStart = t
        text_31.frameNStart = frameN  # exact frame index
        text_31.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "go"-------
for thisComponent in goComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "go" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/ShortSocaMotivePracticeEncodeConditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    ensureResponse = data.TrialHandler(nReps=5, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ensureResponse')
    thisExp.addLoop(ensureResponse)  # add the loop to the experiment
    thisEnsureResponse = ensureResponse.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse.rgb)
    if thisEnsureResponse != None:
        for paramName in thisEnsureResponse.keys():
            exec(paramName + '= thisEnsureResponse.' + paramName)
    
    for thisEnsureResponse in ensureResponse:
        currentLoop = ensureResponse
        # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse.rgb)
        if thisEnsureResponse != None:
            for paramName in thisEnsureResponse.keys():
                exec(paramName + '= thisEnsureResponse.' + paramName)
        
        # ------Prepare to start Routine "Cue"-------
        t = 0
        CueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        peerPhotoCue.setImage(Cue)
        Prediction_Response = event.BuilderKeyResponse()
        responseMsg = ''
        # keep track of which components have finished
        CueComponents = [peerPhotoCue, Prediction_Response, PredictText, text_41]
        for thisComponent in CueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *peerPhotoCue* updates
            if t >= 0.0 and peerPhotoCue.status == NOT_STARTED:
                # keep track of start time/frame for later
                peerPhotoCue.tStart = t
                peerPhotoCue.frameNStart = frameN  # exact frame index
                peerPhotoCue.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if peerPhotoCue.status == STARTED and t >= frameRemains:
                peerPhotoCue.setAutoDraw(False)
            
            # *Prediction_Response* updates
            if t >= 0.25 and Prediction_Response.status == NOT_STARTED:
                # keep track of start time/frame for later
                Prediction_Response.tStart = t
                Prediction_Response.frameNStart = frameN  # exact frame index
                Prediction_Response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Prediction_Response.clock.reset)  # t=0 on next screen flip
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if Prediction_Response.status == STARTED and t >= frameRemains:
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
            if Prediction_Response.keys:
                responseMsg = allowable_keys[Prediction_Response.keys]
            
            # *PredictText* updates
            if t >= 0 and PredictText.status == NOT_STARTED:
                # keep track of start time/frame for later
                PredictText.tStart = t
                PredictText.frameNStart = frameN  # exact frame index
                PredictText.setAutoDraw(True)
            frameRemains = 0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if PredictText.status == STARTED and t >= frameRemains:
                PredictText.setAutoDraw(False)
            if PredictText.status == STARTED:  # only update if drawing
                PredictText.setText(responseMsg, log=False)
            
            # *text_41* updates
            if t >= 0.0 and text_41.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_41.tStart = t
                text_41.frameNStart = frameN  # exact frame index
                text_41.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_41.status == STARTED and t >= frameRemains:
                text_41.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
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
        
        # -------Ending Routine "Cue"-------
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Prediction_Response.keys in ['', [], None]:  # No response was made
            Prediction_Response.keys=None
        ensureResponse.addData('Prediction_Response.keys',Prediction_Response.keys)
        if Prediction_Response.keys != None:  # we had a response
            ensureResponse.addData('Prediction_Response.rt', Prediction_Response.rt)
        
        
        # ------Prepare to start Routine "Slow"-------
        t = 0
        SlowClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        SlowComponents = [slowText]
        for thisComponent in SlowComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Slow"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SlowClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slowText* updates
            if t >= 0.0 and slowText.status == NOT_STARTED:
                # keep track of start time/frame for later
                slowText.tStart = t
                slowText.frameNStart = frameN  # exact frame index
                slowText.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if slowText.status == STARTED and t >= frameRemains:
                slowText.setAutoDraw(False)
            if Prediction_Response.keys:
                continueRoutine=False
                ensureResponse.finished=True
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SlowComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Slow"-------
        for thisComponent in SlowComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 5 repeats of 'ensureResponse'
    
    
    # ------Prepare to start Routine "Motvation"-------
    t = 0
    MotvationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    motivePhoto.setImage(Cue)
    motiveText.setText(responseMsg)
    # keep track of which components have finished
    MotvationComponents = [motivePhoto, motiveText]
    for thisComponent in MotvationComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Motvation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = MotvationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *motivePhoto* updates
        if t >= 0.0 and motivePhoto.status == NOT_STARTED:
            # keep track of start time/frame for later
            motivePhoto.tStart = t
            motivePhoto.frameNStart = frameN  # exact frame index
            motivePhoto.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if motivePhoto.status == STARTED and t >= frameRemains:
            motivePhoto.setAutoDraw(False)
        
        # *motiveText* updates
        if t >= 0 and motiveText.status == NOT_STARTED:
            # keep track of start time/frame for later
            motiveText.tStart = t
            motiveText.frameNStart = frameN  # exact frame index
            motiveText.setAutoDraw(True)
        frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if motiveText.status == STARTED and t >= frameRemains:
            motiveText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MotvationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Motvation"-------
    for thisComponent in MotvationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    PeerPhotoFeedback.setImage(Cue)
    PeerPhotoFeedback.setSize([676,777])
    predictText.setText(responseMsg)
    # keep track of which components have finished
    FeedbackComponents = [PeerPhotoFeedback, peerEval, predictText]
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PeerPhotoFeedback* updates
        if t >= 0.0 and PeerPhotoFeedback.status == NOT_STARTED:
            # keep track of start time/frame for later
            PeerPhotoFeedback.tStart = t
            PeerPhotoFeedback.frameNStart = frameN  # exact frame index
            PeerPhotoFeedback.setAutoDraw(True)
        frameRemains = 2.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if PeerPhotoFeedback.status == STARTED and t >= frameRemains:
            PeerPhotoFeedback.setAutoDraw(False)
        
        # *peerEval* updates
        if t >= 0 and peerEval.status == NOT_STARTED:
            # keep track of start time/frame for later
            peerEval.tStart = t
            peerEval.frameNStart = frameN  # exact frame index
            peerEval.setAutoDraw(True)
        frameRemains = 0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if peerEval.status == STARTED and t >= frameRemains:
            peerEval.setAutoDraw(False)
        if peerEval.status == STARTED:  # only update if drawing
            peerEval.setText(Eval, log=False)
        
        # *predictText* updates
        if t >= 0 and predictText.status == NOT_STARTED:
            # keep track of start time/frame for later
            predictText.tStart = t
            predictText.frameNStart = frameN  # exact frame index
            predictText.setAutoDraw(True)
        frameRemains = 0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if predictText.status == STARTED and t >= frameRemains:
            predictText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
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
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Cross"-------
    t = 0
    CrossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrossComponents = [fix]
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix.status == STARTED and t >= frameRemains:
            fix.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
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
    
    # -------Ending Routine "Cross"-------
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "AllInstructions"-------
t = 0
AllInstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
AllInstructionsComponents = [text_13, key_resp_7]
for thisComponent in AllInstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "AllInstructions"-------
while continueRoutine:
    # get current time
    t = AllInstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AllInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "AllInstructions"-------
for thisComponent in AllInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "AllInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/ShortSocaMotivePracticeEncodeConditions.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4.keys():
        exec(paramName + '= thisTrial_4.' + paramName)

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4.keys():
            exec(paramName + '= thisTrial_4.' + paramName)
    
    # ------Prepare to start Routine "CueMotive"-------
    t = 0
    CueMotiveClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    CueMotivePic.setImage(Cue)
    cueResponse = event.BuilderKeyResponse()
    responseMsgMotive=''
    # keep track of which components have finished
    CueMotiveComponents = [CueMotivePic, cueResponse, PredText]
    for thisComponent in CueMotiveComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "CueMotive"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CueMotiveClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CueMotivePic* updates
        if t >= 0.0 and CueMotivePic.status == NOT_STARTED:
            # keep track of start time/frame for later
            CueMotivePic.tStart = t
            CueMotivePic.frameNStart = frameN  # exact frame index
            CueMotivePic.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CueMotivePic.status == STARTED and t >= frameRemains:
            CueMotivePic.setAutoDraw(False)
        
        # *cueResponse* updates
        if t >= 0.25 and cueResponse.status == NOT_STARTED:
            # keep track of start time/frame for later
            cueResponse.tStart = t
            cueResponse.frameNStart = frameN  # exact frame index
            cueResponse.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(cueResponse.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cueResponse.status == STARTED and t >= frameRemains:
            cueResponse.status = STOPPED
        if cueResponse.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if cueResponse.keys == []:  # then this was the first keypress
                    cueResponse.keys = theseKeys[0]  # just the first key pressed
                    cueResponse.rt = cueResponse.clock.getTime()
        if cueResponse.keys:
            responseMsgMotive = allowable_keys[cueResponse.keys]
            Prediction='True'
        else:
            Prediction='False'
        
        # *PredText* updates
        if t >= 0 and PredText.status == NOT_STARTED:
            # keep track of start time/frame for later
            PredText.tStart = t
            PredText.frameNStart = frameN  # exact frame index
            PredText.setAutoDraw(True)
        frameRemains = 0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PredText.status == STARTED and t >= frameRemains:
            PredText.setAutoDraw(False)
        if PredText.status == STARTED:  # only update if drawing
            PredText.setText(responseMsgMotive, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueMotiveComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "CueMotive"-------
    for thisComponent in CueMotiveComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if cueResponse.keys in ['', [], None]:  # No response was made
        cueResponse.keys=None
    trials_4.addData('cueResponse.keys',cueResponse.keys)
    if cueResponse.keys != None:  # we had a response
        trials_4.addData('cueResponse.rt', cueResponse.rt)
    
    
    # ------Prepare to start Routine "Motivation2"-------
    t = 0
    Motivation2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    MotiveCue.setImage(Cue)
    MotiveText2.setText(responseMsgMotive)
    # keep track of which components have finished
    Motivation2Components = [MotiveCue, MotiveText2, polygon]
    for thisComponent in Motivation2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Motivation2"-------
    while continueRoutine:
        # get current time
        t = Motivation2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MotiveCue* updates
        if t >= 0.0 and MotiveCue.status == NOT_STARTED:
            # keep track of start time/frame for later
            MotiveCue.tStart = t
            MotiveCue.frameNStart = frameN  # exact frame index
            MotiveCue.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MotiveCue.status == STARTED and t >= frameRemains:
            MotiveCue.setAutoDraw(False)
        
        # *MotiveText2* updates
        if t >= 0 and MotiveText2.status == NOT_STARTED:
            # keep track of start time/frame for later
            MotiveText2.tStart = t
            MotiveText2.frameNStart = frameN  # exact frame index
            MotiveText2.setAutoDraw(True)
        frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MotiveText2.status == STARTED and t >= frameRemains:
            MotiveText2.setAutoDraw(False)
        
        # *polygon* updates
        if (t>=0 and Prediction=='False') and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        if polygon.status == STARTED and t >= (polygon.tStart + 1.0):
            polygon.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Motivation2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Motivation2"-------
    for thisComponent in Motivation2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Motivation2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Feedback2"-------
    t = 0
    Feedback2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    cueFdbk.setImage(Cue)
    text_10.setText(responseMsgMotive)
    text_11.setText(Eval)
    polygon_3.setSize([0.25, 0.25])
    polygon_6.setPos([0.7, 0])
    polygon_6.setSize([0.25, 0.25])
    # keep track of which components have finished
    Feedback2Components = [cueFdbk, text_10, text_11, polygon_3, polygon_6]
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback2"-------
    while continueRoutine:
        # get current time
        t = Feedback2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cueFdbk* updates
        if t >= 0.0 and cueFdbk.status == NOT_STARTED:
            # keep track of start time/frame for later
            cueFdbk.tStart = t
            cueFdbk.frameNStart = frameN  # exact frame index
            cueFdbk.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if cueFdbk.status == STARTED and t >= frameRemains:
            cueFdbk.setAutoDraw(False)
        
        # *text_10* updates
        if t >= 0 and text_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_10.tStart = t
            text_10.frameNStart = frameN  # exact frame index
            text_10.setAutoDraw(True)
        frameRemains = 0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_10.status == STARTED and t >= frameRemains:
            text_10.setAutoDraw(False)
        
        # *text_11* updates
        if (t>=0 and Prediction=='True') and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        if text_11.status == STARTED and t >= (text_11.tStart + 2.0):
            text_11.setAutoDraw(False)
        
        # *polygon_3* updates
        if (t>=0 and Prediction=='False') and polygon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_3.tStart = t
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED and t >= (polygon_3.tStart + 2.0):
            polygon_3.setAutoDraw(False)
        
        # *polygon_6* updates
        if (t>=0 and Prediction=='False') and polygon_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_6.tStart = t
            polygon_6.frameNStart = frameN  # exact frame index
            polygon_6.setAutoDraw(True)
        if polygon_6.status == STARTED and t >= (polygon_6.tStart + 2.0):
            polygon_6.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback2"-------
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Feedback2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Cross"-------
    t = 0
    CrossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    CrossComponents = [fix]
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Cross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = CrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if t >= 0.0 and fix.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix.tStart = t
            fix.frameNStart = frameN  # exact frame index
            fix.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix.status == STARTED and t >= frameRemains:
            fix.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
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
    
    # -------Ending Routine "Cross"-------
    for thisComponent in CrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_4'


# ------Prepare to start Routine "Finished_"-------
t = 0
Finished_Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Finished_Components = [text_14]
for thisComponent in Finished_Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Finished_"-------
while continueRoutine:
    # get current time
    t = Finished_Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Finished_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finished_"-------
for thisComponent in Finished_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Finished_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
