# My first stopwatch which has a function of one-playing game
import simplegui

text1 = '0'
text2='0'
text3='0'
text4= '0'
#text5 = '0'
text6 = '0'
text8 = '0'
message = '0:00.0'
message1 = 'John:0'     #message1 is  in right upper ,text5 and text6
message2 = 'Jone:0'     #message2 is  in left upper, text7 and text8


def draw(canvas):
    canvas.draw_text(message,[100,100],36,'White')
    canvas.draw_text(message1,[210,20],24,'Red') 
    canvas.draw_text(message2,[10,20],24,'Red')

def tick():
    global text4
    global text3
    global text2
    global text1
    text4 = str(int(text4)+1)
    
    
    if text4 == '10':
        text4= '0'
        text3= str(int(text3)+1)
    
    if text3 == '10':
        text3 = '0'
        text2 = str(int(text2)+1)
    
    if text2 =='6':
        text2 ='0'
        text1 = str(int(text1)+1)
    
    global message
    message = text1+':'+text2+text3+'.'+text4
   

def start_handler():
    timer.start()

def stop_handler():
    timer.stop()
    
def reset_handler():
    global message
    global message1
    global message2
    global text1,text2,text3,text4,text5,text6
    text1 = '0'
    text2='0'
    text3= '0'
    text4='0'
    text6 = '0'
    text8 = '0'
    timer.stop()
    message = '0:00.0' 
    message1 = 'John:0'
    message2 = 'Jone:0'

def key_handler(key):
    
    if key == simplegui.KEY_MAP['P']:
        global text6
        global message1
        if ((text3 == '4' or text3 =='9')  and (text4 == '8' or text4 =='9' ) or 
           (text3 == '5' or text3 =='0') and text4 =='0'):
            text6 = str(int(text6)+3)
        else:
            text6 = str(int(text6)-1)
        message1 = 'Jone:'+text6
   
            

def key_handler1(key):
    if key == simplegui.KEY_MAP['A']:
        global text8
        global message2
        if ((text3 == '4' or text3 =='9') and (text4=='8' or text4=='9') or
           (text3 == '5' or text3 =='0') and text4 =='0'):
            text8 = str(int(text8) + 3)
        else:
            text8 = str(int(text8) - 1)
        message2 ='John:'+ text8
  


frame = simplegui.create_frame('Stopwatch',300,200)
timer = simplegui.create_timer(100,tick)
button1 = frame.add_button('Start',start_handler,100)
button2 = frame.add_button('Stop',stop_handler,100)
button3 = frame.add_button('Reset',reset_handler,100)
frame.set_keydown_handler(key_handler)
frame.set_keyup_handler(key_handler1)

frame.set_draw_handler(draw)
frame.start()


