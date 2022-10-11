#link(https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)

def jump():
    move()
    turn_left()
    turn_left()
    turn_left()
      
while front_is_clear():
    move()
    
while not at_goal():    
    if wall_in_front():
        turn_left()
    else:        
        jump()
