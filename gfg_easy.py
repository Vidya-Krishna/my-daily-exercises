




#-------------------------------------------
#this took me 40 minutes to solve.
#The array has only one repetitive element. Find the repetitive element.
a = [4, 1, 5, 2, 3, 1]
n = 1
for i in range(len(a)):
    x = a[i]
    for j in a[n:]:
        if j == k:
            print(k)
            break
    n += 1

#----------------------------------------------------------------------
#bitonic point 
#in a given array, there will be only 1 largest number = bitonic point and after it, the numbers will be strictly decreasing
def largest_num():
  a = list(map(int, input('Enter: ').split()))
  for i, e in enumerate(a[:-1]):
    if e > a[i+1]:
      print(f"bitonic point is: {e}")
largest_num()
    
