# consecutive stopwatch
# this is for my morning routine, for now only deals with seconds. 


import time

def consecutive_stopwatch(last):
  for i in range (last, 0, -1):
    print(f'\r 00:00:{i:02f}    ', end='')
    time.sleep(1)

last1 = int(input('enter 1st timer: ')    
last2 = int(input('enter 2nd timer: ')
while True:
  consecutive_stopwatch(last1)
  # need to play an alarm here; to_do_list.append(consecutive_stopwatch.py) :(
  consecutive_stopwatch(last2)
  # need to play an alarm here too;
  if input('Y/N: ') not in {'y', 'yes', 'yeah', }:
    break

# i don't want to enter last1, last2 everytime! but should add if user wants to change last1/last2 after a set; 
# the UX sucks for this code. blerghhh
