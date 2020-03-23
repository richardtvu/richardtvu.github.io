# Programming Exercises for Chapter 3

1. Done.

2. CountLargestDivisors

  **Pseudo-code**:

  ```java
  // iterate through all 10_000 integers
  // determine how many divisors each number has 
  // IF the current integer has more divisors than the last integer THEN 
  // Update the variable used to keep track of the int with max
  // divisors to be the current integer 

  // Update the variable for the maximum divisors seen so far
  // print the integers.
  ```

  Next steps:

  - What is a divisor?
  - How do I determine the divisors of an integer?

3. Write a program that will evaluate simple expressions such as `17 + 3` and `3.14159*4.7`. The expressions are to be typed in by the user. The input always consists of a number, followed by an operator, followed by another number. The operators that are allowed are `+`, `-`, `*`, and `/`. You can read the numbers with `TextIO.getDouble()` and the operator with `TextIO.getChar()`. Your program should read an expression, print its value, read another expression, print its value, and so on. The program should end when the user enters 0 as the first number on the line.

  **PSEUDO-CODE**:

  ```
  This program will ask the user for an expression of the 
  syntax: [number][operator][number], e.g. 7 + 9\. The operator 
  must be +, -, *, or /. The program will then convert the 
  input into an expression, evaluate it, and print the result. 
  Then, it will repeat this process until the user puts 0 as 
  the first #.

  WHILE the first input is NOT 0: 

  Ask the user for input: 
  "Please input a number:      "
     IF this first input is 0, THEN
         first input is 0 
  "Please input an operator:   "
  "Please input a number:      "

  Combine the inputs into an expression 

  Evaluate the expression 

  Print the result
  ```

  **CODE**:

4. Write a program that reads one line of input text and breaks it up into words. The words should be output one per line. A word is defined to be a sequence of letters. Any characters in the input that are not letters should be discarded. For example, if the user inputs the line

  `He said, "That's not a good idea."`

  then the output of the program should be

  ```
  He 
  said
  That's // An apostrophe can be considered a part of the word 
  // if there is a letter on each side of the apostrophe
  not
  a
  good
  idea
  ```

  **Pseudo-code**:

  ```
  Read one line of input text 
  FOR each character in the line of input:
  IF the character is a letter AND 
  the next character is a letter THEN: 
   Add the character to a sequence to be printed 
  ELSE IF the character is a letter AND 
  the next character is NOT a letter AND
  NOT an apostrophe THEN:
   Add the character to the sequence to be printed
   Print the sequence to standard output on a new line
   Remove the sequence from memory
  ELSE:
   Discard the character
  ```

5. There is a file named "sales.dat". It contains sales data for each city in the format: `[City]: [Sales]`. The sales are input as a double, e.g. `Philadelphia: 23891.22`, OR a string which provides an explanation for the missing data, e.g. `Nashville: no report received`.

  This program will calculate and print the sum of the sales from all the cities and the number of cities without sales data.

  **PSEUDO-CODE**:

  ```
  WHILE it is NOT the end of the file:
  Read and ignore characters up to the colon
  Read the rest of the line into a String
  TRY to convert the string into a number:
    IF successful THEN: 
        Add the number to the sum 
  CATCH the error:
    Increment the number of cities without sales data
    Continue the loop
  Print the sum of the sales data and the # of cities without sales data
  ```

  **What do I need to know?**

  - How do I ignore characters up to a certain point?
  - How to convert a string into a number?
  - How do I tell when a file has ended?
  - How do I use the try..catch statement?

6. **Exercise 3.2** asked you to find the number in the range 1 to 10_000 that has the largest number of divisors. You only had to print out one such number. Revise the program so that it will print out **all** numbers that have the maximum number of divisors. Use an array as follows: As you count the divisors for each number, store each count in an array. Then at the end of the program, you can go through the array and print out all the numbers that have the maximum count. The output from the program should look something like this:

  ```
  Among integers between 1 and 10,000, 
  The maximum number of divisors was 64
  Numbers with that many divisors include: 
    7560 
    9240
  ```

  **PSEUDO-CODE**:

  ```
  FOR each integer between 1 and 10_000: 
  Calculate the number of divisors 
  Store the integer and its number of divisors in an array
  IF the integer has more divisors than the current max
  Update the current max

  FOR each element in the array:
  Print out the integers whose number of divisors matches the maximum
  ```

  **What do I need to know?**

  - How do I check which element in the array has the largest number of divisors?
  - How do I store values in an array?

