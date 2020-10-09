def solve_button_press(text, color, label, lit, battery):
    text = text.lower()
    label = label.lower()
    if(battery>1 and text=='detonate'):
        return 'Press and immediately release the button'
    elif(battery>2 and label=='frk' and lit):
        return 'Press and immediately release the button'
    elif(color=='red' and text=='hold'):
        return 'Press and immediately release the button'
    else:
        return 'Hold and check label strip color'
    
def solve_button_strip(color):
    color = color.lower()
    if(color=='blue'):
        return 'Release when the countdown timer has a 4 in any position'
    if(color=='yellow'):
        return 'Release when the countdown timer has a 5 in any position'
    else:
        return 'Release when the countdown timer has a 1 in any position'