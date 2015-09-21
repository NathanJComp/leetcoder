import math
def reverse(x):
    if x<0:
        rev=0
        x*=-1
        for i in range(int(math.log10(x)),-1,-1):
            rev+=(x%10)*10**i
            x//=10
        rev*=-1
        return rev if rev > -(2**31) else 0
    rev=0
    for i in range(int(math.log10(x)),-1,-1):
        rev+=(x%10)*10**i
        x//=10
    return rev if rev<2**31-1 else 0

print(reverse(-123))