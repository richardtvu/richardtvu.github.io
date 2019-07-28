# Section 8.7 Looping and counting 



# Modify function to use find: What am I trying to get with count and find?
# I think that I'd still be trying to get the # of letters of interest
# Okay, let's do that: Modify count to use find, and use the resulting
# index in the counter? So if the returned value != -1, then keep counting
# from that 
def find(word, letter, index):
    while index < len(word): 
        if word[index] == letter:
            return index
        index = index + 1
    return -1 



def count(word, letter_of_interest, index):
    count = 0 
    while index<len(word):
        print(index)
        index = find(word, letter_of_interest, index)
        print(index)
        count = count + 1
        print(count)
        return find(word, letter_of_interest, index) and count
    print(count)
    return count 

count("Lovely Bones are lovely ", "l", 0)
