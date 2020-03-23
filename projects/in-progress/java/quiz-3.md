# Quiz on Chapter 3

## First Attempt, Pre-Reading 

1. An **algorithm** is a set of instructions that when run, will always conclude in a specificied result. 

2. **Pseudocode** refers to the descriptive comments that explain the purpose of code, the context, or other details. It's kind of like writing an outline to an essay, providing the high level overview of the essay, so pseudocode provides the higher level overview of the program and what it's supposed to do. By writing pseudocode, you can make algorithm development more smooth because you have a better sense of the direction and make it clear what the algorithm is supposed to do. 

3. A **block statement** is a set of statements that are run together, for instance in loops or if statements or other control structures. 

4. The main difference between a `while` and a `do...while loop` is that the `do...while` loop will run its block statement at least once, whereas the `while` statement will only run if the condition is true. 

**5. I have no idea what it means to **prime** a loop, but I thinnk it may be to start or initialize the loop?**

6. I am unsure, but I think an **animation** is a sequence of related pictures that indicate movement of some kind to communicate something. The computer rapidly flashes, depending on the hardware, e.g. 60 frames per second. 

7. A for loop to print out multiples of 3 from 3 to 36, i.e. 3 6 9 12 15 18 21 24 27 30 33 36 would look like: 

```Java

for (int n = 3; n <= 36; n++ ) {
    if ( n % 3 == 0 ) {
        System.out.print(n + " "); 
    }
}
```

8. A program that checks whether a user's input is even or odd:

```Java
import java.util.Scanner;

public class Ch3EvenOrOdd {
	
	public static void main(String[] args) {
		
		/* Create a scanner object for input */ 
		Scanner stdin = new Scanner( System.in );  
		
		/* Declare my variables */ 
		int integer; 	// Integer to check, input by the user
		boolean even; 	// A boolean for whether the integer is even or odd
		
		/* Ask the user to input an integer */
		System.out.print("Input an integer:     ");
		integer = stdin.nextInt();
		stdin.nextLine(); 
		
		/* Check if the integer is even or odd */ 
		if (integer % 2 == 0) {
			even = true; 
		} else {
			even = false; 
		}
		
		/* Print whether integer is even or odd */ 		
		if (even) {
			System.out.println("The integer is even"); 
		} else {
			System.out.println("The integer is odd."); 
		}
	}

}
```

9. Two *different* random integers. 

```Java
public class Ch3TwoDifferentRandomIntegers {
	
	public static void main(String[] args) {
		
		int firstRandomInt;
		int secondRandomInt;
		
		firstRandomInt  = (int)( Math.random()*10 );
		secondRandomInt = (int)( Math.random()*10 );
	
		while (firstRandomInt == secondRandomInt) {
			secondRandomInt = (int)( Math.random()*10 );
		}
		System.out.printf("The two different random integers are %d "
				+ "and %d", firstRandomInt, secondRandomInt); 
		
	} // end main()

} // end of class
```

10. Suppose that `s1` and `s2` are variables of type *String*, whose values are expected to be string representations of values of type *int*. Write a code segment that will compute and print the integer sum of those values, or will print an error message if the values cannot successfully be converted into integers. (Use a `try..catch` statement). 

    Pseudo-code: 
    ```Java
    // Declare variables s1 and s2
    String s1;  // A string representation of the first integer
    String s2;  // A string representation of the second integer
    
    /* Use a `try..catch` statement to check if values can be 
    converted into integers. */ 

        // if they can, compute the sum of the two integers 
    
        /* otherwise, print an error message saying that the values
        could not be converted into integers*/


    ```

    **Unclear**: 
    - How do I use a `try..catch` statement?

11. The exact output produced by the following `main()` routine: 

    ```Java
    public static void main(String[] args) {
        int N;
        N = 1;
        while (N <= 32) {
        N = 2 * N;
        System.out.println(N);   
        }
    }
    ```

    Would be: 
    
    ```Java
    2
    4
    8
    16
    32 
    ``` 

12. The exact output produced by the following `main()` routine: 

    ```Java
    public static void main(String[] args) {
    int x,y;
    x = 5;
    y = 1;
    while (x > 0) {
        x = x - 1;
        y = y * x;
        System.out.println(y);
    }
    }
    ```

    Would be: 
    
    ```Java
    4
    12
    24
    24
    0
    ```

13. What output is produced by the following program segment? **Why?** (recall that `name.charAt(i)` is  the i-th character in the string, `name`.)

    ```Java
    String name;
    int i;
    boolean startWord;

    name = "Richard M. Nixon";
    startWord = true;
    for (i = 0; i < name.length(); i++) {
        if (startWord)
            System.out.println(name.charAt(i));
        if (name.charAt(i) == ' ')
            startWord = true;
        else
            startWord = false;
    }
    ```

    When the loop begins, `startWord` is true, so it prints out the 0-th character, which is `R`. However, since `R` is NOT an empty space, `startWord` becomes false. Since `startWord` is false, the characters up until the next white space will NOT be printed. Once that white space is reached, `startWord` will become `true`. Thus, the next character, `M`, will be printed and then `startWord` becomes `false` again until the next white space. This white space then causes `startWord` to be set to `true` and the next character `N` will be printed and `startWord` will be set to `false`. Since `startWord` is false and there are no more white spaces, there will be no more characters printed on the screen. 

    Output: 
    
    ```Java
    R 
    M
    N
    ```



14. Supposed that `numbers` is an array of type `int[]`. Write a code segment that will count and output the number of times that the number 42 occurs in the array. 

    Pseudo-code: 

        FOR each element in the array `numbers`:
            IF the element is equal to 42, THEN 
                Increment the count of times 42 occurs 
        Print the count 

    ```Java
    int count;  // The number of times that 42
                // appears in the array 
    count = 0;    

    for (int i = 0; i < numbers.length; i+= ) {
        if ( numbers[i] == 42 ) {
            count++; 
        }
    }

    System.out.printf("The number 42 appeared in the array %d times", count); 
    ```

    **Unclear**
    - How do I initialize an array? 
        - Using `{values}` squiggly brackets.

15. Define the `range` of an array of numbers to be the maximum value in the array minus the minimum value. Suppose that `raceTimes` is an array of type `double[]`. Write a code segment that will find and print the range of `raceTimes`. 

    Pseudo-code: 

        FOR each value in raceTimes:
            IF the value is greater than the current maximum, THEN 
                Set the current maximum to be the value 
            IF the value is less than the current maximum, THEN 
                Set the current minimum to to be the value 
        
        Calculate the range as the maximum minus the minimum 

        Print the range 

    ```Java
    double range;      // The maximum minus the minimum 
    double maximum;    // The largest value in the array
    double minimum;    // The smallest value in the array 

    maximum = raceTimes[0]; 
    minimum = raceTimes[0];

    for ( i = 0; i < raceTimes.length(); i++ ) {
        if ( raceTimes[i] > maximum ) {
            maximum = raceTimes[i]; 
        } 
        if ( raceTimes[i] < minimum ) {
            minimum = raceTimes[i];
        }
    }

    range = maximum - minimum; 

    System.out.printf("The range for raceTimes is %1.2f.%n", range); 

    ```

    




## Second Attempt, Post-Reading

## Post-Review Reflections