# Programming Exercises for Chapter 2

## Goal

My goal is to do a first-pass through of the exercises, copying the instructions, writing up a first-pass answer like a "minimum viable answer" that meets the criteria, followed by reflections on how I could improve the answer, and then... if I still feel like it, go back and try to implement the thoughts!

## Exercise 2.1

### Instructions

Write a program that will print your initials to standard output in letters that are nine lines tall. Each big letter should be made up of a bunch of *'s. For example, if your initials were "DJE", then the output would look something like:

```
******           *************        **********
**    **                **            **
**     **               **            **
**      **              **            **
**      **              **            ********
**      **       **     **            **
**     **         **    **            **
**    **           **  **             **
*****               ****              **********
```

### Answer(s)

#### First answer

I ended up hard-coding the outputs for each line as a first answer.

```
public class Initials {

    public static void main(String[] args) {

        /*
         * The first method for doing things could be to hard code
         * the letter shapes and use a bunch of System.out.print...
         * I'll try that first. 
         */
        System.out.println("     Printout of my initials, using brute force!"); 
        System.out.println("====================================================");
        System.out.println("********      **************      **              **");
        System.out.println("**    **            **             **            **"); 
        System.out.println("**    **            **              **          **");
        System.out.println("**    **            **               **        **");
        System.out.println("********            **                **      **");
        System.out.println("** **               **                 **    **");
        System.out.println("**  **              **                  **  **");
        System.out.println("**   **             **                   ****");
        System.out.println("**    **            **                    **");

    } // end main()

} // end of class Initials
```

**Output**:

```
Printout of my initials, using brute force!
====================================================
********      **************      **              **
**    **            **             **            **
**    **            **              **          **
**    **            **               **        **
********            **                **      **
** **               **                 **    **
**  **              **                  **  **
**   **             **                   ****
**    **            **                    **
```

**Reflections**

I think the next steps would be for me to create representations for what each letter should look like, so that I can ask the user for their initials and be able to output letters no matter which of the 26 letters they input. Some other features could include:

- A check that users input letters, not symbols or numbers

  - What kind of loop syntax would I use?

- A function to check the space between big letters for uniformity

  - How would I check the space between big letters?

**Post-Solutions Reflection**

- Oh hey, it was pretty similar to the solution suggested! Hurray.

## Exercise 2.2

### 2.2 Instructions

Write a program that simulates rolling a pair of dice. You can simulate rolling one die by choosing one of the integers 1, 2, 3, 4, 5, or 6 at random. The number you pick represents the number on the die after it is rolled. As pointed out in Section 2.5, the expression `(int)(Math.random()*6) + 1`

does the computation to select a random integer between 1 and 6\. You can assign this value to a variable to represent one of the dice that are being rolled. Do this twice and add the results together to get the total roll. Your program should report the number showing on each die as well as the total roll. For example:

```
The first die comes up 3
The second die comes up 5
Your total roll is 8
```

### Answer(s)

#### Code

```java
package programmingExercises;

public class Dice {

    public static void main(String[] args) {

        int firstDice;     // Declare a variable of type int for the first die.
        int secondDice;     // Declare a variable of type int for the second die. 

        // Roll dice
        firstDice = rollDice();
        System.out.print("The first die comes up ");
        System.out.println(firstDice); 

        secondDice = rollDice(); 
        System.out.println("The second die comes up "
                + secondDice); 
        // Sum the die 
        int total;         // Variable of type int to hold sum of two die
        total = firstDice + secondDice;

        // Display the total
        System.out.print("Your total roll is "); 
        System.out.println(total); 
    }

    /* Create a dice roll method */
    public static int rollDice() {
        int dice; 
        dice = (int)(Math.random()*6) + 1; 
        return dice; 
    }
}
```

#### Output

```
The first die comes up 6
The second die comes up 6
Your total roll is 12
```

### Reflections

I saw that I'd be copy and pasting `(int)(Math.random()*6) + 1`, so I decided to make it a function instead. I'm not sure if I saved time, but I think I could have made it better by ... Maybe I could refactor it, and make a function out of the die summing, followed by another function to call the dice roller, the dice summer, and then display the total. I'm not sure what I could do to improve this, I'll probably check out the solution later.

**Post-Solutions Reflection**

- The variable names were simpler in the solutions, i.e. `die1`, `die2`, `roll`, instead of `firstDice` or `secondDice` or `total`.

## Exercise 2.3

### 2.3 Instructions

Write a program that asks the user's name, and then greets the user by name. Before outputting the user's name, convert it to upper case letters. For example, if the user's name is Fred, then the program should respond "Hello, FRED, nice to meet you!".

### 2.3 Answer(s)

#### 2.3 First Answer

#### 2.3 Code

