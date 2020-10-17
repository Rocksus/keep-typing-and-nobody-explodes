import random

possible_passwords = [
        'about', 'after', 'again', 'below', 'could',
        'every', 'first', 'found', 'great', 'house',
        'large', 'learn', 'never', 'other', 'place',
        'plant', 'point', 'right', 'small', 'sound',
        'spell', 'still', 'study', 'their', 'there',
        'these', 'thing', 'think', 'three', 'water',
        'where', 'which', 'world', 'would', 'write'
    ]

# TODO: this module should implement the main module generator class
class Module:
    def generate_module(self):
        # TODO: there's a better way to generate one unique solution
        self.letters = []
        solution = random.choice(possible_passwords)
        for i in range(5):
            self.letters.append([])
            candidates = [
                'a','b','c','d','e','f','g','h','h','i',
                'j','k','l','m','n','o','p','q','r','s',
                't','u','v','w','x','y','z'
            ]
            # append the solution
            self.letters[i].append(solution[i])
            candidates.remove(solution[i])
            for j in range(5):
                candidate = random(candidates)
                self.letters[i].append(candidate)
                candidates.remove(candidate)
            random.shuffle(self.letters[i])
    def dispaly_module(self):
        for i in range(self.letters):
            print('Col {}: {}'.format(i, self.letters[i][0]))
    def change_letters(self, index, direction):
        col = self.letters[index]
        if(direction == 'up'):
            # left rotate the array
            temp = col[0]
            for i in range(len(col)-1):
                col[i] = col[i+1]
            col[-1]=temp
        elif(direction == 'down'):
            # right rotate the array
            temp = col[-1]
            for i in range(len(col)-1):
                col[-(i+1)]=col[-(i+2)]
            col[0]=temp
        self.letters[index]=col

    def check_logic(self):
        # gather the letters in each column
        guess = self.letters[0][0] + self.letters[1][0] + self.letters[2][0] + self.letters[3][0] + self.letters[4][0]
        if(guess in self.find_possible_solutions()):
            return True
        return False
    def find_possible_solutions(self):
        password_guess = possible_passwords
        tmp = []
        # TODO: this algorithm can be improved!
        # hint: maybe use trie / DP
        
        # loop through to find the possible values
        for i in range(len(self.letters)):
            for j in range(len(self.letters[i])):
                for k in range(len(password_guess)):
                    if(password_guess[k][i]==self.letters[i][j]):
                        tmp.append(password_guess[k])
            password_guess = tmp
            tmp = []
        
        return password_guess
        