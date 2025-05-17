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

#----------------------------------------------------

