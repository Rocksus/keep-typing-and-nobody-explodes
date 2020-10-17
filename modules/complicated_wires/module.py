import random

# TODO: this module should implement the main module generator class
class Module:
    def __init__(self, config):
        try:
            self.even_serial = not config.odd_serial
            self.parallel_port = config.parallel_port
            self.batteries = config.batteries
        except:
            print('Unable to load complicated wires module. There was a problem in loading the bomb config.')
    def generate_module(self):
        num_of_wires = random.randint(1,6)
        self.wires = []
        for x in range(num_of_wires):
            self.wires.append([random.getrandbits(), random.getrandbits(), random.getrandbits(), random.getrandbits()])
        
    def display_module(self):
        for x, i in enumerate(self.wires):
            print('Wire {}:\n', format(i))
            if(x[0] == True):
                print("\tIt has red\n")
            if(x[1] == True):
                print("\tIt has blue\n")
            if(x[2] == True):
                print("\tThere's a star symbol\n")
            if(x[3] == True):
                print("\tLED is on\n")
    
    def check_logic(self, index):
        return self.solve_complicated_wire(index)

    def solve_complicated_wire(self, index):
        red = self.wires[index][0]
        blue = self.wires[index][1]
        star = self.wires[index][2]
        led = self.wires[index][3]
        if(red and blue and star and led):
            return solve_complicated_wire_letter("D")
        elif(red and blue and star and not led):
            return solve_complicated_wire_letter("P")
        elif(red and blue and not star and led):
            return solve_complicated_wire_letter("S")
        elif(red and blue and not star and not led):
            return solve_complicated_wire_letter("S")
        elif(red and not blue and star and led):
            return solve_complicated_wire_letter("B")
        elif(red and not blue and star and not led):
            return solve_complicated_wire_letter("C")
        elif(red and not blue and not star and led):
            return solve_complicated_wire_letter("B")
        elif(red and not blue and not star and not led):
            return solve_complicated_wire_letter("S")
        elif(not red and blue and star and led):
            return solve_complicated_wire_letter("P")
        elif(not red and blue and star and not led):
            return solve_complicated_wire_letter("D")
        elif(not red and blue and not star and led):
            return solve_complicated_wire_letter("P")
        elif(not red and blue and not star and not led):
            return solve_complicated_wire_letter("S")
        elif(not red and not blue and star and led):
            return solve_complicated_wire_letter("B")
        elif(not red and not blue and star and not led):
            return solve_complicated_wire_letter("C")
        elif(not red and not blue and not star and led):
            return solve_complicated_wire_letter("D")
        elif(not red and not blue and not star and not led):
            return solve_complicated_wire_letter("C")

    def solve_complicated_wire_letter(self, letter):
        if(letter=="D"):
            return False
        elif(letter=="C"):
            return True
        elif(letter=="S"):
            if(self.even_serial):
                return True
            else:
                return False
        elif(letter=="P"):
            if(self.parallel_port):
                return True
            else:
                return False
        elif(letter=="B"):
            if(self.batteries>=2):
                return True
            else:
                return False
        else:
            return False