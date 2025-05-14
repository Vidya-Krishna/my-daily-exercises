#Calculator(s)

————————————————————————————————————————————————————————
#order value calculation
stock_name = []
stock_prices = []
value = 0

def order_value(): #Not familiar with args & kwargs
    while True:
        ticker = input("Enter stock ticker symbol / press q to exit: ") #taking input multiple times
        if ticker.lower() == "q":
            break #don't want our machine to break
        else:
            stock_name.append(ticker)
            value = float(input("Enter stock price: ")
            stock_prices.append(value)
order_value()
print(sum(stock_prices))


————————————————————————————————————————————————————————
#Compound Interest Calculator
p = float(input("Enter input > 0: "))
rate = float(input("Enter rate of interest > 0: "))
time = float(input("Enter time in years > 0: "))

def validFloat(p):
    while True:
        if p <= 0:
            p = float(input(f"Enter input {p} > 0: "))
        else:
            break
validFloat(p)
validFloat(rate)
validFloat(time)

# while p <= 0:
#    p = float(input("Enter principle: "))
#    if p <= 0:
#       print("Principle can't be less than or equal to 0 ")

# while rate <= 0:
#    rate = float(input("Enter rate: "))
#    if rate <= 0:
#       print("Rate can't be less than or equal to 0 ")

# while time <= 0:
#    time = int(input("Enter time: "))
#    if time <= 0:
#       print("Time can't be less than or equal to 0 ")
a = p * pow((1 + (rate/100)), time)
print(f"{a:,.2f}")
————————————————————————————————————————————————————————
#Match case
a = float(input("Enter a: "))
b = float(input("Enter b: "))

def add(a, b):
    print(a + b)
def sub(a, b):
    if a>b: 
       print(b-a)
    else:
        print(a - b)
def mul(a, b): print(a * b)
def div(a, b): 
    if b == 0:
        print("Denominator can't be Zero")
    else:
        print (a / b)
def mod(a, b): 
    if b == 0:
        print("Denominator can't be Zero")
    else:
        print (a % b)
def pow(a, b): print(a**b)

x = int(input("Enter 1 for +, 2 for -, 3 for /, 4 for *, 5 for %, 6 for **: "))
match x:
    case 1:
        add(a, b)
    case 2:
        sub(a, b)
    case 3:
        div(a, b)
    case 4:
        mul(a, b)
    case 5:
        mod(a, b)
    case 6:
        pow(a, b)
    case _:
        print("Try Again and choose a valid option")
————————————————————————————————————————————————————————
#if, elif

s = input("Enter + for Addition, - for Substraction, / for Division, * for mutliplication, % for Moudlud or Remainder, ** for Power: ")

while True:
    if s in ("+", "-", "/", "*", "%", "**"):
        break
    print("Invalid input. Try again.")
    s = input("Enter + for Addition, - for Substraction, / for Division, * for mutliplication, % for Moudlud or Remainder, ** for Power: ")

a = float(input("enter int a: "))
b = float(input("enter int b: "))
def add(a, b):
    print(a + b)

def sub(a, b):
    if a>b: 
       print(b-a)
    else:
        print(a - b)
    
def mul(a, b): print(a * b)
def div(a, b): print (a / b)

def mod(a, b): print(a/b)
    
def pow(a, b): print(a**b)
    
if s == "+": add(a, b)
elif s == "-": sub(a, b)
elif s == "*": mul(a, b)
elif s == "/": div(a, b)
elif s == "%": mod(a, b)
elif s == "**": pow(a, b)
————————————————————————————————————————————————————————
