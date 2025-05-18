









#----------------------------------------------------------------------
#bitonic point 
#in a given array, there will be only 1 largest number = bitonic point and after it, the numbers will be strictly decreasing
def largest_num():
  a = list(map(int, input('Enter: ').split()))
  for i, e in enumerate(a[:-1]):
    if e > a[i+1]:
      print(f"bitonic point is: {e}")
largest_num()
    
