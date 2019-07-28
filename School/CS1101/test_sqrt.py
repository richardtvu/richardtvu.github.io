# -------------------------------------------- Final Product ---------------------------------------------------# 
# Run with Python Window maximized for full aesthetic experience.
import math

def my_sqrt(a):
    """
    In general:
    Takes number, a, that you want the square root of, and an estimate,
    x, and outputs the closest approximation to the true square root that can be
    found via Newton's algorithm.

    Specifically: 
    Takes argument a, the value you want to take a square root of, and x, the first
    estimate you have for the square root. Evaluates x and a according to Newton's
    algorithm for finding square roots (Downey, 2015), updates the estimate to a
    closer approximation, and checks if the approximation provided by the algorithm
    is equivalent to the last approximation. If true, stop the program and move on
    to the next statement. Otherwise, continue the loop. 
    """
    # Initializes x and sets the estimate as half of a. 
    x = a/2
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
    # Returns final value of x. 
    return x

def sqrt_table_header():
    print(" ")
    print(" ")
    print("                                         Square Roots Table                                          ")
    print("-----------------------------------------------------------------------------------------------------")          
    print("  a              my.sqrt(a)                       math.sqrt(a)                        diff")
    print("------  -----------------------------   --------------------------------   --------------------------")


def test_guardian(a):
    # Prevents non-integers from being entered and errors from arising due to non-integer input. 
    if type(a) != int:
        print("Non-integers aren't accepted. Use a positive integer.")
        a = input("What positive integer do you want to find the square root of? \n")     
        try: 
            a = int(a)
            return test_guardian(a)
        except:
            print("That's not an integer. Try again.")
            print(" ")
            return test_guardian(a)
    # Prevents non-positive integers from being entered. 
    while a <=0:
        print(" ")
        print("This function is only defined for positive integers (i.e. integers above 0). ")
        a = input("What number do you want to input for a? E.g. '25' \n")
        a = int(a)
    # Maintains format of table by preventing inputs larger than 99
    if a > 99:
        print("This function is only defined for integers up to 99")
        print("a will be set to 99.")
        a = 99
        return a
    return a


def test_sqrt(a):
    a = test_guardian(a)
    sqrt_table_header()
    n = 1
    # Prints values from 1 to a. 
    while n <= a and a > 0:
        my_spaces = (18 - len(str(my_sqrt(n)))) * " "
        math_spaces = (18 - len(str(math.sqrt(n)))) * " "
        diff = abs(math.sqrt(n) - my_sqrt(n))
        # Have two branches for formatting of table 
        if n < 10:
            # Take the absolute value of the difference between math.sqrt(a) and my.sqrt(a)
            # Ensure that my.sqrt(a) and math.sqrt(a) are printed on same line with a end = "" attribute
            print("a = 0" + str(n) + " my.sqrt(a) = " + str(my_sqrt(n)) + my_spaces, end = "")
            print(" math.sqrt(a) = " + str(math.sqrt(n)) + math_spaces, end = " ")
            print(" diff = " + str(diff))
        if n >= 10:
            print("a = " + str(n) + " my.sqrt(a) = " + str(my_sqrt(n)) + my_spaces, end = "")
            print(" math.sqrt(a) = " + str(math.sqrt(n)) + math_spaces, end = " ")
            print(" diff = " + str(diff))
        # Updates n by an increment of 1
        n += 1
    return(a)


test_sqrt(25)

## Output
"""
 
                                         Square Roots Table                                          
-----------------------------------------------------------------------------------------------------
  a              my.sqrt(a)                       math.sqrt(a)                        diff
------  -----------------------------   --------------------------------   --------------------------
a = 01 my.sqrt(a) = 1.0                math.sqrt(a) = 1.0                 diff = 0.0
a = 02 my.sqrt(a) = 1.414213562373095  math.sqrt(a) = 1.4142135623730951  diff = 2.220446049250313e-16
a = 03 my.sqrt(a) = 1.7320508075688772 math.sqrt(a) = 1.7320508075688772  diff = 0.0
a = 04 my.sqrt(a) = 2.0                math.sqrt(a) = 2.0                 diff = 0.0
a = 05 my.sqrt(a) = 2.23606797749979   math.sqrt(a) = 2.23606797749979    diff = 0.0
a = 06 my.sqrt(a) = 2.449489742783178  math.sqrt(a) = 2.449489742783178   diff = 0.0
a = 07 my.sqrt(a) = 2.6457513110645907 math.sqrt(a) = 2.6457513110645907  diff = 0.0
a = 08 my.sqrt(a) = 2.82842712474619   math.sqrt(a) = 2.8284271247461903  diff = 4.440892098500626e-16
a = 09 my.sqrt(a) = 3.0                math.sqrt(a) = 3.0                 diff = 0.0
a = 10 my.sqrt(a) = 3.162277660168379  math.sqrt(a) = 3.1622776601683795  diff = 4.440892098500626e-16
a = 11 my.sqrt(a) = 3.3166247903554    math.sqrt(a) = 3.3166247903554     diff = 0.0
a = 12 my.sqrt(a) = 3.4641016151377544 math.sqrt(a) = 3.4641016151377544  diff = 0.0
a = 13 my.sqrt(a) = 3.6055512754639896 math.sqrt(a) = 3.605551275463989   diff = 4.440892098500626e-16
a = 14 my.sqrt(a) = 3.7416573867739413 math.sqrt(a) = 3.7416573867739413  diff = 0.0
a = 15 my.sqrt(a) = 3.872983346207417  math.sqrt(a) = 3.872983346207417   diff = 0.0
a = 16 my.sqrt(a) = 4.0                math.sqrt(a) = 4.0                 diff = 0.0
a = 17 my.sqrt(a) = 4.123105625617661  math.sqrt(a) = 4.123105625617661   diff = 0.0
a = 18 my.sqrt(a) = 4.242640687119286  math.sqrt(a) = 4.242640687119285   diff = 8.881784197001252e-16
a = 19 my.sqrt(a) = 4.358898943540673  math.sqrt(a) = 4.358898943540674   diff = 8.881784197001252e-16
a = 20 my.sqrt(a) = 4.47213595499958   math.sqrt(a) = 4.47213595499958    diff = 0.0
a = 21 my.sqrt(a) = 4.58257569495584   math.sqrt(a) = 4.58257569495584    diff = 0.0
a = 22 my.sqrt(a) = 4.69041575982343   math.sqrt(a) = 4.69041575982343    diff = 0.0
a = 23 my.sqrt(a) = 4.795831523312719  math.sqrt(a) = 4.795831523312719   diff = 0.0
a = 24 my.sqrt(a) = 4.898979485566356  math.sqrt(a) = 4.898979485566356   diff = 0.0
a = 25 my.sqrt(a) = 5.0                math.sqrt(a) = 5.0                 diff = 0.0
"""


