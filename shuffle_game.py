from random import shuffle

def shuffle_list(my_list):
  shuffle(my_list)
  return my_list

def player_guess():
  guess = ''
  while guess not in ['0','1','2']:
    guess = input("Pick a number: 0,1 or 2: ")
  return int(guess)
    
def check_guess(my_shuffled_list, user_guess):
  if my_shuffled_list[user_guess] == 'O':
    print("Correct!")
  else:
    print("Wrong!")
    print(my_shuffled_list)
  

# INITIAL LIST
game_list = [' ','O',' ']

# SHUFFLE LIST
mixed_up_list = shuffle_list(game_list)

# USER GUESS
my_guess = player_guess()

# CHECK GUESS
check_guess(mixed_up_list,my_guess)