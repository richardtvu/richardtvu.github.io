#------Learning Journal #4 Part 2 - Creating a Useful Program of My Choice------#
#          Creation of a Study Hours Function and Schedule Creator              #
#-------------------------------------------------------------------------------#
"""
The purpose of this function is to return the number of available hours per day
that I can allocate to studying, given a basic set of needs/non-negotiables, such
as sleep, work, hygiene, journaling, walking, reading, and eating. 

The program will ask the user for the number of hours necessary for each activity
via the user input command and then take the total, subtract it from the hours in
a day, and obtain the available hours for study time.

If time permits, then development of features, such as rank-ordering of non-
negotiables and activities by importance and suggested schedules, may take place.

Parameters of interest:
- Sleep
- Work
- Meals
- Journal
- Hygiene
- Exercise
- Non-Productive Time
- Reading
- Study

Code/functions that may be necessary:
- If, elif, else
- Try, except
- User input
- Recursion
- Turtles:
Drawing, turtle to visualize the daily schedule in a rectangular format where
each section that is shaded represents a half hour?
""" 

# Begin with outline of definition 
def study_hours():
    return 0.0

# Ask for user input and display user input
def study_hours():
    user_input = input("How many hours do you need to/would like to dedicate to sleep? \n")
    print(user_input)

"""
test input:
study_hours()

test output:
How many hours do you need to/would like to dedicate to sleep? 
10
10
"""

# Define function that will simplify process of obtaining user input for parameters
def user_input(parameter):
    """
    Ask user how many hours they want to dedicate to a certain activity and assigns
    it to the variable commitment
    """
    commitment = input("Input many hours would you like to commit to: " + parameter + ".\n")
    return int(commitment)

"""
test input:
sleep = user_input("sleep")
print("sleep")

test output:
Input many hours would you like to commit to: sleep.
10
10
""" 

# Inclusion of guardian conditional to prevent non-numerical inputs and negative inputs
# based on examples from Pynative (2019) and "Python Try Except" (n.d.). 
def user_input(parameter):
    """
    Ask user how many hours they want to dedicate to a certain activity and assigns
    it to the variable commitment.
    """
    commitment = input("Input many hours would you like to commit to: " + parameter + ".\n")
    try: 
        commitment = float(commitment)
        if commitment >= 0 and commitment <= 24:
            print("You've elected to dedicate", commitment, "hours to", parameter)
            print("")
            return commitment
        else:
            print("You can't commit less than 0 hours or more than 24 hours to an activity. Try again.")
            print("")
            return user_input(parameter)
    except ValueError:
        print("You didn't input a number. To make this work, you need to input something like '10' to represent 10 hours. Let's try again")
        print("")
        return user_input(parameter)


"""
test input:
sleep = user_input("sleep")
print(sleep)

test output:
Input many hours would you like to commit to: sleep.
ten
You didn't input a number. To make this work, you need to input something like '10' without the quotes to represent 10 hours. Let's try again

Input many hours would you like to commit to: sleep.
-10
You can't commit less than 0 hours to an activity. Try again.

Input many hours would you like to commit to: sleep.
10
10.0 

Input many hours would you like to commit to: sleep.
25
You can't commit less than 0 hours or more than 24 hours to an activity. Try again.

Input many hours would you like to commit to: sleep.
24
24.0
"""


# Include user_input function in study_hours funtion
def study_hours():
    sleep = user_input("sleep")
    return(sleep)

"""
test input: 
sleep = study_hours()
print(sleep)

test output:
Input many hours would you like to commit to: sleep.
24
24.0
"""

# Repeat process of requesting and displaying user input for all parameters and
# display total hours commited to each activity 
def study_hours():
    sleep = user_input("sleep")
    work = user_input("work")
    sustenance = user_input("sustenance")
    journaling = user_input("journaling")
    hygiene = user_input("hygiene")
    exercise = user_input("exercise")
    non_prod_time = user_input("non-productive time")
    reading = user_input("reading")
    total = sleep + work + sustenance + journaling + hygiene + exercise + non_prod_time + reading
    print(total)
    return total

"""
test input:
study_hours()

test output:
Input many hours would you like to commit to: sleep.
10
You've elected to dedicate 10.0 hours to sleep

Input many hours would you like to commit to: work.
9
You've elected to dedicate 9.0 hours to work

Input many hours would you like to commit to: sustenance.
1
You've elected to dedicate 1.0 hours to sustenance

Input many hours would you like to commit to: journaling.
1
You've elected to dedicate 1.0 hours to journaling

Input many hours would you like to commit to: hygiene.
1
You've elected to dedicate 1.0 hours to hygiene

Input many hours would you like to commit to: exercise.
1
You've elected to dedicate 1.0 hours to exercise

Input many hours would you like to commit to: non-productive time.
0
You've elected to dedicate 0.0 hours to non-productive time

Input many hours would you like to commit to: reading.
1
You've elected to dedicate 1.0 hours to reading

24.0
"""

# Subtract sum of parameters from hours in a day and return the result

