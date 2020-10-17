def solve_complicated_wire_letter(letter, parallel_port=False, even_serial=False, batteries=0):
    if(letter=="D"):
        return "Do not cut the wire"
    elif(letter=="C"):
        return "Cut the wire"
    elif(letter=="S"):
        if(even_serial):
            return "Cut the wire"
        else:
            return "Do not cut the wire"
    elif(letter=="P"):
        if(parallel_port):
            return "Cut the wire"
        else:
            return "Do not cut the wire"
    elif(letter=="B"):
        if(batteries>=2):
            return "Cut the wire"
        else:
            return "Do not cut the wire"
    else:
        return "Unknown"

def solve_complicated_wire(red, blue, star, led, parallel_port, even_serial, batteries):
        if(red and blue and star and led):
            return solve_complicated_wire_letter("D")
        elif(red and blue and star and not led):
            return solve_complicated_wire_letter("P", parallel_port, even_serial, batteries)
        elif(red and blue and not star and led):
            return solve_complicated_wire_letter("S", parallel_port, even_serial, batteries)
        elif(red and blue and not star and not led):
            return solve_complicated_wire_letter("S", parallel_port, even_serial, batteries)
        elif(red and not blue and star and led):
            return solve_complicated_wire_letter("B", parallel_port, even_serial, batteries)
        elif(red and not blue and star and not led):
            return solve_complicated_wire_letter("C")
        elif(red and not blue and not star and led):
            return solve_complicated_wire_letter("B", parallel_port, even_serial, batteries)
        elif(red and not blue and not star and not led):
            return solve_complicated_wire_letter("S", parallel_port, even_serial, batteries)
        elif(not red and blue and star and led):
            return solve_complicated_wire_letter("P", parallel_port, even_serial, batteries)
        elif(not red and blue and star and not led):
            return solve_complicated_wire_letter("D")
        elif(not red and blue and not star and led):
            return solve_complicated_wire_letter("P", parallel_port, even_serial, batteries)
        elif(not red and blue and not star and not led):
            return solve_complicated_wire_letter("S", parallel_port, even_serial, batteries)
        elif(not red and not blue and star and led):
            return solve_complicated_wire_letter("B", parallel_port, even_serial, batteries)
        elif(not red and not blue and star and not led):
            return solve_complicated_wire_letter("C")
        elif(not red and not blue and not star and led):
            return solve_complicated_wire_letter("D")
        elif(not red and not blue and not star and not led):
            return solve_complicated_wire_letter("C")