# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name =='lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'wrong name'
  


def number_to_name(number):
    
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'wrong number'
        
    
    
import random
def rpsls(player_choice): 
   
    player_number = name_to_number(player_choice)
    computer_number= random.randrange(0,5)
    computer_choice = number_to_name(computer_number)
    answer = player_number - computer_number
    if answer < 0 :
        answer = answer + 5
        if answer == 1 or answer == 2:
            print 'Player chooses', player_choice
            print 'Computer chooses', computer_choice
            print 'Plyer Wins!'
        elif answer == 3 or answer == 4:
            print 'Player chooses',player_choice
            print 'Computer chooses',computer_choice
            print 'Computer Wins!'
        else:
            print 'Wrong'
    elif answer==0:
        print 'Player chooses',player_choice
        print 'Computer chooses',computer_choice
        print ' Wins Wins!'
    else:
        if answer ==1 or answer ==2:
            print 'Player chooses', player_choice
            print 'Computer chooses',computer_choice
            print 'Player Wins!'
        elif answer ==3:
            print 'Player chooses',player_choice
            print 'Computer choses',computer_choice
            print 'Computer Wins!'
    
                               
    
    
   
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
