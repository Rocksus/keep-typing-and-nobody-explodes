import random

possible_freq = {
    'shell' : '3.505',
    'halls' : '3.515',
    'slick' : '3.522',
    'trick' : '3.532',
    'boxes' : '3.535',
    'leaks' : '3.542',
    'strobe' : '3.545',
    'bistro' : '3.552',
    'flick' : '3.555',
    'bombs' : '3.565',
    'break' : '3.572',
    'brick' : '3.575',
    'steak' : '3.582',
    'sting' : '3.592',
    'vector' : '3.595',
    'beats' : '3.600' 
}

morse_code = {
    '.-' : 'a',
    '-...' : 'b',
    '-.-.' : 'c',
    '-..' : 'd',
    '.' : 'e',
    '.._.' : 'f',
    '--.' : 'g',
    '....' : 'h',
    '..' : 'i',
    '.---' : 'j',
    '-.-' : 'k',
    '.-..' : 'l',
    '--' : 'm',
    '-.' : 'n',
    '---' : 'o',
    '.--.' : 'p',
    '--.-' : 'q',
    '.-.' : 'r',
    '...' : 's',
    '-' : 't',
    '..-' : 'u',
    '...-' : 'v',
    '.--' : 'w',
    '-..-' : 'x',
    '-.--' : 'y',
    '--..' : 'z'
}

class Module:
    def __init__(self, config):
        try:
            self.morse = config.morse
        except:
            print('Unable to load morse code module. There was a problem in loading the bomb config.')
    
    def generate_module(self):
        self.morse_text = ''
        rev_morse_code = {value : key for (key, value) in morse_code.items()}
        solution = random.choice(possible_freq.keys())
        solution_len = len(solution)

        st_index = random.randint(0, solution_len-1)
        if (st_index > 0):
            text = solution[st_index:] + solution[:st_index]
        else:
            text = solution
        
        for i in range(solution_len):
            self.morse_text += rev_morse_code[text[i]] + '/'
        
    def display_module(self):
        print('The morse code is {}\n'.format(self.morse_text))

    def check_logic(self):
        answer = self.translate_morse()
        if (answer in possible_freq.keys()):
            return True
        return False
    
    def translate_morse(self):
        codes = self.morse_text.split('/')
        trans_code = ''
        
        for i in codes:
            trans_code += morse_code[codes[i]]
        
        for i in range(len(trans_code)-1):
            possible_answer = trans_code[i:] + trans_code[:i]
            if (possible_answer in possible_freq.keys()):
                return possible_answer

        return possible_answer

