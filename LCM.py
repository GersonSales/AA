import GCD

def LCM(a, b):
    return  (a * b) / GCD.GCD(a, b)

a, b = map(int, raw_input().split())

print "LCM: %d" %(LCM(a, b))
