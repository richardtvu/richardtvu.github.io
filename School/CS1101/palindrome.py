#------------------------- Palindrome Exercise -------------------------------#
"""
A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last
letters are the same and the middle is a palindrome.
e.g. The letter "a"
e.g. "racecar"
e.g. "yay"
"""
# Palindrome Functionss

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


## Call function, middle, with a string with two letters, one letter, and empty
## string. 

# Call middle with a string two letters or less in size returns an empty string
print(middle("ab"))
print(middle("a"))
print(middle(""))

## Write a function called is_palindrome that takes a string argument and returns
## True if it is a palindrome and False otherwise. You can use len to check
## the length of a string. 

# Incremental development:
# Begin with an outline of the function
def is_palindrome(word): 
    return "Output"

# Add code to obtain the first letters of the word
def is_palindrome(word):
    length = len(word)
    print(length)
    return "Output"

# Add code for one-letter word, which is automatically a palindrome. 
def is_palindrome(word):
    length = len(word)
    print("Input:", word)
    print("Is this word a palindrome?")
    if length <= 1:
        print("True")
    return "----------"

# Add code for two-letter words:
def is_palindrome(word):
    length = len(word)
    print("Input:", word)
    print("Is this word a palindrome?")
    if length <= 1:
        print("True")
    elif length == 2 and first(word) == last(word):
        print("Yes, it's a palindrome.")
    elif length == 2 and not (first(word) == last(word)):
        print("No, it's not a palindrome")
    return "----------"

## Test Cases Passed:
"""
print(is_palindrome("a"))
print(is_palindrome("bb"))
print(is_palindrome("ab"))
print(is_palindrome("racecar"))
"""

# Add code for three letter words and above; print the word with the first and
# last letters taken off:
def is_palindrome(word):
    length = len(word)
    print("Input:", word)
    print("Is this word a palindrome?")
    if length <= 1:
        print("True")
    elif length == 2 and first(word) == last(word):
        print("Yes, it's a palindrome.")
    elif length == 2 and not (first(word) == last(word)):
        print("No, it's not a palindrome")
    elif length >= 3 and first(word) == last(word):
        print(middle(word))
    return "----------"


# Add recursive function call that takes the middle and inputs it back into
# is_palindrome:
def is_palindrome(word):
    length = len(word)
    print("Input:", word)
    print("Is this word a palindrome?")
    if length <= 1:
        print("True")
    elif length == 2 and first(word) == last(word):
        print("Yes, it's a palindrome.")
    elif length == 2 and not (first(word) == last(word)):
        print("No, it's not a palindrome")
    elif length >= 3 and first(word) == last(word):
        middle_word = middle(word)
        print(middle_word)
        is_palindrome(middle_word)
    return "----------"

# Output of Test Case: racecar
"""
print(is_palindrome("racecar"))
Input: racecar
Is this word a palindrome?
aceca
Input: aceca
Is this word a palindrome?
cec
Input: cec
Is this word a palindrome?
e
Input: e
Is this word a palindrome?
True
"""

## Remove intermediate variables and scaffolding. 
def is_palindrome(word):
    length = len(word)
    if length <= 1:
        print("Yes, it's a palindrome")
    elif length == 2 and first(word) == last(word):
        print("Yes, it's a palindrome.")
    elif length == 2 and not (first(word) == last(word)):
        print("No, it's not a palindrome")
    elif length >= 3 and first(word) == last(word):
        middle_word = middle(word)
        is_palindrome(middle_word)
    return 


## Make function more concise by combining branches 2-4
def is_palindrome(word):
    length = len(word)
    if length == 0 or length == 1:
        print("Yes.")
    elif length >= 2 and first(word) == last(word):
        middle_word=middle(word)
        is_palindrome(middle_word)
    else:
        print("No.")

# Make function even more concise by removing consider of length >=2 and print
# statements. 
def is_palindrome(word):
    length = len(word)

    if length <= 1:
        return "Yes."
    elif first(word) != last(word):
        return "No."
    else:
        middle_word = middle(word)
        return is_palindrome(middle_word)

# Is it possible to make it more concise by removing the else statement? Yes! 
def is_palindrome(word):
    length = len(word)

    if length <= 1:
        return "Yes."
    elif first(word) != last(word):
        return "No."
    middle_word = middle(word)
    return is_palindrome(middle_word)

# Remove the intermediate variable middle_world and "el" from
# elif for the final product! 
def is_palindrome(word):
    length = len(word)
    if length<=1:
        return "Yes."
    if first(word) != last(word):
        return "No."
    return is_palindrome(middle(word))

# Compare to the ThinkPython solution, which was checked after my final product:
def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

## Why return true and false?
"""
I'm not sure, but if it returns True and False, it can be used in other functions
because it returned a boolean value. 
"""
print(is_palindrome("racecar"))
