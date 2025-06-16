
#-------------------------------------------
import time
start_time = time.time()
"""
Form largest number from digits
Difficulty: Easy
Given an array arr[] of numbers from 0 to 9. Your task is to rearrange elements of the array 
such that after combining all the elements of the array, the number formed is maximum.

Examples:

Input: arr[] = [9, 0, 1, 3, 0]
Output: 93100
Explanation: Largest number is 93100 which can be formed from array digits.

Input: arr[] = [1, 2, 3]
Output: 321
"""
#But for ultra-large inputs, Python handles big integers well, 
# but converting them to strings (or printing them) can be slower. 
# If ever hit limits:
#Consider building as a string instead (e.g., ''.join(map(str, sorted(arr, reverse=True))))

import time
start_time = time.time()
def descending_order_brute_force(arr: list) -> int:
    arr.sort(reverse = True)
    total = 0
    for i in arr:
        total += i
        total *= 10
    return(total//10)

print(descending_order_brute_force(arr = [9]*1000))

end_time = time.time()
print(f"Time spent: {round(end_time - start_time, 2)} seconds")

""" 
test_case_one: arr = [0, 0, 0]
# Expected: 0
✅passed

test_case_two: arr = [5]
# Expected: 5
✅passed

test_case_three: arr = [3, 3, 3]
# Expected: 333
✅passed

test_case_four: arr = [9, 8, 7, 6]
# Expected: 9876
✅passed

test_case_five: arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected: 9876543210
✅passed

test_case_six: arr = [9]*1000
# Expected: a number with 1000 nines
✅passed

"""


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
    n += 1                    #this approach sucks as time complexity  = O(n) in worst case
    
                #------------
seen = set()
for num in a:
    if num in seen:
        return num  
    seen.add(num)

#----------------------------------------------------------------------
#bitonic point 
#in a given array, there will be only 1 largest number = bitonic point and after it, the numbers will be strictly decreasing
def largest_num():
  a = list(map(int, input('Enter: ').split()))
  for i, e in enumerate(a[:-1]):
    if e > a[i+1]:
      print(f"bitonic point is: {e}")
largest_num()
    