```java
import textio.*;

public class HelloUser {

    public static void main(String[] args) {

        // ask for user's name
        System.out.print("What's your name?    ");
        String name = TextIO.getlnString();

        // convert user's input to all capital letters
        name = name.toUpperCase();

        // display a greeting
        System.out.println("Hello, "
                + name + ", nice to meet you!");

    }
}
```

#### 2.3 Output

```java
What's your name?    Rich
Hello, RICH, nice to meet you!
```

### 2.3 Reflections

I thought it was pretty straight forward. I wonder how I'd get the user's input without using the `TextIO` class though? I could make it better by:

- Using the built-in scanner class.
- Checking the user's input to take out white spaces and carriage returns? Not sure about this.
- Asking for a first, last, and middle name?

## Exercise 2.4

### 2.4 Instructions

Write a program that helps the user count his change. The program should ask how many quarters the user has, then how many dimes, then how many nickels, then how many pennies. Then the program should tell the user how much money he has, expressed in dollars.

### 2.4 Answer(s)

#### 2.4 First Answer

##### 2.4 Code

```java
package programmingExercises;

import textio.*;

/** Exercise 2.4
 * This program will help count the change of a user.
 * It will ask for the # of quarters, dimes, nickels, 
 * and pennies the user possesses. Then, it'll sum 
 * the value and print the total in dollars. 
 * http://math.hws.edu/javanotes/c2/exercises.html
 */
public class ChangeCounter {

    public static void main(String[] args) {

        // Ask for the # of quarters
        System.out.print("How many quarters do you have? ");
        int quarters = TextIO.getlnInt();

        // Ask for the # of dimes
        System.out.print("How many dimes do you have? ");
        int dimes = TextIO.getlnInt(); 

        // Ask for the # of nickels
        System.out.print("How many nickels do you have? ");
        int nickels = TextIO.getlnInt(); 

        // Ask for the # of pennies 
        System.out.print("How many pennies do you have? ");
        int pennies = TextIO.getlnInt(); 

        // Total the amount 
        double total = quarters * 25 + dimes * 10 + nickels * 5 + pennies; 


        System.out.println("You said you have: "); 
        System.out.println("Quarters: " + quarters);
        System.out.println("Dimes: " + dimes); 
        System.out.println("Nickels: " + nickels); 
        System.out.println("Pennies: " + pennies); 
        System.out.println("Total # of pennies: " + (int)(total) + "\n");

        System.out.printf("You have $%1.2f", total/100); 


        // Display dollars 

    }

}
```

##### 2.4 Output

```
How many quarters do you have? 1237
How many dimes do you have? 4843
How many nickels do you have? 38345
How many pennies do you have? 9
You said you have: 
Quarters: 1237
Dimes: 4843
Nickels: 38345
Pennies: 9
Total # of pennies: 271089

You have $2710.89
```

### 2.4 Reflections

- I learned that floor division will give you the whole number and the floor modulus will give the remainder (?). I also learned i could skip out on that....

- The solution:

  - declares the variables used at the top
  - groups the variables for the user's input together
  - has a comment for asking the user for their input, a comment for calculating the value of coins, and a comment for displaying the result

## Exercise 2.5

### 2.5 Instructions

If you have N eggs, then you have N/12 dozen eggs, with N%12 eggs left over. (This is essentially the definition of the / and % operators for integers.) Write a program that asks the user how many eggs she has and then tells the user how many dozen eggs she has and how many extra eggs are left over.

A gross of eggs is equal to 144 eggs. Extend your program so that it will tell the user how many gross, how many dozen, and how many left over eggs she has. For example, if the user says that she has 1342 eggs, then your program would respond with

`Your number of eggs is 9 gross, 3 dozen, and 10`

since 1342 is equal to 9_144 + 3_12 + 10.

### 2.5 Answer(s)

#### 2.5 Code

```java
package programmingExercises;

import textio.*;

public class LeftoverEggs {

    public static void main(String[] args) {

        /* Ask user how many eggs she has */ 
        System.out.print("How many eggs do you have? "); 
        int total = TextIO.getlnInt(); 

        /* Calculate gross, dozen, and remaining eggs */ 
        int gross = total/144;
        int remaining = total%144;

        int dozen = remaining/12; 
        remaining = remaining%12;

        System.out.println("Your number of eggs is " + gross 
                + " gross, " + dozen + " dozen, and "
                        + remaining + "."); 

    }
}
```

#### 2.5 Output

```
How many eggs do you have? 1342
Your number of eggs is 9 gross, 3 dozen, and 10.
```

### 2.5 Reflections

I'm tired...

**Post-solution Reflections**

- Again, a major difference is that his variables are defined at the top of the main routine. He also has some pretty descriptive comments on how the extra number of eggs are calculated. 
- I'll try to re-write my program, so that:
	- The variables are defined at the top of the main routine, so that I'm using the variables eggs, dozen, gross, and extras because they're more descriptive. 


