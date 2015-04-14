
import simplegui
import random

range_num= 100



def new_game():
    global num
    num = 7
    global secret_number
    secret_number = random.randrange(0,range_num)
    print 'New game. Range is from 0 to',range_num
    print 'Number of remainding guesses is',num
    print ''


def range100():
    global range_num
    range_num = 100
    new_game()

def range1000():
    global range_num 
    range_num = 1000
    new_game()
def input_guess(guess):
    guess = int(guess)
    print 'Guess was',guess
    global num
    num = num - 1
    if num <=0:
        print 'number of guesses is',num
        print 'Guess out of range. The secret_number was',secret_number
        print ''
        new_game()
        print ''
    else:
        print 'Number of remainding guess is',num
        if guess > secret_number:
            print 'Lower'
            print ''
        elif guess < secret_number:
            print 'Higher'
            print ''
        else:
            print 'You got it!'
            print ''
            new_game()
            print ''
  
    
frame = simplegui.create_frame('Guess number',300,300)
frame.add_button('Range [0,100)',range100,200)
frame.add_button('Range [0,1000)',range1000,200)
frame.add_input('Input guess',input_guess,200)


new_game()

frame.start()


