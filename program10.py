import random

def main():
    print()
    #Game instructions
    instruction()
    print()
    #Menu
    opt=select()
    print()
    #set accumulators
    computerscore=0
    userscore= 0
    #user draws
    while opt == 1:
        #pick and display card
        score = play()
        #user total score
        userscore +=score 
        print('Total score:',userscore)
        print()
        #if user exceeds 21
        if userscore>21:
            print('You lost! Score greater than 21.')
            again=1
            again=int(input('Type 0 if you would like to play again:'))
            #play again
            if again==0:
                main()
            #quit program
            else:
                opt=3
        #if computerscore is less than 15, call function to pick card
        elif computerscore<15 and userscore<=21:
            compscore=compplay()
            computerscore+=compscore
            opt=select()
        #comp score is greater than 15: game freezes
        else:
            opt = 2
            print('Computer froze the game!')
    #if game freezes:
    if opt == 2:
        end(userscore, computerscore)
    #quit program
    if opt==3:
        print('Thank you for playing!')
        
def instruction():
    print("The goal of the game is to get as close to 21 as possible by drawing cards.")
    print("Try and beat the computer!")
    print("Good luck!")

def select():
    print('1. Draw a card\n2. Freeze the game\n3. Quit the game')
    print()
    opt=int(input('Which action will you take?:'))
    while opt not in [1,2,3]:
        opt=int(input('Error: Please select a valid option!'))
    return opt

def play():
    card = random.randint(1,13)
    suit = random.randint(1,4)
    #card name based on selection
    if card== 11:
        cardname ='Jack of'
    elif card== 12:
        cardname='Queen of'
    elif card==13:
        cardname= 'King of'
    elif card == 1:
        cardname='Ace of'
    else:
        cardname= str(card)+' of'
    #card suit 
    if suit == 1:
        suitname = 'Hearts'
    elif suit == 2:
        suitname='Spades'
    elif suit== 3:
        suitname='Clubs'
    elif suit == 4:
        suitname='Diamonds'
    if card in range(10,14):
        score = 10
    else:
        score=card
    draw= cardname+' '+suitname
    print()
    #display card name
    print('card:',draw)
    
    return score

def compplay():
    card = random.randint(1,13)
    suit = random.randint(1,4)
    if card== 11:
        cardname ='Jack of'
    elif card== 12:
        cardname='Queen of'
    elif card==13:
        cardname= 'King of'
    elif card == 1:
        cardname='Ace of' 
    if suit == 1:
        suitname = 'Hearts'
    elif suit == 2:
        suitname='Spades'
    elif suit== 3:
        suitname='Clubs'
    elif suit == 4:
        suitname='Diamonds'
    if card in range(10,14):
        score = 10
    else:
        score=card
    return score

def end(user,computer):
    #user won
    if computer>21:
        print('You won! computer exceeded 21!')
    if user>computer:
        print('Congrats! You won!')
        print('score:',user)
        print('Computer score:',computer)
    #tie
    elif user == computer:
        print('Congrats! It\'s a tie!')
        print('score:',user)
        print('Computer score:',computer)
    #Computer won
    else:
        print('Computer won!')
        print('score:',user)
        print('Computer score:',computer)
    again=0
    again= int(input('type 1 if you would like to play again:'))
    #play again
    if again==1:
        main()
    #quit program
    else:
        print('Thank you for playing!')
    
    
main()

