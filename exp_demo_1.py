from psychopy import visual, event, core, data, gui
from random import choice, shuffle

trials_data = data.importConditions('stimuli_pool.csv')

trials = data.TrialHandler2(trialList = trials_data, nReps=1)

win = visual.Window([800,450])
mouse = event.Mouse()

#graphical elements
text = visual.TextStim(win, pos=(0.0, 0.25))
question = visual.TextStim(win, pos=(0.0, 0.5))
button_1 = visual.TextBox2(win, text = None, pos = [-0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])
button_2 = visual.TextBox2(win, text = None, pos = [0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])
cross = visual.TextStim(win, text= '+', pos=(0.0, 0.0))


#title screen
title = visual.TextStim(win, pos=(0.0, 0.5), text= "WELCOME TO THE EXPERIMENT", bold = True)
message = visual.TextStim(win, pos=(0.0, 0.0), text= "Press ENTER to procede\nPress ESCAPE to quit")
title.draw()
message.draw()
win.flip()
while True:
    if 'return' in event.getKeys():
        break
    if 'escape' in event.getKeys():
        win.close()
        core.quit()
        break
    
    pass

for trial in trials:
    if 'escape' in event.getKeys():
        win.close()
        core.quit()
    #fixation
    cross.draw() 
    win.flip()
    core.wait(0.5) 
    
    #stimulus
    text.setText(trial['text'])
    text.setColor(trial['color_hex'])
    text.draw()
    win.flip()
    core.wait(0.5)
    
    #fixation
    cross.draw()
    win.flip()
    core.wait(0.5)
    
    #feature1
    feature = trial['feature_1']
    question.setText('What was the stimulus {feature}?'.format(feature = feature))
    button_text = [trial[feature], trial['{feature}_wrong'.format(feature = feature)]]
    shuffle(button_text)
    button_1.setText(button_text[0])
    button_2.setText(button_text[1])
    mouse.setPos()
    question.draw()
    button_1.draw()
    button_2.draw()
    win.flip()
    while True:
        if mouse.isPressedIn(button_1):
            trials.addData('response_1', button_1.getText())
            break
        if mouse.isPressedIn(button_2):
            trials.addData('response_1', button_2.getText())
            break
        
        pass
    core.wait(.5)
    #feature2
    feature = trial['feature_2']
    question.setText('What was the stimulus {feature}?'.format(feature = feature))
    button_text = [trial[feature], trial['{feature}_wrong'.format(feature = feature)]]
    shuffle(button_text)
    button_1.setText(button_text[0])
    button_2.setText(button_text[1])
    mouse.setPos()
    question.draw()
    button_1.draw()
    button_2.draw()
    win.flip()
    while True:
        if mouse.isPressedIn(button_1):
            trials.addData('response_2', button_1.getText())
            break
        if mouse.isPressedIn(button_2):
            trials.addData('response_2', button_2.getText())
            break
        pass
    core.wait(.5)

#trials.data.to_csv('experiment_result.csv', index = False)