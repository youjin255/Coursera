
import math
import simplegui
import random


WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

HALF_WIDTH = WIDTH/2
HALF_HEIGHT = HEIGHT/2
ball_pos = [HALF_WIDTH,HALF_HEIGHT]

vel = 0
vel1 = 0
vel2 = [0,0]

score1 = '0'
score2 = '0'

paddle1_pos = [HALF_PAD_WIDTH,HALF_HEIGHT]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH,HALF_HEIGHT]



def keydown(key):
    if key == simplegui.KEY_MAP['w']:
        global vel
        vel = vel -3
    elif key == simplegui.KEY_MAP['s']:
       
        vel = vel + 3

def keyup(key):
    if key == simplegui.KEY_MAP['up']:
        global vel1
        vel1 -=3
    elif key == simplegui.KEY_MAP['down']:
        vel1 +=3
def start1():
    global vel2
    vel2 = [3,3]
    
def resert():
    global paddle1_pos,paddle2_pos,ball_pos,vel,vel1,vel2 
    global score1,score2
    ball_pos = [HALF_WIDTH,HALF_HEIGHT]
    
    vel = 0
    vel1 = 0
    vel2 = [0,0]

    score1 = '0'
    score2 = '0'

    paddle1_pos = [HALF_PAD_WIDTH,HALF_HEIGHT]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH,HALF_HEIGHT]


        
        
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
  
   
   
    ball_pos[0] += vel2[0]
    ball_pos[1] -= vel2[1]
    if ball_pos[1]<=20:
        vel2[1] = -vel2[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
        vel2[1] = - vel2[1]
    if paddle2_pos[0] - ball_pos[0] <= (HALF_PAD_WIDTH+BALL_RADIUS)and math.fabs(paddle2_pos[1] - ball_pos[1])<= HALF_PAD_HEIGHT:
        vel2[0] = - vel2[0]
        global score2
        score2 = str(int(score2) +1)
        
    if ball_pos[0] - paddle1_pos[0]<=(HALF_PAD_WIDTH+BALL_RADIUS):# and math.fabs(paddle1_pos[1] - ball_pos[1])<= HALF_PAD_HEIGHT:
        vel2[0] = - vel2[0]
        global score1
        score1 = str(int(score1)+1)
        
    canvas.draw_circle(ball_pos,BALL_RADIUS,0.1,'White','White')
    
    
    paddle1_pos[1] += vel
    canvas.draw_polygon([[0,paddle1_pos[1] - HALF_PAD_HEIGHT ],
                        [paddle1_pos[0] + HALF_PAD_WIDTH,paddle1_pos[1] - HALF_PAD_HEIGHT  ], 
                        [PAD_WIDTH,paddle1_pos[1] + HALF_PAD_HEIGHT ],
                        [0,paddle1_pos[1] + HALF_PAD_HEIGHT ]],
                        0.1,'White','White')
    paddle2_pos[1] +=vel1                                      
    canvas.draw_polygon([[paddle2_pos[0] - HALF_PAD_WIDTH,paddle2_pos[1] - HALF_PAD_HEIGHT +vel1],                                
                         [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT + vel1],
                         [WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT + vel1],
                         [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT + vel1]],
                         0.1, 'White','White')
                        
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(score1,[HALF_WIDTH -80,80],48,'Red')
    canvas.draw_text(score2, [HALF_WIDTH +80,80],48,'Red')
        

   


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Resert',resert,100)
frame.add_button('Start',start1,100)




# start frame
new_game()
frame.start()
