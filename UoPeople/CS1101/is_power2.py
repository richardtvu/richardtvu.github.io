#-----------------------------Section 6.11 Exercise 4-------------------------#
# Create a function is_power that takes arguments a and b and returns true if #
# a is a power of b. Note: You have to think about the base case.             #
#-----------------------------------------------------------------------------#      
"""
A number, a, is a power of 2, if after repeatedly dividing the
number by 2, the quotient becomes 1 (Regan, 2009) ...
That is, 32 is a power of 2, because if you divide it 5 times by 2...
32/2 = 16, 16/2 = 8, 8/2 = 4, 4/2 = 2, 2/2 = 1, then you'll reach 1. 

Therefore, a is a power of b, if after repeatedly dividing the number by b,
the quotient becomes 1. However, if after repeatedly dividing by b, there is a
remainder greater than 0, not 1, and less than b, then a is not a power of b.

a is a power of b if:
    a % b == 0 and (a/b) is a power of b

"""

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_power(a,b):
    """
    Takes two inputs, a and b, and determines if input a is a power of b. That is if b is taken to a certain power, b^n, whether the result can be input a.
    Prevents negative numbers from being input and only goes into recursion if b is greater than one to avoid infinite recursion.
    """
    if a <= 0 or b <= 0:
        return "This program is only defined for integers above 0."
    elif (a/b) <= b:
        return is_divisible(a,b)
    elif  (a/b) % b == 0 and b > 1:
        return is_power(a/b, b)
    return False

print("is_power(10, 2)      returns: ", is_power(10, 2))      # False
print("is_power(27, 3)      returns: ", is_power(27, 3))      # True 
print("is_power(1, 1)       returns: ", is_power(1, 1))       # True
print("is_power(3, 3)       returns: ", is_power(3, 3))       # True
print("is_power(10, 1)      returns: ", is_power(10, 1))      # False
print("is_power(-10, 10.0)  returns: ", is_power(-10, 10.0))  # This program is only defined for integers above 0.
print("is_power(10.0, 10.0) returns: ", is_power(10.0, 10.0)) # True


## Output

## References
"""
Regan, R. (2009, January 18). "Ten Ways to Check if an Integer is a Power of Two
in C". Retrieved from https://www.exploringbinary.com/ten-ways-to-check-if-an-integer-is-a-power-of-two-in-c/
"""
