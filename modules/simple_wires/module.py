import random

# TODO: this module should implement the main module generator class
class Module:
    def __init__(self, config):
        try:
            self.odd_serial = config.odd_serial
        except:
            print("Unable to load simple wires module. There was a problem in loading the bomb config.")

    # generate_module will be responsible in generating the class module
    def generate_module(self):
        colors = ['yellow', 'red', 'blue', 'black', 'white']
        num_of_wires = random.randint(3, 6)
        self.wires = []
        for x in range(num_of_wires):
            self.wires.append(random.choice(colors))

    def display_module(self):
        # TODO: improve this display function
        # This will be the simplified implementation for now, no fancy ASCII art
        for x, i in enumerate(self.wires):
            print('Wire{}: {}\n'.format(i, x))

    # check logic will be responsible in checking whether the input was correct or not
    def check_logic(self, index):
        solution = self.cut_simple_wires()
        if(index == solution):
            return True
        return False
    # solve_simple_wires handles the decision
    # on whether the wires being cut was right or not
    # will input 
    def cut_simple_wires(self):
        colors = {}
        wires = self.wires
        odd_serial = self.odd_serial
        for wire in wires:
            if(wire in colors):
                colors[wire] += 1
            else:
                colors[wire] = 1
        
        ll = len(wires)
        if(ll == 3):
            if('red' not in colors):
                return 1
            elif(wires[-1]=='white'):
                return 2
            elif('blue' in colors and colors['blue']>1):
                return max(idx for idx, val in enumerate(wires) if val =='blue')
            return 2
        elif(ll == 4):
            if('red' in colors and colors['red']<=1 and odd_serial):
                return max(idx for idx, val in enumerate(wires) if val =='red')
            elif(wires[-1]=='yellow' and 'red' not in colors)
                return 0
            elif('blue' in colors and colors['blue']==1):
                return 0
            elif('yellow' in colors and colors['yellow']>1):
                return 3
            return 1
        elif(ll == 5):
            if(wires[-1]=='black' and odd_serial):
                return 3
            elif('red' in colors and colors['red']==1 and 'yellow' in colors and colors['yellow']>1):
                return 0
            elif('black' not in colors):
                return 1
            return 0
        elif(ll == 6):
            if('yellow' not in colors and odd_serial):
                return 2
            elif('yellow' in colors and colors['yellow']==1 and 'white' in colors and colors['white']>1):
                return 3
            elif('red' not in colors):
                return 5
            return 3
        else:
            return -1