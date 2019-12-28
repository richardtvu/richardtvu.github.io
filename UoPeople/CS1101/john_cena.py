John_Cena = True
Does_Charity = True 

def john_cena(John_Cena, Does_Charity):
    if 1 == 1:
        pass
    if John_Cena and Does_Charity:
        print("John Cena does charity.")
    elif John_Cena and not (Does_Charity):
        print("John Cena does not do charity.")
    elif not (John_Cena) and Does_Charity:
        print("Someone that is not John Cena does charity.")
    elif not (John_Cena) and not(Does_Charity):
        print("Someone that is not John Cena does not do charity.")
    else:
        print("We aren't talking about charity anymore. But hey, that doesn't matter because this option will never be fulfilled.")



john_cena(John_Cena, Does_Charity)
john_cena(False, True)
john_cena(False, False)
john_cena(True, False)



print("Which causes do you think John Cena supports? You may answer by inputting a, b, c, d, e, or f as value for option in john_cena_chained(option).")
print("a. cancer")
print("b. children")
print("c. grief support")
print("d. health")
print("e. all of the above")
print("f. none of the above.")

a = "a. \"cancer.\""
b = "b. \"children.\""
c = "c. \"grief support.\""
d = "d. \"health.\""
e = "e. \"all of the above.\""
f = "f. \"none of the above.\""

def john_cena_chained(option):
    "Takes the input 'a, b, c, d, e, or f' and returns a message stating whether the user is correct or incorrect."
    # Draw attention to response and print option chosen by user.
    print("---------------------------------")
    print("|       Response Chosen         |")
    print("---------------------------------")
    print("    " + option)
    # Evaluate option chosen and print appropriate response.
    if option == a:
        print("You've got part of the answer right. Try again :)!.")
    elif option == b:
        print("You get 25% credit. Try again.")
    elif option == c:
        print("Your answer is one-fourth correct. Try again.")
    elif option == d:
        print("He does do charity work in the health field, but he also does other things too. Try again.")
    elif option == e:
        print("Ding ding ding! We have a winner!")
        print("It turns out that John does all of the above!" + "(John Cena: Charity Work, Events, and Causes,\" n.d.). John Cena is most known for his contributions to the *Make a Wish* foundation, through which he\'s granted more than 580 wishes for children with terminal cancer (Blynn, 2018).")
    else:
        print("Sorry, that's wrong. Try again.")

## Answer?
john_cena_chained(e)

## Question
print(" --------------------------------------------------")
question_part_one = "Which causes do you think John Cena supports? "
question_part_two = " You may answer by inputting your answer into john_cena_nested(option_one, option_two, option_three, option_four, option_five."
question_part_three = " If you think an option is true, put True for that argument."
question_part_four = " For instance, if you think John Cena only supports cancer, answer john_cena_nested(True, False, False, False, False)."
print(question_part_one + question_part_two + question_part_three + question_part_four)
print(" --------------------------------------------------")


## Options
option1 = "a. \"cancer.\""
option2 = "b. \"children.\""
option3 = "c. \"grief support.\""
option4 = "d. \"health.\""
option5 = "e. \"none of the above.\""
print(option1)
print(option2)
print(option3)
print(option4)
print(option5)

## Define function that takes multiple conditions and choose appropriate response using nested conditionals.
def john_cena_nested(option1, option2, option3, option4, option5):
    "A multiple-choice question that takes multiple answers and selects an appropriate response."
    ## Draw attention to response and print option(s) chosen by user.
    print(" --------------------------------------------------")
    print("|       Let's see if you got the right answer!     |")
    print(" --------------------------------------------------")
    if option1 == True:
        if option2 == True:
            if option3 == True:
                if option4 == True:
                    if option5 == False:
                        print("You chose a, b, c, and d.")
                        print("Ding ding ding! We have a winner!")
                        print("It turns out that John does all of the above!" + "(John Cena: Charity Work, Events, and Causes,\" n.d.). John Cena is most known for his contributions to the *Make a Wish* foundation, through which he\'s granted more than 580 wishes for children with terminal cancer (Blynn, 2018).")
                    else:
                        print("No... you can't select all of the above and none of the above at the same time.")
                else: 
                    print("You've got three correct answers! One more left.")
            else:
                print("You got two out of the four correct answers!")
        else:
            print("You got one out of the four correct answers!")
    else:
        print("There are four answers that are correct. You get 0% credit.")
        
john_cena_nested(True, True, True, True, False)
