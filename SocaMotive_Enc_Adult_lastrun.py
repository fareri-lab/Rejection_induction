#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.03),
    on Thu Feb  7 16:54:12 2019
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
expName = 'SocaMotiveAdult_Encoding'  # from the Builder filename that created this script
expInfo = {u'Version': u'1A', u'Subject': u'SocaME999'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['Subject'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/dfareri/Dropbox/Dominic/Github/fareri-lab/Rejection/SocaMotive_Enc_Adult.psyexp',
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
    text="Welcome to the First Impressions Task!\n\nParticipants at other study sites rated whether they liked you based on your picture. \n\nDuring this task, your job is to guess whether or not the other person liked you. After that, you will be shown whether they actually liked you. Then you must press any button to confirm you've seen what they said.\n\n\n\n\nPress either key to begin.",
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.6, ori=0, 
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

# Initialize components for Routine "Slow"
SlowClock = core.Clock()
slowText = visual.TextStim(win=win, name='slowText',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Delay"
DelayClock = core.Clock()
delay = visual.ImageStim(
    win=win, name='delay',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
delayText = visual.TextStim(win=win, name='delayText',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.2, wrapWidth=None, ori=0, 
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
    depth=-2.0);
predictText = visual.TextStim(win=win, name='predictText',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "RunDir"
RunDirClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You have completed Run 1.\n\nYou are free to take a break!\n\n\n\n\nIf you are ready to proceed to the next run, please press either key.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Cue2"
Cue2Clock = core.Clock()
peerPhotoCue2 = visual.ImageStim(
    win=win, name='peerPhotoCue2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

text_3 = visual.TextStim(win=win, name='text_3',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Slow2"
Slow2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Delay2"
Delay2Clock = core.Clock()
delayCue = visual.ImageStim(
    win=win, name='delayCue',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_7 = visual.TextStim(win=win, name='text_7',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Feedback2"
Feedback2Clock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='default text',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "RunDir2"
RunDir2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You have completed Run 2.\n\nYou are free to take a break!\n\n\n\n\nIf you are ready to proceed to the next run, please press either key.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Cue3"
Cue3Clock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Slow3"
Slow3Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Delay3"
Delay3Clock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_11 = visual.TextStim(win=win, name='text_11',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Feedback3"
Feedback3Clock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_12 = visual.TextStim(win=win, name='text_12',
    text='default text',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_13 = visual.TextStim(win=win, name='text_13',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "RunDir3"
RunDir3Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='You have completed Run 3.\n\nYou are free to take a break!\n\n\n\n\nIf you are ready to proceed to the last run, please press either key.',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=1.7, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Cue4"
Cue4Clock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Slow4"
Slow4Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Too Slow!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);


# Initialize components for Routine "Delay4"
Delay4Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win, name='image_6',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_16 = visual.TextStim(win=win, name='text_16',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Feedback4"
Feedback4Clock = core.Clock()
image_7 = visual.ImageStim(
    win=win, name='image_7',units='pix', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[676,777],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
text_17 = visual.TextStim(win=win, name='text_17',
    text='default text',
    font='Arial',
    pos=[0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='default text',
    font='Arial',
    pos=[-0.7, 0], height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);

# Initialize components for Routine "Cross"
CrossClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
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

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(_thisDir + os.sep + 'conditions/SocaMotiveConditions_Encode_Version%s_Run1.xlsx' %(expInfo['Version'])),
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
    ensureResponse = data.TrialHandler(nReps=3, method='sequential', 
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
        CueComponents = [peerPhotoCue, Prediction_Response, PredictText]
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
            if t >= 0.5 and Prediction_Response.status == NOT_STARTED:
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
            if t >= .5 and PredictText.status == NOT_STARTED:
                # keep track of start time/frame for later
                PredictText.tStart = t
                PredictText.frameNStart = frameN  # exact frame index
                PredictText.setAutoDraw(True)
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if PredictText.status == STARTED and t >= frameRemains:
                PredictText.setAutoDraw(False)
            if PredictText.status == STARTED:  # only update if drawing
                PredictText.setText(responseMsg, log=False)
            
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
        routineTimer.add(1.500000)
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
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
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
        
    # completed 3 repeats of 'ensureResponse'
    
    
    # ------Prepare to start Routine "Delay"-------
    t = 0
    DelayClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    delay.setImage(Cue)
    delay.setSize([676,777])
    delayText.setText(responseMsg)
    delayText.setPos([-0.7, 0])
    # keep track of which components have finished
    DelayComponents = [delay, delayText]
    for thisComponent in DelayComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Delay"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = DelayClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *delay* updates
        if t >= 0.0 and delay.status == NOT_STARTED:
            # keep track of start time/frame for later
            delay.tStart = t
            delay.frameNStart = frameN  # exact frame index
            delay.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if delay.status == STARTED and t >= frameRemains:
            delay.setAutoDraw(False)
        
        # *delayText* updates
        if t >= 0.0 and delayText.status == NOT_STARTED:
            # keep track of start time/frame for later
            delayText.tStart = t
            delayText.frameNStart = frameN  # exact frame index
            delayText.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if delayText.status == STARTED and t >= frameRemains:
            delayText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
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
    
    # -------Ending Routine "Delay"-------
    for thisComponent in DelayComponents:
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
    Run1EvalRT = event.BuilderKeyResponse()
    peerEval.setText(Eval)
    predictText.setText(responseMsg)
    # keep track of which components have finished
    FeedbackComponents = [PeerPhotoFeedback, Run1EvalRT, peerEval, predictText]
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
        
        # *Run1EvalRT* updates
        if t >= 0.0 and Run1EvalRT.status == NOT_STARTED:
            # keep track of start time/frame for later
            Run1EvalRT.tStart = t
            Run1EvalRT.frameNStart = frameN  # exact frame index
            Run1EvalRT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Run1EvalRT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if Run1EvalRT.status == STARTED and t >= frameRemains:
            Run1EvalRT.status = STOPPED
        if Run1EvalRT.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if Run1EvalRT.keys == []:  # then this was the first keypress
                    Run1EvalRT.keys = theseKeys[0]  # just the first key pressed
                    Run1EvalRT.rt = Run1EvalRT.clock.getTime()
        
        # *peerEval* updates
        if t >= 0 and peerEval.status == NOT_STARTED:
            # keep track of start time/frame for later
            peerEval.tStart = t
            peerEval.frameNStart = frameN  # exact frame index
            peerEval.setAutoDraw(True)
        frameRemains = 0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if peerEval.status == STARTED and t >= frameRemains:
            peerEval.setAutoDraw(False)
        
        # *predictText* updates
        if t >= 0.0 and predictText.status == NOT_STARTED:
            # keep track of start time/frame for later
            predictText.tStart = t
            predictText.frameNStart = frameN  # exact frame index
            predictText.setAutoDraw(True)
        frameRemains = 2.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
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
    # check responses
    if Run1EvalRT.keys in ['', [], None]:  # No response was made
        Run1EvalRT.keys=None
    trials.addData('Run1EvalRT.keys',Run1EvalRT.keys)
    if Run1EvalRT.keys != None:  # we had a response
        trials.addData('Run1EvalRT.rt', Run1EvalRT.rt)
    
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


# ------Prepare to start Routine "RunDir"-------
t = 0
RunDirClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
RunDirComponents = [text, key_resp_2]
for thisComponent in RunDirComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "RunDir"-------
while continueRoutine:
    # get current time
    t = RunDirClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RunDirComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RunDir"-------
for thisComponent in RunDirComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "RunDir" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(_thisDir + os.sep + 'conditions/SocaMotiveConditions_Encode_Version%s_Run2.xlsx' %(expInfo['Version'])),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    ensureResponse2 = data.TrialHandler(nReps=3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ensureResponse2')
    thisExp.addLoop(ensureResponse2)  # add the loop to the experiment
    thisEnsureResponse2 = ensureResponse2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse2.rgb)
    if thisEnsureResponse2 != None:
        for paramName in thisEnsureResponse2.keys():
            exec(paramName + '= thisEnsureResponse2.' + paramName)
    
    for thisEnsureResponse2 in ensureResponse2:
        currentLoop = ensureResponse2
        # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse2.rgb)
        if thisEnsureResponse2 != None:
            for paramName in thisEnsureResponse2.keys():
                exec(paramName + '= thisEnsureResponse2.' + paramName)
        
        # ------Prepare to start Routine "Cue2"-------
        t = 0
        Cue2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        peerPhotoCue2.setImage(Cue)
        Prediction_Response2 = event.BuilderKeyResponse()
        responseMsg = ''
        # keep track of which components have finished
        Cue2Components = [peerPhotoCue2, Prediction_Response2, text_3]
        for thisComponent in Cue2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Cue2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Cue2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *peerPhotoCue2* updates
            if t >= 0.0 and peerPhotoCue2.status == NOT_STARTED:
                # keep track of start time/frame for later
                peerPhotoCue2.tStart = t
                peerPhotoCue2.frameNStart = frameN  # exact frame index
                peerPhotoCue2.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if peerPhotoCue2.status == STARTED and t >= frameRemains:
                peerPhotoCue2.setAutoDraw(False)
            
            # *Prediction_Response2* updates
            if t >= 0.5 and Prediction_Response2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Prediction_Response2.tStart = t
                Prediction_Response2.frameNStart = frameN  # exact frame index
                Prediction_Response2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Prediction_Response2.clock.reset)  # t=0 on next screen flip
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if Prediction_Response2.status == STARTED and t >= frameRemains:
                Prediction_Response2.status = STOPPED
            if Prediction_Response2.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if Prediction_Response2.keys == []:  # then this was the first keypress
                        Prediction_Response2.keys = theseKeys[0]  # just the first key pressed
                        Prediction_Response2.rt = Prediction_Response2.clock.getTime()
            if Prediction_Response2.keys:
                responseMsg = allowable_keys[Prediction_Response2.keys]
            
            # *text_3* updates
            if t >= 0.5 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_3.status == STARTED and t >= frameRemains:
                text_3.setAutoDraw(False)
            if text_3.status == STARTED:  # only update if drawing
                text_3.setText(responseMsg, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Cue2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Cue2"-------
        for thisComponent in Cue2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Prediction_Response2.keys in ['', [], None]:  # No response was made
            Prediction_Response2.keys=None
        ensureResponse2.addData('Prediction_Response2.keys',Prediction_Response2.keys)
        if Prediction_Response2.keys != None:  # we had a response
            ensureResponse2.addData('Prediction_Response2.rt', Prediction_Response2.rt)
        
        
        # ------Prepare to start Routine "Slow2"-------
        t = 0
        Slow2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        Slow2Components = [text_6]
        for thisComponent in Slow2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Slow2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Slow2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_6* updates
            if t >= 0.0 and text_6.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_6.tStart = t
                text_6.frameNStart = frameN  # exact frame index
                text_6.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_6.status == STARTED and t >= frameRemains:
                text_6.setAutoDraw(False)
            if Prediction_Response2.keys:
                continueRoutine=False
                ensureResponse2.finished=True
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Slow2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Slow2"-------
        for thisComponent in Slow2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 3 repeats of 'ensureResponse2'
    
    
    # ------Prepare to start Routine "Delay2"-------
    t = 0
    Delay2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    delayCue.setImage(Cue)
    text_7.setText(responseMsg)
    # keep track of which components have finished
    Delay2Components = [delayCue, text_7]
    for thisComponent in Delay2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Delay2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Delay2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *delayCue* updates
        if t >= 0.0 and delayCue.status == NOT_STARTED:
            # keep track of start time/frame for later
            delayCue.tStart = t
            delayCue.frameNStart = frameN  # exact frame index
            delayCue.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if delayCue.status == STARTED and t >= frameRemains:
            delayCue.setAutoDraw(False)
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Delay2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Delay2"-------
    for thisComponent in Delay2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Feedback2"-------
    t = 0
    Feedback2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    image.setImage(Cue)
    Run2EvalRT = event.BuilderKeyResponse()
    text_8.setText(Eval)
    text_9.setText(responseMsg)
    # keep track of which components have finished
    Feedback2Components = [image, Run2EvalRT, text_8, text_9]
    for thisComponent in Feedback2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *Run2EvalRT* updates
        if t >= 0.0 and Run2EvalRT.status == NOT_STARTED:
            # keep track of start time/frame for later
            Run2EvalRT.tStart = t
            Run2EvalRT.frameNStart = frameN  # exact frame index
            Run2EvalRT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Run2EvalRT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Run2EvalRT.status == STARTED and t >= frameRemains:
            Run2EvalRT.status = STOPPED
        if Run2EvalRT.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Run2EvalRT.keys = theseKeys[-1]  # just the last key pressed
                Run2EvalRT.rt = Run2EvalRT.clock.getTime()
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_8.status == STARTED and t >= frameRemains:
            text_8.setAutoDraw(False)
        
        # *text_9* updates
        if t >= 0.0 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_9.status == STARTED and t >= frameRemains:
            text_9.setAutoDraw(False)
        
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
    # check responses
    if Run2EvalRT.keys in ['', [], None]:  # No response was made
        Run2EvalRT.keys=None
    trials_2.addData('Run2EvalRT.keys',Run2EvalRT.keys)
    if Run2EvalRT.keys != None:  # we had a response
        trials_2.addData('Run2EvalRT.rt', Run2EvalRT.rt)
    
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
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "RunDir2"-------
t = 0
RunDir2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
RunDir2Components = [text_2, key_resp_3]
for thisComponent in RunDir2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "RunDir2"-------
while continueRoutine:
    # get current time
    t = RunDir2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RunDir2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RunDir2"-------
for thisComponent in RunDir2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "RunDir2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(_thisDir + os.sep + 'conditions/SocaMotiveConditions_Encode_Version%s_Run3.xlsx' %(expInfo['Version'])),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    ensureResponse3 = data.TrialHandler(nReps=3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ensureResponse3')
    thisExp.addLoop(ensureResponse3)  # add the loop to the experiment
    thisEnsureResponse3 = ensureResponse3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse3.rgb)
    if thisEnsureResponse3 != None:
        for paramName in thisEnsureResponse3.keys():
            exec(paramName + '= thisEnsureResponse3.' + paramName)
    
    for thisEnsureResponse3 in ensureResponse3:
        currentLoop = ensureResponse3
        # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse3.rgb)
        if thisEnsureResponse3 != None:
            for paramName in thisEnsureResponse3.keys():
                exec(paramName + '= thisEnsureResponse3.' + paramName)
        
        # ------Prepare to start Routine "Cue3"-------
        t = 0
        Cue3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        image_2.setImage(Cue)
        Prediction_Response3 = event.BuilderKeyResponse()
        responseMsg=''
        # keep track of which components have finished
        Cue3Components = [image_2, Prediction_Response3, text_4]
        for thisComponent in Cue3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Cue3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Cue3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # *Prediction_Response3* updates
            if t >= 0.5 and Prediction_Response3.status == NOT_STARTED:
                # keep track of start time/frame for later
                Prediction_Response3.tStart = t
                Prediction_Response3.frameNStart = frameN  # exact frame index
                Prediction_Response3.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Prediction_Response3.clock.reset)  # t=0 on next screen flip
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if Prediction_Response3.status == STARTED and t >= frameRemains:
                Prediction_Response3.status = STOPPED
            if Prediction_Response3.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if Prediction_Response3.keys == []:  # then this was the first keypress
                        Prediction_Response3.keys = theseKeys[0]  # just the first key pressed
                        Prediction_Response3.rt = Prediction_Response3.clock.getTime()
            if Prediction_Response3.keys:
                responseMsg = allowable_keys[Prediction_Response3.keys]
            
            # *text_4* updates
            if t >= .5 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            if text_4.status == STARTED:  # only update if drawing
                text_4.setText(responseMsg, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Cue3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Cue3"-------
        for thisComponent in Cue3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Prediction_Response3.keys in ['', [], None]:  # No response was made
            Prediction_Response3.keys=None
        ensureResponse3.addData('Prediction_Response3.keys',Prediction_Response3.keys)
        if Prediction_Response3.keys != None:  # we had a response
            ensureResponse3.addData('Prediction_Response3.rt', Prediction_Response3.rt)
        
        
        # ------Prepare to start Routine "Slow3"-------
        t = 0
        Slow3Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        Slow3Components = [text_10]
        for thisComponent in Slow3Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Slow3"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Slow3Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            if t >= 0.0 and text_10.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_10.tStart = t
                text_10.frameNStart = frameN  # exact frame index
                text_10.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_10.status == STARTED and t >= frameRemains:
                text_10.setAutoDraw(False)
            if Prediction_Response3.keys:
                continueRoutine=False
                ensureResponse3.finished=True
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Slow3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Slow3"-------
        for thisComponent in Slow3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 3 repeats of 'ensureResponse3'
    
    
    # ------Prepare to start Routine "Delay3"-------
    t = 0
    Delay3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_4.setImage(Cue)
    text_11.setText(responseMsg)
    # keep track of which components have finished
    Delay3Components = [image_4, text_11]
    for thisComponent in Delay3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Delay3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Delay3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *text_11* updates
        if t >= 0.0 and text_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_11.tStart = t
            text_11.frameNStart = frameN  # exact frame index
            text_11.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_11.status == STARTED and t >= frameRemains:
            text_11.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Delay3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Delay3"-------
    for thisComponent in Delay3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Feedback3"-------
    t = 0
    Feedback3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    image_5.setImage(Cue)
    Run3EvalRT = event.BuilderKeyResponse()
    text_12.setText(Eval)
    text_13.setText(responseMsg)
    # keep track of which components have finished
    Feedback3Components = [image_5, Run3EvalRT, text_12, text_13]
    for thisComponent in Feedback3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *Run3EvalRT* updates
        if t >= 0.0 and Run3EvalRT.status == NOT_STARTED:
            # keep track of start time/frame for later
            Run3EvalRT.tStart = t
            Run3EvalRT.frameNStart = frameN  # exact frame index
            Run3EvalRT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Run3EvalRT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Run3EvalRT.status == STARTED and t >= frameRemains:
            Run3EvalRT.status = STOPPED
        if Run3EvalRT.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Run3EvalRT.keys = theseKeys[-1]  # just the last key pressed
                Run3EvalRT.rt = Run3EvalRT.clock.getTime()
        
        # *text_12* updates
        if t >= 0.0 and text_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_12.tStart = t
            text_12.frameNStart = frameN  # exact frame index
            text_12.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_12.status == STARTED and t >= frameRemains:
            text_12.setAutoDraw(False)
        
        # *text_13* updates
        if t >= 0.0 and text_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_13.tStart = t
            text_13.frameNStart = frameN  # exact frame index
            text_13.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_13.status == STARTED and t >= frameRemains:
            text_13.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback3"-------
    for thisComponent in Feedback3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Run3EvalRT.keys in ['', [], None]:  # No response was made
        Run3EvalRT.keys=None
    trials_3.addData('Run3EvalRT.keys',Run3EvalRT.keys)
    if Run3EvalRT.keys != None:  # we had a response
        trials_3.addData('Run3EvalRT.rt', Run3EvalRT.rt)
    
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
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "RunDir3"-------
t = 0
RunDir3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
RunDir3Components = [text_14, key_resp_5]
for thisComponent in RunDir3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "RunDir3"-------
while continueRoutine:
    # get current time
    t = RunDir3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['1', '2'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RunDir3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "RunDir3"-------
for thisComponent in RunDir3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "RunDir3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(_thisDir + os.sep + 'conditions/SocaMotiveConditions_Encode_Version%s_Run4.xlsx' %(expInfo['Version'])),
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
    
    # set up handler to look after randomisation of conditions etc
    ensureResponse4 = data.TrialHandler(nReps=3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ensureResponse4')
    thisExp.addLoop(ensureResponse4)  # add the loop to the experiment
    thisEnsureResponse4 = ensureResponse4.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse4.rgb)
    if thisEnsureResponse4 != None:
        for paramName in thisEnsureResponse4.keys():
            exec(paramName + '= thisEnsureResponse4.' + paramName)
    
    for thisEnsureResponse4 in ensureResponse4:
        currentLoop = ensureResponse4
        # abbreviate parameter names if possible (e.g. rgb = thisEnsureResponse4.rgb)
        if thisEnsureResponse4 != None:
            for paramName in thisEnsureResponse4.keys():
                exec(paramName + '= thisEnsureResponse4.' + paramName)
        
        # ------Prepare to start Routine "Cue4"-------
        t = 0
        Cue4Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        image_3.setImage(Cue)
        Prediction_Response4 = event.BuilderKeyResponse()
        responseMsg=''
        # keep track of which components have finished
        Cue4Components = [image_3, Prediction_Response4, text_5]
        for thisComponent in Cue4Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Cue4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Cue4Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_3.status == STARTED and t >= frameRemains:
                image_3.setAutoDraw(False)
            
            # *Prediction_Response4* updates
            if t >= 0.5 and Prediction_Response4.status == NOT_STARTED:
                # keep track of start time/frame for later
                Prediction_Response4.tStart = t
                Prediction_Response4.frameNStart = frameN  # exact frame index
                Prediction_Response4.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(Prediction_Response4.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if Prediction_Response4.status == STARTED and t >= frameRemains:
                Prediction_Response4.status = STOPPED
            if Prediction_Response4.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if Prediction_Response4.keys == []:  # then this was the first keypress
                        Prediction_Response4.keys = theseKeys[0]  # just the first key pressed
                        Prediction_Response4.rt = Prediction_Response4.clock.getTime()
            if Prediction_Response4.keys:
                responseMsg = allowable_keys[Prediction_Response4.keys]
            
            # *text_5* updates
            if t >= 0.5 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t
                text_5.frameNStart = frameN  # exact frame index
                text_5.setAutoDraw(True)
            frameRemains = 3.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_5.status == STARTED and t >= frameRemains:
                text_5.setAutoDraw(False)
            if text_5.status == STARTED:  # only update if drawing
                text_5.setText(responseMsg, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Cue4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Cue4"-------
        for thisComponent in Cue4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Prediction_Response4.keys in ['', [], None]:  # No response was made
            Prediction_Response4.keys=None
        ensureResponse4.addData('Prediction_Response4.keys',Prediction_Response4.keys)
        if Prediction_Response4.keys != None:  # we had a response
            ensureResponse4.addData('Prediction_Response4.rt', Prediction_Response4.rt)
        
        
        # ------Prepare to start Routine "Slow4"-------
        t = 0
        Slow4Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        Slow4Components = [text_15]
        for thisComponent in Slow4Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Slow4"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Slow4Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_15* updates
            if t >= 0.0 and text_15.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_15.tStart = t
                text_15.frameNStart = frameN  # exact frame index
                text_15.setAutoDraw(True)
            frameRemains = 0.0 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_15.status == STARTED and t >= frameRemains:
                text_15.setAutoDraw(False)
            if Prediction_Response4.keys:
                continueRoutine=False
                ensureResponse4.finished=True
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Slow4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Slow4"-------
        for thisComponent in Slow4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed 3 repeats of 'ensureResponse4'
    
    
    # ------Prepare to start Routine "Delay4"-------
    t = 0
    Delay4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image_6.setImage(Cue)
    text_16.setText(responseMsg)
    # keep track of which components have finished
    Delay4Components = [image_6, text_16]
    for thisComponent in Delay4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Delay4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Delay4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_6* updates
        if t >= 0.0 and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t
            image_6.frameNStart = frameN  # exact frame index
            image_6.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_6.status == STARTED and t >= frameRemains:
            image_6.setAutoDraw(False)
        
        # *text_16* updates
        if t >= 0.0 and text_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_16.tStart = t
            text_16.frameNStart = frameN  # exact frame index
            text_16.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_16.status == STARTED and t >= frameRemains:
            text_16.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Delay4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Delay4"-------
    for thisComponent in Delay4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "Feedback4"-------
    t = 0
    Feedback4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    image_7.setImage(Cue)
    Run4EvalRT = event.BuilderKeyResponse()
    text_17.setText(Eval)
    text_18.setText(responseMsg)
    # keep track of which components have finished
    Feedback4Components = [image_7, Run4EvalRT, text_17, text_18]
    for thisComponent in Feedback4Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Feedback4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Feedback4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_7* updates
        if t >= 0.0 and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t
            image_7.frameNStart = frameN  # exact frame index
            image_7.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_7.status == STARTED and t >= frameRemains:
            image_7.setAutoDraw(False)
        
        # *Run4EvalRT* updates
        if t >= 0.0 and Run4EvalRT.status == NOT_STARTED:
            # keep track of start time/frame for later
            Run4EvalRT.tStart = t
            Run4EvalRT.frameNStart = frameN  # exact frame index
            Run4EvalRT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(Run4EvalRT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Run4EvalRT.status == STARTED and t >= frameRemains:
            Run4EvalRT.status = STOPPED
        if Run4EvalRT.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                Run4EvalRT.keys = theseKeys[-1]  # just the last key pressed
                Run4EvalRT.rt = Run4EvalRT.clock.getTime()
        
        # *text_17* updates
        if t >= 0.0 and text_17.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_17.tStart = t
            text_17.frameNStart = frameN  # exact frame index
            text_17.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_17.status == STARTED and t >= frameRemains:
            text_17.setAutoDraw(False)
        
        # *text_18* updates
        if t >= 0.0 and text_18.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_18.tStart = t
            text_18.frameNStart = frameN  # exact frame index
            text_18.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_18.status == STARTED and t >= frameRemains:
            text_18.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Feedback4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback4"-------
    for thisComponent in Feedback4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Run4EvalRT.keys in ['', [], None]:  # No response was made
        Run4EvalRT.keys=None
    trials_4.addData('Run4EvalRT.keys',Run4EvalRT.keys)
    if Run4EvalRT.keys != None:  # we had a response
        trials_4.addData('Run4EvalRT.rt', Run4EvalRT.rt)
    
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
    
# completed 1 repeats of 'trials_4'









# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
