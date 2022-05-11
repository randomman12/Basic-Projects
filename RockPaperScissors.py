#Imported random module for random choice 
import random


#while loop to ensure user can quit or play again

#RPC = Rock, Paper, Scissors
RPS = ['rock', 'paper', 'scissors']
while True:
  #Asks user to input text (no input formatting)
  user = input('Pick rock paper or scissors \n')
  #randomly selects from rock, paper or scissors
  comp = (random.choice(RPS))
  #using f replaces expressions with a value
  print(f"You chose {user}, Computer chose {comp}")
  # If statements for draw
  if user == comp:
    print ("Draw")
    # if statement for user picking rock 
  elif user == 'rock':
    if comp == 'paper':
      print ('You Lose')
    else: print ('You Win!')
   #if statement for picking paper   
  elif user == 'paper':
    if comp == 'rock':
      print ('You win')
    else: print('You Lose')
  #if statement for picking scissors
  elif user == 'scissors':
    if comp == 'rock':
      print ('you lose')
    else: print ('you win')
  

#allows user to break loop or play again depending on input 
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break
