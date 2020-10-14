# solve_simple_wires handles the decision
# on which wire to cut.
# 
# Input should be a list of string, representing the wire color
# and whether the serial is odd or even with a boolean flag.
def solve_simple_wires(wires, odd_serial):
    colors = {}
    for wire in wires:
        if(wire in colors):
            colors[wire] += 1
        else:
            colors[wire] = 1
    
    ll = len(wires)
    if(ll == 3):
        if('red' not in colors):
            return 'Cut the second wire'
        elif(wires[-1]=='white'):
            return 'Cut the last wire'
        elif('blue' in colors and colors['blue']>1):
            return 'Cut the last blue wire'
        return 'Cut the last wire'
    elif(ll == 4):
        if('red' in colors and colors['red']>=1 and odd_serial):
            return 'Cut the last red wire'
        elif(wires[-1]=='yellow' and 'red' not in colors):
            return 'Cut the first wire'
        elif('blue' in colors and colors['blue']==1):
            return 'Cut the first wire'
        elif('yellow' in colors and colors['yellow']>1):
            return 'Cut the last wire'
        return 'Cut the second wire'
    elif(ll == 5):
        if(wires[-1]=='black' and odd_serial):
            return 'Cut the fourth wire'
        elif('red' in colors and colors['red']==1 and 'yellow' in colors and colors['yellow']>1):
            return 'Cut the first wire'
        elif('black' not in colors):
            return 'Cut the second wire'
        return 'Cut the first wire'
    elif(ll == 6):
        if('yellow' not in colors and odd_serial):
            return 'Cut the third wire'
        elif('yellow' in colors and colors['yellow']==1 and 'white' in colors and colors['white']>1):
            return 'Cut the fourth wire'
        elif('red' not in colors):
            return 'Cut the last wire'
        return 'Cut the fourth wire'
    else:
        return "Invalid"