def study_hours():
    potential_hours = 24
    sleep = user_input("sleep")
    work = user_input("work")
    sustenance = user_input("sustenance")
    journaling = user_input("journaling")
    hygiene = user_input("hygiene")
    exercise = user_input("exercise")
    non_prod_time = user_input("non-productive time")
    reading = user_input("reading")
    total_commitments = sleep + work + sustenance + journaling + hygiene + exercise + non_prod_time + reading
    avail_study_hours = potential_hours - total_commitments
    print("You have", avail_study_hours, "hours available for studying.")
    return avail_study_hours

"""
test_input:
study_hours()

test_output:
Input many hours would you like to commit to: sleep.
11
You've elected to dedicate 11.0 hours to sleep

Input many hours would you like to commit to: work.
8
You've elected to dedicate 8.0 hours to work

Input many hours would you like to commit to: sustenance.
0.5
You've elected to dedicate 0.5 hours to sustenance

Input many hours would you like to commit to: journaling.
0.75
You've elected to dedicate 0.75 hours to journaling

Input many hours would you like to commit to: hygiene.
0.75
You've elected to dedicate 0.75 hours to hygiene

Input many hours would you like to commit to: exercise.
1.25
You've elected to dedicate 1.25 hours to exercise

Input many hours would you like to commit to: non-productive time.
0
You've elected to dedicate 0.0 hours to non-productive time

Input many hours would you like to commit to: reading.
1
You've elected to dedicate 1.0 hours to reading

You have 0.75 hours available for studying.
"""

# Making the program more concise in output by deleting unnecessary print statements:
def user_input(parameter):
    """
    Ask user how many hours they want to dedicate to a certain activity and assigns
    it to the variable commitment.
    """
    commitment = input("Input many hours would you like to commit to: " + parameter + ".\n")
    try: 
        commitment = float(commitment)
        if commitment >= 0 and commitment <= 24:
            return commitment
        else:
            print("You can't commit less than 0 hours or more than 24 hours to an activity. Try again.")
            print("")
            return user_input(parameter)
    except ValueError:
        print("You didn't input a number. To make this work, you need to input something like '10' to represent 10 hours. Let's try again")
        print("")
        return user_input(parameter)

def study_hours():
    potential_hours = 24
    sleep = user_input("sleep")
    work = user_input("work")
    sustenance = user_input("sustenance")
    journaling = user_input("journaling")
    hygiene = user_input("hygiene")
    exercise = user_input("exercise")
    non_prod_time = user_input("non-productive time")
    reading = user_input("reading")
    total_commitments = sleep + work + sustenance + journaling + hygiene + exercise + non_prod_time + reading
    avail_study_hours = potential_hours - total_commitments
    # Kept this print statement because the equivalent return statement is not aesthetically pleasing to me. 
    print ("You have", avail_study_hours, "hours available for studying.") 
    return avail_study_hours


"""
test input:
avail_study_hours = study_hours()

test output:
Input many hours would you like to commit to: sleep.
10.5
Input many hours would you like to commit to: work.
8
Input many hours would you like to commit to: sustenance.
0.25
Input many hours would you like to commit to: journaling.
0.5
Input many hours would you like to commit to: hygiene.
0.75
Input many hours would you like to commit to: exercise.
1.25
Input many hours would you like to commit to: non-productive time.
0
Input many hours would you like to commit to: reading.
0.5
You have 2.25 hours available for studying.
"""



## ------------------------------- Stretch Goal------------------------------ ##

# Add a turtle object
import math 
import turtle

stud = turtle.Turtle()

# The following code snippet taken from Downey (2015):
def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)

stud.pu()
stud.bk(300)
stud.rt(90)
stud.fd(225)
stud.lt(90)
stud.pd()

square(stud, 500)

# Draw the dividers. 
##stud.fd(length/2)
##stud.lt(90)
##stud.fd(length)
##stud.lt(90)
##stud.fd(length/2)
##stud.lt(90)
##stud.fd(length)

# It looks like I made a variant of Xeno's paradox haha! 
def vertical_dividers(t, length, n): 
    x_distance = length/n
    for i in range(2):
        t.fd(x_distance)
        t.lt(90)
        t.fd(length)
        t.lt(90)
    n = n +1
    for i in range(4):
        vertical_dividers(t, length, n)

vertical_dividers(stud, 500, 1)



# Have turtle draw out one large square 
# Have turtle draw out eight by eight square, where each square represents 0.5 h

# Is it possible to get a list of inputs to make the code even more concise? 
##------------------------------- References ------------------------------- ##
"""
Downey, A.B. (2015). Think Python: How to Think Like a Computer Scientist. Retrieved from https://greenteapress.com/thinkpython2/html/index.html
Pynative. (2019, July 14). "How to check user input is a number or string in Python?" Retrieved July 17, 2019 from https://pynative.com/python-check-user-input-is-number-or-string/
"Python Try Except" (n.d.). Retrieved July 17, 2019 from https://www.w3schools.com/python/python_try_except.asp


"""
