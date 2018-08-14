# Get the square root of a number

# The multiply approach
def SquareRoot(n):
    k = 1.0
    while((k*k - n) > 0.0000000001 or (n - k * k) > 0.0000000001):
        k = (k + n / k) / 2 
    return k

# Binary search approach
def SquareRoot2(n):

    if n == 0 or n == 1:
        return n

    low = 0
    high = n
    oldmid = 0
    mid = n
    while oldmid - mid > 0.0000000001 or mid - oldmid > 0.0000000001:
        oldmid = mid
        mid = (low + high) / 2
        if mid * mid > n:
            high = mid
        elif mid * mid < n:
            low = mid
        else:
            return mid

    return mid
