def is_palindrome(x):
    if x < 0:
        return False

    # check how many digit for x
    digit = 0
    tmp = x

    while(tmp > 0):
        digit += 1
        tmp /= 10
    
    leftMostDigit = digit - 1
    while (x > 0):
        mask = 10 ** leftMostDigit
        leftVal = x / mask
        rightVal = x % 10
    
        if leftVal != rightVal:
            return False
        
        x -= mask * leftVal
        x /= 10
        leftMostDigit -= 2

    return True