## Exercise 2.6

### Instructions

This exercise asks you to write a program that tests some of the built-in subroutines for working with **Strings**. The program should ask the user to enter their first name and their last name, separated by a space. Read the user's response using TextIO.getln(). Break the input string up into two strings, one containing the first name and one containing the last name. You can do that by using the indexOf() subroutine to find the position of the space, and then using substring() to extract each of the two names. Also output the number of characters in each name, and output the user's initials. (The initials are the first letter of the first name together with the first letter of the last name.) A sample run of the program should look something like this:

```
Please enter your first name and last name, separated by a space.
? Mary Smith
Your first name is Mary, which has 4 characters
Your last name is Smith, which has 5 characters
Your initials are MS
```

### Answer(s)

#### Code

```java
package programmingExercises;

import textio.TextIO;

public class InitialsInput {

    public static void main(String[] args) {

        System.out.print("Input your first and last name "
                + "separated \n" + "by a space, "
                + "e.g. 'Richard Vu' without quotes:"
                + "     "); 
        String fullName = TextIO.getln(); 

        int space = fullName.indexOf(" "); 
        System.out.println("The index of the space is "
                + space); 

        String firstName = fullName.substring(0, space); 
        System.out.print("Your first name is ");
        System.out.print(firstName);
        System.out.println(", which has "
                + firstName.length() + " characters"); 

        String lastName = fullName.substring(space, fullName.length());
        System.out.print("Your last name is");
        System.out.print(lastName);
        System.out.println(", which has "
                + (lastName.length()-1) + " characters");

        System.out.println("Your initials are "
                + firstName.charAt(0) 
                + lastName.charAt(1) ); 


    }

}
```

#### Output

```
Input your first and last name separated 
by a space, e.g. 'Richard Vu' without quotes:     Mary Sue
The index of the space is 4
Your first name is Mary, which has 4 characters
Your last name is Sue, which has 3 characters
Your initials are MS
```

### Reflections

- I didn't automatically take out the white space between the first and last name, so I had to account for that later when trying to assess the number of characters in the first and last name... and when I was trying to print the initials.

- The way that I could have extracted the first and last names without also extracting the space, would have been to not include the index of the space. That is, for 

```
Mary Smith 
0123456789
```
The space is at index 4, so when trying to extract the first namne, I could be using `name.substring(0,4)` because it'll extract the 0th character up to, but NOT including the character at index 4. However, when I'm extracting the last name, I should be using `name.substring(5,10)` because I'm trying to NOT get the space and because I'm trying to also get the last character at index 9. OR I could have used something easier, which was to use `name.substring(start)`, and just the rest of it, i.e. `name.substring(5)` to get the 5th character and every character after it for the last name. 

What kind of changes do I want to make to my program? 
- I want to declare the variables at the top of the main routine, with some descriptive comments. 
- I want to use formatted print statements to make the program more readable, as suggested by the author. 
- I also want to implement the `substring` method in a way that avoids extracting the space. 


## Exercise 2.7

### Instructions

Suppose that a file named "testdata.txt" contains the following information: The first line of the file is the name of a student. Each of the next three lines contains an integer. The integers are the student's scores on three exams. Write a program that will read the information in the file and display (on standard output) a message that contains the name of the student and the student's average grade on the three exams. The average is obtained by adding up the individual exam grades and then dividing by the number of exams.

### Answer(s)

#### Code

```java
package programmingExercises;

import textio.*;

/** Exercise 2.7 
 * This will read a file named "testdata.txt" consisting of:
 * the first line, which has the student's name; 
 * the next three lines containing the student's scores
 * on three exams as an integer.
 * 
 * It will display the student's name and the average 
 * grade on the three exams. 
 * 
 * @author richardtvu
 *
 */

public class ExamAverage {

    public static void main(String[] args) {

        /* Read "testdata.txt" */ 
        TextIO.readFile("testdata.txt"); // Where is it opening up from? 

        /* Display the student's name */
        String name = TextIO.getln();
        System.out.println(name); 

        /* Calculate the exam average */ 
        int examOne = TextIO.getInt(); 
        int examTwo = TextIO.getInt();
        int examThree = TextIO.getInt(); 
        int examAverage = (examOne + examTwo + examThree) / 3; 

        /* Display the exam average */ 
        System.out.println("Exam Average: " + examAverage); 

    }

}
```

#### Output

```
Richard Vu
Exam Average: 99
```

### Reflections

- I could have made it better by checking whether the inputs were actually integers?
- The solution actually uses `TextIO.getln()` instead of `TextIO.getInt()`, which is confusing because I'm not sure how you can convert the string to an int! oh, it's because the script actually uses `TextIO.getlnInt()`. 
- To rewrite my program, I will want to add some descriptive comments to explain the variable names, and use getlnInt() instead of getInt(). In addition, I'll want to use formatted output. 
