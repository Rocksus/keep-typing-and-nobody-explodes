import random

label_pos = {
    'yes': 'left-2',
    'first': 'right-1',
    'display': 'right-3',
    'okay': 'right-1',
    'says': 'right-3',
    'nothing': 'left-2',
    '': 'left-3',
    'blank': 'right-2',
    'no': 'right-3',
    'led': 'left-2',
    'lead': 'right-3',
    'read': 'right-2',
    'red': 'right-2',
    'reed': 'left-3',
    'leed': 'left-3',
    'hold on': 'right-3',
    'you': 'right-2',
    'you are': 'right-3',
    'your': 'right-2',
    'you\'re': 'right-2',
    'ur': 'left-1',
    'there': 'right-3',
    'they\'re': 'left-3',
    'their': 'right-2',
    'they are': 'left-2',
    'see': 'right-3',
    'c': 'right-1',
    'cee': 'right-3'
}

possible_answers = {}
possible_answers['ready'] = ['yes', 'okay', 'what', 'middle', 'left', 'press', 'right', 'blank', 'ready']
possible_answers['first'] = ['left', 'okay', 'yes', 'middle', 'no', 'right', 'nothing', 'uhhh', 'wait', 'ready', 'blank', 'what', 'press', 'first']
possible_answers['no'] = ['blank', 'uhhh', 'wait', 'first', 'what', 'ready', 'right', 'yes', 'nothing', 'left', 'press', 'okay', 'no']
possible_answers['blank'] = ['wait', 'right', 'okay', 'middle', 'blank']
possible_answers['nothing'] = ['uhhh', 'right', 'okay', 'middle', 'yes', 'blank', 'no', 'press', 'left', 'what', 'wait', 'first', 'nothing']
possible_answers['yes'] = ['okay', 'right', 'uhhh', 'middle', 'first', 'what', 'press', 'ready', 'nothing', 'yes']
possible_answers['what'] = ['uhhh', 'what']
possible_answers['uhhh'] = ['ready', 'nothing', 'left', 'what', 'okay', 'yes', 'right', 'no', 'press', 'blank', 'uhhh']
possible_answers['left'] = ['right', 'left']
possible_answers['right'] = ['yes', 'nothing', 'ready', 'press', 'no', 'wait', 'what', 'right']
possible_answers['middle'] = ['blank', 'ready', 'okay', 'what', 'nothing', 'press', 'no', 'wait', 'left', 'middle']
possible_answers['okay'] = ['middle', 'no', 'first', 'yes', 'uhhh', 'nothing', 'wait', 'okay']
possible_answers['wait'] = ['uhhh', 'no', 'blank', 'okay', 'yes', 'left', 'first', 'press', 'what', 'wait']
possible_answers['press'] = ['right', 'middle', 'yes', 'ready', 'press']
possible_answers['you'] = ['sure', 'you are', 'your', 'you\'re', 'next', 'uh huh', 'ur', 'hold', 'what?', 'you']
possible_answers['you are'] = ['your', 'next', 'like', 'uh huh', 'what?', 'done', 'uh uh', 'hold', 'you', 'u', 'you\'re', 'sure', 'ur', 'you are']
possible_answers['your'] = ['uh uh', 'you are', 'uh huh', 'your']
possible_answers['you\'re'] = ['you', 'you\'re']
possible_answers['ur'] = ['done', 'u', 'ur']
possible_answers['u'] = ['uh huh', 'sure', 'next', 'what?', 'you\'re', 'ur', 'uh uh', 'done', 'u']
possible_answers['uh huh'] = ['uh huh']
possible_answers['uh uh'] = ['ur', 'u', 'you are', 'you\'re', 'next', 'uh uh']
possible_answers['what?'] = ['you', 'hold', 'you\'re', 'your', 'u', 'done', 'uh uh', 'like', 'you are', 'uh huh', 'ur', 'next', 'what?']
possible_answers['done'] = ['sure', 'uh huh', 'next', 'what?', 'your', 'ur', 'you\'re', 'hold', 'like', 'you', 'u', 'you are', 'uh uh', 'done']
possible_answers['next'] = ['what?', 'uh huh', 'uh uh', 'your', 'hold', 'sure', 'next']
possible_answers['hold'] = ['you are', 'u', 'done', 'uh uh', 'you', 'ur', 'sure', 'what?', 'you\'re', 'next', 'hold']
possible_answers['sure'] = ['you are', 'done', 'like', 'you\'re', 'you', 'hold', 'uh huh', 'ur', 'sure']
possible_answers['like'] = ['you\'re', 'next', 'u', 'ur', 'hold', 'done', 'uh uh', 'what?','uh huh', 'you', 'like']


class Module:
    def __init__(self, config):
        try:
            self.display = config.display.lower()
            self.label = config.label.lower()
        except:
            print('Unable to load who\'s on first module. There was a problem in loading the bomb config.')

        def generate_module(self):
            display = [
                    'yes', 'first', 'display', 'okay', 
                    'says', 'nothing', '', 'blank', 
                    'no', 'led', 'lead', 'read', 
                    'red', 'reed', 'leed', 'hold on', 
                    'you', 'you are', 'your', 'you\'re', 
                    'ur', 'there', 'they\'re', 'their', 
                    'they are', 'see', 'c', 'cee'
                ]
            label = [
                    'ready', 'first', 'no', 'blank', 
                    'nothing', 'yes', 'what', 'uhhh', 
                    'left', 'right', 'middle', 'okay', 
                    'wait', 'press', 'you', 'you are', 
                    'your', 'you\'re', 'ur', 'u', 
                    'uh huh', 'uh uh', 'what?', 'done', 
                    'next', 'hold', 'sure', 'like'
                ]

            self.display = random.choice(display)
            self.label = random.choice(label)

        def display_module(self):
            print('The text on the display is {} and the text on the label is {}\n'.format(self.display.upper(), self.label.upper()))

        def check_logic(self):
            if (find_position() and find_possible_answers()):
                return True
            return False

        def find_position(self):
            if (self.display in label_pos.keys()):
                return True
            return False
        
        def find_possible_answers(self):
            if (self.label in possible_answers.keys()):
                return True
            return False