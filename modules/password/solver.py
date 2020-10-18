def solve_password(letters):
    # input would be a nested array, each array
    # consists of letters in one column
    possible_passwords = [
        'about', 'after', 'again', 'below', 'could',
        'every', 'first', 'found', 'great', 'house',
        'large', 'learn', 'never', 'other', 'place',
        'plant', 'point', 'right', 'small', 'sound',
        'spell', 'still', 'study', 'their', 'there',
        'these', 'thing', 'think', 'three', 'water',
        'where', 'which', 'world', 'would', 'write'
    ]

    password_guess = possible_passwords
    tmp = []
    # TODO: this algorithm can be improved!
    # hint: maybe use trie / DP

    # loop through to find the possible values
    for i in range(len(letters)):
        for j in range(len(letters[i])):
            for k in range(len(password_guess)):
                if(password_guess[k][i]==letters[i][j]):
                    tmp.append(password_guess[k])
        password_guess = tmp
        tmp = []
    
    return password_guess