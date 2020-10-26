def solve_memory(stage, display):
    if (stage == 1):
        if (display == 1 or display == 2):
            return 'Press the button in the second position'
        if (display == 3):
            return 'Press the button in the third position'
        if (display == 4):
            return 'Press the button in the fourth position'
    
    elif (stage == 2):
        if (display == 1):
            return 'Press the button labeled [4]'
        if (display == 2 or display == 4):
            return 'Press the button in the same position as stage 1'
        if (display == 3):
            return 'Press the button in the first position'
    
    elif (stage == 3):
        if (display == 1):
            return 'Press the button with the same label as stage 2'
        if (display == 2):
            return 'Press the button with the same label as stage 1'
        if (display == 3):
            return 'Press the button in the third position'
        if (display == 4):
            return 'Press the button labeled [4]'
    
    elif (stage == 4):
        if (display == 1):
            return 'Press the button in the same position as stage 1'
        if (display == 2):
            return 'Press the button in the first position'
        if (display == 3 or display == 4):
            return 'Press the button in the same position as stage 2'
    
    else:
        if (display == 1):
            return 'Press the button with the same label as stage 1'
        if (display == 2):
            return 'Press the button with the same label as stage 2'
        if (display == 3):
            return 'Press the button with the same label as stage 4'
        if (display == 4):
            return 'Press the button with the same label as stage 3'