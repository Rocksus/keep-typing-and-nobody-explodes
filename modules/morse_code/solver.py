def solve_morse_code(morse_text):
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

    codes = morse_text.split('/')
    trans_code = ''
    
    for i in codes:
        trans_code += morse_code[codes[i]]
    
    for i in range(len(trans_code)-1):
        possible_answer = trans_code[i:] + trans_code[:i]
        if (possible_answer in possible_freq.keys()):
            return possible_freq[possible_answer]
        
    return 'Not Found'

