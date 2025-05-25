# calci - just to make myself comfortable with case/ f'n, return / basic for/while, if/else

def add(a: float, b: float) -> float: return a + b

def sub(a: float, b: float) -> float: return(a-b if a > b else b-a)

def mul(a: float, b: float) -> float: return a * b

def modul(a: float, b: float) -> float: 
    return a % b

def division(a: float, b: float) -> float | str:
    return ('invalid, b cannot be 0' if b == 0 else a/b)

def power(a: float, b: float) -> float: return a ** b

toggle = True
while toggle:
    while True:
        x = input("""Select & enter from below:
            + for addition, 
            - for subtraction, 
            * for multiplication, 
            % for modulo, 
            / for division, 
            ** for power, 
            'q' to quit: """)
        if x in ('+', '-', '*', '%', '/', '**', 'q'):
            if x != 'q':
                a = float(input('enter a: '))
                b = float(input('enter b: '))
                break
            else:
                break
        else :
            print('invalid input')

    match x:
        case '+': print(add(a, b))
        case '-': print(sub(a, b))
        case '*': print(mul(a, b))
        case '%': print(modul(a, b))
        case '/': print(division(a, b))
        case '**': print(power(a, b))
        case 'q' : toggle = False
