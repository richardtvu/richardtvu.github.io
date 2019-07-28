## Programming Assignment Part 1:
"""
Do Exercise 6.4 from textbook using recursion and the is_divisible function: 
> A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called ```is_power``` that takes parameters a and b and returns True if a is a power of b.
     
# Breaking Down the Programming Assignment
There are two main characteristics that your program has to have in order to
fulfill the requirements for the programming assignment:
1. It has to use recursion.
2. It has to use the is_divisible function. 

1. In this context, "using recursion" means that you should have the is_between
function call itself. What follows is the outline of a recursive is_between
function:

# is_power(a, b) calls itself

```
def is_between(x, y, z):
    is_between(x, y, z)
```

2. The next requirements could then be satisfied by oneof the following:

```
def is_between(x,y,z):
    is_divisible(x, y)
    is_divisible(y, z)
    is_between(x, y, z)
```
"""
