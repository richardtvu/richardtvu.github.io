# [3.2.2  The 3N+1 Problem](http://math.hws.edu/javanotes/c3/s2.html#control.2.2)

## Instructions

"Given a positive integer, N, define the '3N+1' sequence starting from N as follows: If N is an even number, then divide N by two; but if N is odd, then multiply N by 3 and add 1. Continue to generate numbers in this way until N becomes equal to 1. For example, starting from N = 3, which is odd, we multiply by 3 and add 1, giving N = 3*3+1 = 10. Then, since N is even, we divide by 2, giving N = 10/2 = 5. We continue in this way, stopping when we reach 1. The complete sequence is: 3, 10, 5, 16, 8, 4, 2, 1.

"Write a program that will read a positive integer from the user and will print out the 3N+1 sequence starting from that integer. The program should also count and print out the number of terms in the sequence."

## Pseudocode 

**Book**

General outline
```
get a positive integer N from the user
computer, print, and count each number in the sequence 
output the number of terms 
``` 

Expand loop
```
get a positive integer N from the user; 
WHILE N is NOT 1:
    Compute N = next term; 
    Output N; 
    Count this term; 
Output the number of terms; 
```

Expand loop
```
get a positive integer N from the user; 
WHILE N is NOT 1:
    IF N is even: 
        Calculate N = N/2; 
    ELSE 
        Calculate N = 3 * N + 1; 
    Output N; 
    Count this term; 
Output the number of terms; 
``` 

Specify how to count terms; 
```
get a positive integer N from the user; 
Let counter = 0; 
WHILE N is NOT 1; 
    IF N is even:
        Calculate N = N/2; 
    ELSE 
        Calculate N = 3 * N + 1; 
    Output N; 
    Add 1 to the counter; 
Output the counter; 
```

Add guardian code to prevent non-positive integer input
```
Ask user to input a positive number; 
Let N be the user's response; 
WHILE N is NOT positive: 
    Print an error message; 
    Read another value for N; 
Let counter = 0; 
WHILE N is NOT 1:
    IF N is even: 
        Calculate N = N/2; 
    ELSE 
        Calculate N = 3 * N + 1; 
    Output N; 
    Add 1 to the counter;
Output the counter
```

Java program implementing this algorithm:

```Java
import textio.TextIO; 

/**
 This program prints out a 3N+1 sequence starting from a positive integer specified by the user. It also counts the number of terms in the sequence, and prints out that number.
 */
 public class ThreeN1 {

     public static void main(String[] args) {

         int N;         // for computing terms in the sequence
         int counter;   // for counting the terms

         System.out.print("Starting point for the sequence: "); 
         N = TextIO.getlnInt(); 
         while (N <= 0) {
            System.out.print(
                 "The starting point must be positive. Please try again: ");
            N = TextIO.getlnInt(); 
         }
         // At this point, we know that N > 0

         counter = 0; 
         while (N != 1) {
             if (N % 2 == 0) {
                 N = N / 2; 
             } else {
                 N = 3 *  N + 1; 
             }
             System.out.println(N); 
             counter = counter + 1; 
         }

         System.out.println(); 
         System.out.print("There were "); 
         System.out.print(counter): 
         System.out.println(" terms in the sequence."); 

     } // end of main()
 } // end of class ThreeN1
```

    

**Expanded pseudo-code**
```
prompt user for input, a number, N
IF N is NOT an integer greater than 1, THEN 
    WHILE N is NOT an integer
        display message "N is not an integer, input has been rejected." 
        re-prompt user for input 
WHILE the number, N, is greater than 1
    Increment number of terms by 1 
    Add N to the end of a string 
    IF N is an even number, THEN divide N by 2
    ELSE multiply N by 3 and add 1
Append 1 to the end of the string. 
Display the number of terms
Display the 3N+1 sequence, starting from the initial N 
```

Pseudocode translated into code: 
```Java
int number, terms = 0; // declare the variables 
String sequenceText = ''; 
System.out.println("Type a positive integer greater than 1: "); 
number = TextIO.getlnDouble(); 
while (typeof(initialNumber) != int) {
    System.out.println("N is not an integer, input has been rejected."); 
    number = TextIO.getlnDouble(); 
}
while ( number > 1 ) {
    terms++; 
    sequenceText += number + ', ' 
    if ( N % 2 == 0 ) {
        number = number / 2;
    } else {
        number = number * 3 + 1; 
    }
}
sequenceText += '1'; 
System.out.println("The sequence, beginning with the number you input, is " + sequenceText); 
System.out.println("The number of terms in this sequence is " + terms); 
```









---
## Background Exercise

> As an example, let's see how one might develop the program from the previous section, which computes the value of an investment over five years. The task that you want the program to perform is: **"Compute and display the value of an investment for each of the next five years, where the initial investment and interest rate are to be specified by the user."** 

Step-by-step pseudo-code: 
```
// get user's input
// calculate the value of the investment after 1 year
// display the value
// calculate the value of the investment after 2 years
// display the value
// calculate the value of the investment after 3 years
// display the value
// calculate the value of the investment after 4 years
// display the value
// calculate the value of the investment after 5 years
// display the value 
```

Pseudocode rewritten with loop: 
```
get user's input
FOR each year
    calculate the value of the investment
    display the value 
``` 

Expanded pseudocode to be more specific: 
```
PROMPT user for value of initial investment 
store user's response 
PROMPT user for interest rate 
store user's response 

FOR each year 
    calculate the interest gained after a year 
    add the interest to the total 
    display the value 
``` 

Loop portion of pseudocode further expanded:
``` 
FOR each year, starting at year 0, and incrementing by 1: 
    year = years + 1; 
    compute interest 
    add the interest to the value
    display the value
```

Further expansion: 
```
PROMPT user for value of initial investment 
store user's response 
PROMPT user for interest rate 
store user's response

FOR each year, starting at year 0, and incrementing by 1: 
    year = years + 1; 
    compute interest = value * interest rate
    add the interest to the value
    display the value
```

Pseudocode translated into code: 
```Java
double principal, rate, interest; // declare the variables
int years; 
System.out.print("Type initial investment: ");
principal = TextIO.getlnDouble(); 
System.out.print("Type interest rate: "); 
rate = TextIO.getlnDouble(); 
for ( years = 0; years <= 5; years++ ) {
    years = years + 1; 
    interest = principal * rate; 
    principal = principal + interest; 
    System.out.println(principal); 
} 
``` 




