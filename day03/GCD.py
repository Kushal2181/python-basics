import math

def gcd_num(a, b):
    """Returns the GCD of given two numbers"""
    m = min(a, b)
    n = max(a, b)
    gcd = 0

    for i in range(1,m+1):
        if m%i == 0 and n%i == 0:
            gcd = i

    return gcd

print(gcd_num(12,18))



