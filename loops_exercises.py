



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

