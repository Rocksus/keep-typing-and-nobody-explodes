import random

# TODO: this module should implement the main module generator class
class Module:
    def __init__(self, config):
        try:
            self.label = config.label.lower()
            self.lit = config.lit
            self.batteries = config.batteries
            #pressed is to indiciate if the button have been pressed
            self.pressed = False
        except:
            print('Unable to load button module. There was a problem in loading the bomb config.')
    def generate_module(self):
        button = ['blue', 'white', 'yellow', 'red', 'black']
        text = ['abort', 'detonate', 'hold', 'press', '']
        strip = ['blue', 'red', 'white', 'yellow']
        self.button = random.choice(button)
        self.text = random.choice(text)
        self.strip = random.choice(strip)
    def display_module(self):
        # TODO: improve this display function
        # This will be the simplified implementation for now, no fancy ASCII art
        if(not self.pressed):
            print('Button color is {} and has a {} label on it\n'.format(self.button, self.text.upper()))
        else:
            print('The strip is colored {}\n', self.strip)
    def check_logic(self, action):
        # TODO: there should be a better way to do this
        #
        # should the input of the strip be in time?
        # if that's so we need to parse the time first and check!
        if(not self.pressed):
            solution = self.check_button()
            if(action==solution):
                return True
            return False
        else:
            solution = self.check_strip()
            if(action==solution):
                return True
            return False
    def check_button(self):
        if(self.batteries>1 and self.text=='detonate'):
            return 0
        elif(self.batteries>2 and self.label=='frk' and self.lit):
            return 0
        elif(self.color=='red' and self.text=='hold'):
            return 0
        else:
            return 1
    def check_strip(self):
        if(color=='blue'):
            return 4
        if(color=='yellow'):
            return 5
        else:
            return 1