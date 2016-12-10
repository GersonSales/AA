def factorial(number):
    if (number <= 1): 
        return 1
    return number * factorial(number - 1)

try:
    while 1: 
        m, n = map(int, raw_input().split())
        print factorial(m) + factorial(n)
except EOFError:
    pass    

