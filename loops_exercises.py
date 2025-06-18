
"""
Nested data processing
pythonstudents = [
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [92, 87, 95]},
    {"name": "Charlie", "grades": [78, 82, 85]}
]
# Create dict with name as key, average grade as value
Multiple conditions
python# Create dict of numbers 1-20 where key is the number and value is:
# "fizzbuzz" if divisible by both 3 and 5
# "fizz" if divisible by 3
# "buzz" if divisible by 5  
# the number itself otherwise
"""

#------------------------------ 
# sum of numbers divisible by 3 or 5 in given range
#here range is 1000
def sum_three_five() -> int:
    l = []
    for i in range(3, 501):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)
    return (sum(l))

print(sum_three_five())
#------------------------------ 
#harshad number / Niven number
 def niven_number(n):
     count = 0
     for i in n:
         count += int(i)
     return ('yes' if int(n) % count == 0 else 'no')

n = input('enter a num to check: ')
print(f'Is {n} a Niven number: {niven_number(n)}')

#------------------------------ 
# printing 3x3 matrix using loops
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

            #--------------
#right corner 
for i in m:
    print(i[len(i)-1])

            #--------------
#left corner
for i in m:
    print(i[0])

            #--------------
#diagonal1 
count = 0
for i in m:
    print(i[count])
    count += 1

            #--------------
#diagonal2 
new_count = 1
for i in m:
    count = len(i)-new_count
    print(i[count])
    new_count += 1

            #--------------
#sum of each row 
for i in m:
    total = 0
    #iteration 1; i = [1,2,3]
    for j in i:
        #iteration 1; j = i[0] = 1 till iteration3 j = i[2] = 3
        total += j
    print('~~~~~* ** *** ** *~~~~~')
    print(total) 



#-------------------------------------------
# number guessing program
import random

def fourth_attempt_iirc():
    low, high = 1, 100
    cg = random.randint(low, high)
    print(cg)
    count = 0
    is_running = True

    while is_running:
        n = (input(f'guess a num in range {low}, {high}: '))
        count += 1
        if n.isdigit():
            n = int(n)
            if n > cg and n > low and n <= high:
                print('cold, try a lower number')
            elif n < cg and n > low and n <= high:
                print('hot, try a higher number')
            elif n < low or n > high:
                print('please enter rangebound int only')
            else:
                print(f'correct, number of gueese: {count}')
                is_running = False
        elif not n.isdigit():
            print('enter integers only')

fourth_attempt_iirc()
           #------------------------------ #same as above, but below is small corrections acc to chat gpt #------------------------------ 
import random

def fourth_attempt_iirc():
    low, high = 1, 100
    cg = random.randint(low, high)
    print(cg)
    count = 0
    is_running = True

    while is_running:
        n = (input(f'guess a num in range {low}, {high}: '))
        count += 1
        if n.isdigit():
            n = int(n)
            if n < low or n >= high: #n > cg and n > low and n <= high:
                print('please enter rangebound int only')#print('cold, try a lower number')
            elif n < cg and n > low and n <= high:
                print('hot, try a higher number')
            elif n > cg and n > low and n <= high:
                print('cold, try a lower number')
            else:
                print(f'correct, number of gueese: {count}')
                is_running = False
        elif not n.isdigit():
            print('enter integers only')

fourth_attempt_iirc()
# here I tested for
#1. -ve numbres = program worked!
#2. out of range int = program worked!
#3. space " " = program worked!
#4. just enter / return = program worked!
#5. If you find any edge-cases, share them!!!
#----------------------------------------------------------
#using random.randint()
n = int(input('Enter n times you want to get random number; n> 0: ')
def random_number():
    n1 = int(input('Enter start range: ')
    n1 = int(input('Enter end range: ')
    print(random.randint(n1, n2))
def multiple_random_numbers():
    for i in range(n):
        random_number()

multiple_random_numbers()
#it broke for my tets_case_1, tets_case_2, tets_case_3, .........
#added this to my infinte to do list
#----------------------------------------------------------
#nested for loop exercise
def invalid_input():
    while True:
        if n.lower() not in ['a', 'b', 'c', 'd', 'e']:
            n = input(('Enter a valid input: '))
            
def market_knowledge():
    q = (('What is the fastest stock exchange in the world'), 
         ('First bank in India listed in NYSE'), 
         ('NSE established in which year'), 
         ('NSE HQ is at'), 
         ('Which agency regulates stock market of India'))
    o = (('NSE',    'NYSE',      'BSE',       'NIKKEI', 'NASDAQ'),
         ('SBI',    'ICICI',     'HFDC',      'AXIS',   'KOTAK'),
         ('1991',   '1992',      '1993',      '1994',   '1995'),
         ('DELHI',  'BANGALORE', 'HYDERABAD', 'MUMBAI', 'CHENNAI'),
         ('NABARD', 'RBI',       'ED',        'CCI',     'SEBI'))

    key = ('c', 'b', 'b', 'd', 'e')
    j_count = 0
    score = 0
    
    for i in q:
        print('---------------------')
        print(i)
        for j in o[j_count]:
            print(j)
        n = input('Choose an option: ')
        print('')
        # invalid_input()    #trying to implement this but getting errors, will catchu up with this later
        if n.lower() == key[j_count]: 
            print(f"Correct")
            score += 1
        else :
            print('Wrong')
            print(f"The correct answer was {key[j_count]}")
        j_count += 1
    print(f"you got {score} correct out of {len(key)}")
market_knowledge()
#----------------------------------------------------------
#check if input number 'n' is a palindrome
def is_plaindrome():
  n = int(input('Enter: '))
  r = 0
  a = n
  while n>0:
    d = n%10
    r = r * 10 + d
    n = n//10
  print('is plaindrom' if r == a else 'not plaindrom')
is_plaindrome()
#----------------------------------------------------------
#reverse an int
def reversed_num():
  n = int(input('Enter an int: ')
  r = 0
  while n > 0:
    a = n % 10
    r = r * 10 + a
    n = n//10
  print(r)
reversed_num()
#this is only working for unsigned int / positive values
#----------------------------------------------------------
#count number of digits in a number 
def count_digits():
  count = 0
  while n > 0:
    n = n//10
    count += 1
  print(count)
count_digits()
#I think i can also add asking user input again until n != 0
#----------------------------------------------------------

