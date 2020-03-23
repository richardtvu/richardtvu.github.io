# Correctness, Robustness, and Efficiency

- <http://math.hws.edu/javanotes/c8/index.html>

Programs are easy to break, but careful program design can minimize errors. Two aspects of design are **correctness** and **robustness**, i.e. how likely it is that the program will do what you want it to do in a variety of situations. Exceptions, such as the `try..catch` statement can help with robustness and tests, such as `assertions` can help with correctness. However, even if you have a perfectly correct and robust program, it is of no use if it takes forever to run. Hence, **efficiency** is another important aspect of design involving how quickly a program can do what you want it to do.

Thus:

- **Correctness** describes whether a program does what you want it to do;
- **robustness** describes whether the program can still run/respond appropriately to undesired inputs

Why are these concepts important?

- small mistakes in code can lead to catastrophic consequences, e.g.

  - a bank in 1985 lost more than 5 million dollars because a bug caused its transaction system to stop working for _only_ 24 hours.
  - planes can crash and kill hundreds or cost billions of dollars

How does Java help increase correctness and robustness?

- **mandatory variable declaration** prevents typos from inadvertently introducing new variables that can cause a rocket to blow up on take-off
- **constraints on programming features** narrow what you can do to mess up programs, e.g.

  - it is impossible to store data into unallocated memory, so no **buffer overflow** errors can happen and cause viruses/malware to be run

- **automatic error detection**, such as trying to use a(n)

  - array location outside of the defined range which prevents undefined locations in arrays
  - `null` value to prevent corrupting vital system data and crashing the whole system

- **garbage collection** to remove un-referenced objects, i.e. those without pointers/variables, so that memory can freed up for other things and reduces slowing down of computer

What are the downsides to Java?

- In return for safety and security, you give up power and efficiency
- Doesn't automatically detect **integer overflow**, which is when a number is outside of the range of -2147483648 to 2147483647\. 

  - What is the consequence of not detecting integer overflow? 

    - Calculations involving numbers beyond the range will produce incorrect results. And in some cases, like the `3N+1` program, it might cause the program to run "infinitely"!

  - WHy can't we test `if (3*N+1 > 2147483647)`? 

    - Java can only represent up an integer up to 2147483647 before it begins to "wrap around" into the negatives. If we were to test this statement, then any N that is greater than 214783646/3 will cause `3*N+1` to evaluated as a negative number. FOr instance if `N = 2147483647/3`, then `3*N` would equal `2147483647` and then `3N+1` would equal `2147483647 + 1`, which would evaluate as `-2147483648`. Thus, this test would evaluate as false specifically when we want it to evaluate as true!

## Section 8.2 Writing Correct Programs

### Provably Correct Programs?

- **Provably correct** programs are a set of instructions that, when executed, will always produce the correct answer. The correct answer will need to have been specified completely and be verified to be "correct" beforehand. Otherwise, the program cannot be provably correct, as there would be no correct answer. Likewise, if there is a correct answer, and the program will always produce that answer, then that is a correct program. A correct program that you can produce a mathematical proof for, showing that the program will always produce the correct answer, is a **provably correct program**.

- What is **state**?

  - State is the particular form of a program at a given time. That is, the current values of the inputs to be read, the variables, the output produced. It is also the location of where the program is currently being executed at a given time.

- What is **process**?

  - **Process** is the sequence of states that a program goes through from start to finish.

- Therefore, a provably correct program is one in which all of the processes and states can be accounted for mathematically with 100% certainty.

- Why are they important?

  - Provable correctness of a program is important as something to strive for in applications, especially as they scale because as programs scale, the price of mistakes grow exponentially.

- How do they relate to what I've learned before?

  - Object oriented programs allow for modularity of programs, hence making it easier to figure out what state a variable is in and the process that the program takes which allows you track down bugs more easily(?). A program that is provably correct would mean that there are no bugs.

### Preconditions and postconditions?

- What are **preconditions** and **postconditions**? Why are they important? How do they relate to what I've learned before?

  - A **precondition** is a statement that must be true before a program can run. It's something you're supposed to check or force to be true prior to running the program.
  - A **postcondition** is a statement that must be true after a program has run.
  - Pre- and post-conditions help with assessing the correctness of a program and help with making that program provably correct.

- What is the quadratic formula?

  - It's an equation that allows you to find out the value of the x's where a parabola/curve intersects the x axis.
  - `b^2 -4ac` is known as the **discriminant** because it helps you tell whether you'll have two real solutions, one solution, or two complex solutions to the quadratic formula

### What are **invariants**?

#### What is a **loop invariant**?

- A **loop invariant** is a statement whose value is not changed by a loop. That is, the value is the same prior to and after running the loop. However, it is possible for the loop invariant's value to change during the loop, e.g. going from true to false.

- Loop invariants are useful for proving that programs are correct.

- They also help us develop algorithms, such as a sorting algorithm.

  ```java
  i = 0; 
    while (i < A.length) {
        // Loop invariant: A[0] <= A[1] <= .. A[i-1]
            .
            . // Code that adds A[i] to the sorted portion of the array
            .
        i = i + 1; 
    }
    // At this point, i = A.length, and A[0] <= A[1] <= ... A[A.length-1]
  ```

#### What are **class invariants**?

- **Class invariants** are statements that are always true about the state of a class or about objects made from that class.
- Invariants are important because they help you outline, plan out programs; check to make sure that they are correct; and be able to prove that your program or at least part of your program is correct.

### Why are correctness and robustness important when handling input?

- The potential user's input is virtually limitless, unless you specifically limit what they can input. Even then, you might still get unexpected inputs that can break your program if they're not handled well. Hence, you want a program that can cope well with unforeseen inputs (robustness), so that it will do what is that you want it to do (correctness).

## Section 8.3\. Exceptions and try..catch
