#just another num_guessing code
import random

def mini_proj_num_guess():
  low = 1
  high = 100
  cg = random.randint(low, high)
  gc = 0
  is_running = True
  
  while is_running:
    n = input(f'Guess an int between {low}, {high}: ')

    if n.isdigit():
      n = int(n)
      if n < 0 or n > 100:
        print(f'range bound error, please enter an int between {low}, {high} ')
      elif n > cg:
        gc += 1
        print('cold, try a lower number')
      elif n < cg:
        gc += 1
        print('hot, try a high number')
      else:
        gc += 1
        print(f'correct, it matched in {gc} times')
        is_running = False
    else:
      invalid_gc += 1
      print('please enter an **int**  between {low}, {high} ')

mini_proj_num_guess()

#passed for inputs: space, just return/enter, -ve inputs, out of range ints
#need to add Difficulty levels (e.g., fewer attempts allowed) | Tracking all previous guesses | Scoring system

