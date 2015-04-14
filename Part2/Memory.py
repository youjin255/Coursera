import simplegui
import random

# helper function to initialize globals
def new_game():
    global change, turns, numbers, positions, state, temp1, temp2
    turns = 0
    state = 0
    temp1 = 0
    temp2 = 0
    change = 16 * [False]
    numbers = range(8) + range (8)
    random.shuffle(numbers)
    positions = range(0, 800, 50)
    
# define event handlers
def mouseclick(pos):
    global change, turns, state, temp1, temp2
    for index in range(0, 16):
        if (pos[0] >= positions[index] and
            pos[0] < positions[index] + 50 and
            change[index] == False):
            if state == 0:
                change[index] = True
                temp1 = index
                state = 1
               
            elif state == 1:
                change[index] =True
                temp2 = index
                state = 2
            else :
                if numbers[temp1] != numbers[temp2]:
                    change[temp1] = False
                    change[temp2] = False
                change[index] = True
                temp1 = index
                state = 1
                turns += 1
                                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for index in range(0, 16):
        if change[index]:
            canvas.draw_polygon([(positions[index], 0), (positions[index], 100), 
                                 (positions[index] + 50, 100), (positions[index] + 50 , 0)], 1, "Black", "Black")
            canvas.draw_text(str(numbers[index]), (positions[index] + 20, 60), 30, "White")
    
    for line_pos in positions:
        canvas.draw_line((line_pos, 0), (line_pos, 100), 1, "Red")
        
    label.set_text("Turn = "+str(turns))
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background('Green')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric