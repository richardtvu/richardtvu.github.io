# Section 8.6 Searching

def find(word, letter):
    index = 0 
    while index < len(word): 
        if word[index] == letter:
            return index
        index = index + 1
    return -1 

print(find("Beautiful", "i"))  # Outputs 5, indicating it's the 5th character.

# Modify function to include parameter index, to tell find where to start looking

def find(word, letter, index):
    while index < len(word): 
        if word[index] == letter:
            return index
        index = index + 1
    return -1 

print(find("Beautiful", "i", 5))
