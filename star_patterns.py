# PATTERN: RIGHT ANGLE STAR
# *
# **
# ***
# ****
n = int(input("Enter number of rows: "))
def rightangle_pattern():
    star = "*"
    for i in range(n):
        print(star)
        star+= "*"
rightangle_pattern()

def pattern(n):
    for i in range(1, n+1):
        print("*" * i)

n = int(input("Enter number of rows: "))
pattern(n)
#————————————————————————————————————————————————————————
# PATTERN
# *
# **
# ***
# ****
# *****
# ******
# *******
# *******
# ******
# *****
# ****
# ***
# **
# *
n = int(input("Enter number of rows: "))

def star_symmetry(n, star="*"):
    for i in range(n):
        print(star)
        star += "*"
    count = len(star)-1
    for j in range(count, 0, -1):
        star = star[:count]
        print(star)
        count -= 1

star_symmetry(n)
#————————————————————————————————————————————————————————
#RECTANGLE STAR PATTERN
#****
#****
#****
#****
r = int(input("Enter number of rows : "))

def star_rectangle(r, star = "*"):
    for i in range(r):
        for j in range(r):
            print(star, end="")
        print("")
    
star_rectangle(r)
#————————————————————————————————————————————————————————
#PATTERN 
#*
#**
#***
#***
#**
#*
b = "*"

def pattern(b):
    a = 3#
    for i in range(a):
        print(b)
        b+= "*"
        c = b
    for rev_count in range(len(c)):
        rev_count += 1
        print(c[:-rev_count])
pattern(b)
# ———————
