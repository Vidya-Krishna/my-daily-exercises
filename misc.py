



#--------------------------------------------------
import time
start_time_one = time.time()
j = 0
for i in range(1000000001): j += 1
end_time_one = time.time()
value_one = (end_time_one - start_time_one)
print(f"j += 1 takes {value_one}s")

start_time_two = time.time()
k = 0
for i in range(1000000001): k = k+1 
value_two = (time.time() - start_time_two)
print(f"j = j+1 takes {value_two}s")

print(value_two - value_one)
"""
for a billion operations,
j += 1 takes 34.601717948913574s
j = j+1 takes 39.37363386154175s
4.771915912628174
"""

#--------------------------------------------------
