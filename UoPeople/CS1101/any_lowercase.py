def any_lowercase4(s): 
    flag = False
    for c in s: 
        flag = flag or c.islower()
    return flag 

# Modify variable names to be more descriptive. Add in commentary.  

def any_lowercase4(word):
    """
    - Returns a True or False to the question of whether the inputted word has any lower case letters.
    - Sets the default state of the answer to be false.
    - Evaluates each letter in the parameter, word and determines if the previous answer or the letter is lowercase. If either are true, then it sets the answer state to be True.
    - Once the answer state becomes True, it will be true for the rest of the loop because of the "or" operator, which means that only one part of the condition has to be fulfilled for the entire condition is True.
    - At the end, the program returns the value of the answer, which will be True if at anytime there was a lowercase letter in the word and False otherwise.
    """
    # Set the default answer to be false.
    answer = False
    for letter in word:
        print("Letter: " + letter + ". Is this a lowercase letter? " + str(letter.islower()) + " Updated answer:", answer or letter.islower())
        answer = (answer or letter.islower())
    print("Are there any lowercase letters in " + word + "? ")
    return answer

# Check out anylowercase 5
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


def any_lowercase6(s):
    for c in s:
        if c.islower():
            return True
    return False
print(any_lowercase6("John"))
print(any_lowercase6("JASIDOJSAIDOJOIASJDIASLD"))
print(any_lowercase6("jacoPo"))
