from psychopy import visual, event, core, data, gui
from random import choice, shuffle

trials_data = data.importConditions('stimuli_pool.csv')

win = visual.Window([800,450])
mouse = event.Mouse()

'''

Some classes for consize code
class frame():
    def __init__(self, win, core):
        self.win = win
        self.core = core
    def flip(self):
        self.win.flip()
    def wait(self):
        self.core.wait()

class calibration_frame(frame, visual.Circle):
    
class fixation_frame(frame, visual.TextStim):
    
class stimulus_frame(frame, visual.TextStim):

class feature_frame(frame, visual):

'''

trials_subject = trials_data[:16]

for trial in trials_subject:
    if 'escape' in event.getKeys():
        break
    text = visual.TextStim(win, text=trial['text'], color = trial['color_hex'], pos=(0.0, 0.25))
    cross = visual.TextStim(win, text= '+', pos=(0.0, 0.0))
    '''
    dot_coords = [[i, j] for i in [0, 0.75, -0.75] for j in [0, 0.75, -0.75]]
    for coord in dot_coords:
        circle = visual.Circle(win = win, radius = .05, pos = coord,)
        circle.draw()
    '''
    win.flip()
    #fixation
    cross.draw()
    core.wait(0.5)
    #stimulus
    text.draw()
    win.flip()
    core.wait(0.5)
    #fixation
    cross.draw()
    win.flip()
    core.wait(0.5)
    #feature1
    feature = trial['feature_1']
    question = visual.TextStim(win, text= 'What was the stimulus {feature}?'.format(feature = feature), pos=(0.0, 0.75))
    button_text = [trial[feature], trial['{feature}_wrong'.format(feature = feature)]]
    shuffle(button_text)
    button11 = visual.TextBox2(win, text = button_text[0], pos = [-0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])
    button12 = visual.TextBox2(win, text = button_text[1], pos = [0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])

    question.draw()
    button11.draw()
    button12.draw()
    win.flip()
    while not (mouse.isPressedIn(button11) or mouse.isPressedIn(button12)):
        pass
    core.wait(.5)
    #feature2
    feature = trial['feature_2']
    question = visual.TextStim(win, text= 'What was the stimulus {feature}?'.format(feature = feature), pos=(0.0, 0.75))
    button_text = [trial[feature], trial['{feature}_wrong'.format(feature = feature)]]
    shuffle(button_text)
    button11 = visual.TextBox2(win, text = button_text[0], pos = [-0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])
    button12 = visual.TextBox2(win, text = button_text[1], pos = [0.5, -0.5], color = [0, 0, 0], fillColor = [0.5, 0.5, 0.5], size = [0.4, 0.4])

    question.draw()
    button11.draw()
    button12.draw()
    win.flip()
    while not (mouse.isPressedIn(button11) or mouse.isPressedIn(button12)):
        pass
    core.wait(.5)

win.close()
core.quit()