7. An example in **Subsection 3.8.3** tried to answer the question, "How many random people do you have to select before you find a duplicate birthday?" The source code for that problem can be found in the file _BirthdayProblem.java_. Here are some related questions:

  - How many random people do you have to select before you find **three** people who share the same birthday? (That is, all three people were born on the same day in the same month, but not necessarily in the same year.)

  - Suppose you choose 365 people at random. How many different birthdays will they have? (The number could theoretically be anywhere from 1 to 365).

  - How many different people do you have to check before you've found at least one person with a birthday on each of the 365 days of the year?

  Write **three** programs to answer these questions. Each of your programs should simulate choosing people at random and checking their birthdays. (In each case, ignore the possibility of leap years.)

  - I'll write some pseudo-code for the example in Subsection 3.8.3: "How many random people do you have to select before you find a duplicate birthday?"
      - If we're just interested in the month and date of the their birth, then we don't need to generate the birth year. To tackle this problem, I'd first randomly generate the birth month, which would the impact the possibilities for the birth day. Based on the birth month, I'd randomly generate a birth day. I could then store the month and day in separate variables. Each time a month and day are generated, then I'd check if that month is equal to any of the months prior. If so, then I'd check whether any of the days were equal to any of the previous days. Each time I generate and check, I'd increment the number of people generated. When there is a match for both the month and day, then I'd print out the # of people it took to get o that point. 

      -  How would I represent this? I think it would be a two separate array, where each index in the array represents the person. For instance Month[0] is the birth month of Person 0 and Day[0] is the birth day of Person 0. To check if person 1 has the same birthday, then I'd do an equality check of Month[0] == Month[1]. IF that's true, then I'd check if Day [0] == Day[1]. If that's true, then I'd print out the index + 1 for # of people it took to generate the same MMDD. 

      ```
      Month:  10  1   7
      Day:    23  23  8
      ```  

      ```
      
      Randomly generate a month and a day of birth for the 0-th index
      Increment index by 1 
      
      WHILE the index is greater than 0 AND there is no duplicate
        Generate a MM and DD in the i-th index 
        FOR each index in the array MM:
          IF MM[i] matches any of the previous months: 
            IF the day at the index matches the day at the index of the matching month, THEN: 
              Print that the number of people selected to get a duplicate birthday is the index plus one. 
        Increment the index by 1. 
      ``` 

    **NEXT STEP** - Flesh out this program. 

8. Write a GUI program that draws a checkerboard. Base your solution on the sample program *SimpleGraphicsStarter.java*. You will draw the checkerboard in the `drawPicture()` subroutine, after erasing the code that it already contains. 

Requirements: 
- Checkerboard should be 400x400 px. 
  - You are able to change the size of the drawing area by modifying the first two lines of the `start()` subroutine to set `width` and `height` to 400 instead of 800 and 600. 
  - Set each square to be 50x50 pixels. 
  - The squares should alternate between two colors, e.g. red and black. 
    - You can color them using numbers from 0 to 7. If the row and the column are both even or both odd, then red otherwise black. 
- 

Next steps:
  - Check out *SimpleGraphicsStarter.java* 
  - How do I draw things? 

9. Make an animation that will display cyclic (repeating the same thing over and over) and oscillating motions (doing things back and forth). 

  **CYCLIC**

      Use a square that moves to the right side, jumps back to the start, and then repeats this motion over and over

  **OSCILLIATION**

      Make a square that moves back and forth, moving to the right in the first half of the animation and then to the left in the second half, and then repeating this animation
    
  **NEXT STEPS**
  - Why are we using `cyclicFrameNumber = frameNumber % N;` to implement cyclic motion? 

  - WHy are we using the following to implement oscillating motion? 

      ```Java
      oscillationFrameNumber = frameNumber % (2*N);
      if (oscillationFrameNumber > N) 
        oscillationFrameNumber = (2*N) - oscillationFrameNumber; 
      ```



