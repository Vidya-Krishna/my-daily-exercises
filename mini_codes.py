
#------------------------------
#Just another Banking program
def show_balance(balance: float) -> float:
    print(f"Your balance is: {balance:.2f}")

def amount_not_zero(amount: float) -> float:
    if amount < 0: 
            print("You can't do zat here")
            return 0
    else: return amount

def deposit() -> float:
    amount = float(input("Enter amount to deposit: "))
    return amount_not_zero(amount)

def withdraw(balance: float) -> float:
    withdrawl_amount = float(input('Enter withdrawl_amount: '))
    if withdrawl_amount > balance: 
        print(f"Insufficient funds!!!")
        return 0
    elif withdrawl_amount < 0:
        print("You can't do zat here")
        return 0
    else: return withdrawl_amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("""
             ~~~** *** **~~~
            Banking Options: 
            1. Show Balance
            2. Deposit
            3. Withdraw
            4. Exit""")
        choice = input("Enter (1 - 4): ")
        match choice:
            case "1": show_balance(balance)
            case "2": balance += deposit()
            case "3": balance -= withdraw(balance)
            case "4": is_running = False
            case _: print("Invalid choice")
            
    print("Thank You! Good Day!!")
    
if __name__ == '__main__': main()

#------------------------------
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

