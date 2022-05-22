import random

random_picker = random.randint(1,10)

loop = True
list_of_clues = ['Just to start the index from 1 I am an dummy value','Lower the value higher is my priority', 'Is it true that I pooed','I am neither free nor a tree', 'May the Force be with you', 'Come on Champ give a Hifi'
, 'The ball is out of the Stadium', 'I am neither Eleven nor a lemon but if you read me twice you will guess who I am?', 'I look like eyes and I am curved all the way',
'Its fine a\'clock', 'I am not hen but I am ben']

def match(random_picker): 
  while(True):
    player_guesses = int(input("Guess the Random Number that is being picked between 1 and 10 \n"))
    
    if random_picker == player_guesses:
      print("Bazzinga! Looks like we have winner")
      print("Do you wish to continue? I yes please press 1 or else press 0")
      exit_status = int(input())
      if exit_status == 1:
        random_picker = random.randint(1,10)
        continue
      elif exit_status == 0:
        break
      
    elif random_picker != player_guesses:
      print(list_of_clues[random_picker])
      
    else:
      loop = False
      
match(random_picker)
