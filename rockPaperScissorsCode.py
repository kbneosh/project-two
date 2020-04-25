'''
Created on Apr 20, 2020

@author: ITAUser
'''
import random 

#set variable keepPlaying to true
keepPlaying = True
#While keepPlaying is true:
while(keepPlaying == True):
    print("--------------------------------------------------------")
    #print statement welcoming players to the game
    print ("Welcome to Rock, Paper, Scissors!")
    #print statement stating the rules (best out of 3 press 'q' to quit)
    print("Rules are best out of 3, press 'q' to quit")
    #make a key that assigns a number to each choice for the computer 
    #(rock is 1, scissors is 2, paper is 3)
    rock = 1
    scissors = 2
    paper = 3
    
    #set computer's score to 0
    computer = 0
    #set player's score to 0
    player = 0
    #while player's score is less than 2 and computers score is less than 2:
    while (player < 2 and computer < 2):
        #computer's choice = random number between 1 and 3 
        computerChoice = random.randint(1,3)
        #player's choice = input(ask player to select rock, paper, or scissors)
        playerChoice = input("please choose(Rock, Paper, or Scissors):")
        playerChoice = playerChoice.lower()
        
        #if player inputs 'q' or 'Q':
        if (playerChoice == "q"):
        #   set keepPlaying to false
            keepPlaying = False
        #   stop the loop
            break 
        
        #else if (player inputs rock and computer chooses rock) or
        elif((playerChoice == "rock" and computerChoice == "rock") or (playerChoice == "scissors" and computerChoice == "scissors") or (playerChoice == "paper" and computerChoice == "paper")):
        #(player inputs paper and computer chooses paper) or
        #(player inputs scissors and computer chooses scissors):
        #   print out DRAW
            print("DRAW")
        #   print out player's score and computer's score
            print("player score = " + player.__str__() + " computer score = " + computer.__str__())
        
        #else if (player inputs rock and computer scissors) or
        elif((playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "rock")):
        #(player inputs scissors and computer chooses paper) or
        #(player inputs paper and computer chooses rock):
        #   add one to player's score
            player = player + 1
        #   print out player's score and computer's score
            print("player score = " + player.__str__() + " computer score = " + computer.__str__())
            
        #else if (player inputs rock and computer paper) or
        elif((playerChoice == "rock" and computerChoice == "paper") or (playerChoice == "scissors" and computerChoice == "rock") or (playerChoice == "paper" and computerChoice == scissors)):
        #(player inputs scissors and computer chooses rock) or
        #(player inputs paper and computer chooses scissors):
        #   add one to the computer's score
            computer = computer + 1
        #   print out player's and computer's score
            print("player score = " + player.__str__() + " computer score = " + computer.__str__())
        
        #else:
        else:
        #   tell the user their input was not valid
            print("Your input is invalid, try again")
            
    #print statement thanking the players for playing 
    print("Thank you for playing!")
    #if player's score is 2:
    if player == 2:
    #   print statement letting player know they won
        print("Congrats, you won :)")
    #if computer's score is 2
    if computer == 2:
    #   print statement letting player know the computer won 
        print("Sorry, computer won :(")
    
    #print out player's score and computer's score 
    print("player score = " + player.__str__() + " computer score = " + computer.__str__())
    