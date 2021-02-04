import random

#TODO: This module should automatically counts the stage and remember the result from each stage

class Module:
    def __init__(self, config):
        try:
            self.stage = config.stage
            self.display = config.display
        except:
            print('Unable to load memory module. There was a problem in loading the bomb config.')

        def generate_module(self):
            self.stage = random.randint(1,5)
            self.display = random.randint(1, 4)

        def display_module(self):
            print('This is stage {} and the number on the display is {}\n'.format(self.stage, self.display))

        def check_logic(self, action):
            if (self.stage == 1):
                solution = self.solve_first_stage()
            elif (self.stage == 2):
                solution = self.solve_second_stage()
            elif (self.stage == 3):
                solution = self.solve_third_stage()
            elif (self.stage == 4):
                solution = self.solve_fourth_stage()
            else:
                solution = self.solve_fifth_stage()
            
            if (action == solution):
                return True
            return False

        # n = label n
        # n0 = label in n-th POSITION
        # 10n = label in the same POSITION as stage n
        # 1n = same label as stage n

        def solve_first_stage(self):
            if (self.display == 1 or self.display == 2):
                return 20
            if (self.display == 3):
                return 30
            if (self.display == 4):
                return 40
        
        def solve_second_stage(self):
            if (self.display == 1):
                return 4
            if (self.display == 2 or self.display == 4):
                return 101
            if (self.display == 3):
                return 10
        
        def solve_third_stage(self):
            if (self.display == 1):
                return 12
            if (self.display == 2):
                return 11
            if (self.display == 3):
                return 30
            if (self.display == 4):
                return 4
        
        def solve_fourth_stage(self):
            if (self.display == 1):
                return 101
            if (self.display == 2):
                return 10
            if (self.display == 3 or self.display == 4):
                return 102
        
        def solve_fifth_stage(self):
            if (self.display == 1):
                return 11
            if (self.display == 2):
                return 12
            if (self.display == 3):
                return 14
            if (self.display == 4):
                return 13

