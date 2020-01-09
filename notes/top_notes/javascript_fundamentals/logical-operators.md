# [Logical Operators in JavaScript](http://javascript.info/logical-operators)

## || (OR)

- Comparison that outputs true when any of the arguments are true.
- "Finds the first truthy value". What does that mean? Given the following example, what does the `||` operator do?

  ```JavaScript
  result = value1 || value2 || value3;
  ```

  - Checks the values of the operands from left to right.
  - Converts each operand into a boolean. If the result is true, stops checking and returns that value. Otherwise, it'll return the value of the last oeperand.
  - Thus, if only value2 is `true`, then it'll return the value of value2 as `true`. Otherwise, if all of the variables are `false`, then the `||` operator will return the value of value3, which is `false`.

- How can `||`(OR) be used differently than the conventional, boolean-only use?

  1. Find the first value that has data. e.g.

     ```JavaScript
     let currentUser = null;
     let defaultUser = "John";

     let name = currentUser || defaultUser || "unnamed";

     alert( name ); // Selections "John" in defaultUser, which is the first truthy value.
     ```

     - This would show `"unnamed"` instead if both `currentUser` and `defaultUser` were falsy ( which I think means not containing a value or not true ).

  2. Evaluate expressions for the first truthy one in the shortest path, hence **short-circuit evaluation**.

     ```JavaScript
     let x;

     true || (x = 1);

     alert(x); // undefined because ( x = 1) is not evaluated
     ```

     - What would this display if it were reversed with `(x = 1)` in front?

       ```JavaScript
       let x;

       ( x = 1 ) || true;

       alert(x); // It would display 1!
       ```

  - Why does it display 1? The order of operations would have the expression be evaluated first, so that x would be 1. Then, since x has a value, it is a truthy value and would be displayed.

## && (AND)

- Returns `true` if both operands are truthy (have an actual value), otherwise it returns `false`.

> Finds the first falsy value

- What does that mean?

  - `&&` evaluates operands and converts them to boolean values from left to right. If an operand is `false`, then the operator returns the value of the first operand that is `false`. Otherwise, if there are no `false` operands, `&&` returns the value of the last operand. For instance...

  ```JavaScript
  alert( "Jordan Peterson" && "What a guy" && "The hero"); // returns "The hero"
  ```

- AND `&&` has a higher precedence than OR `||`. That is, it's evaluated first before OR is... For instance, the following two code lines are equivalent.

  ```JavaScript
  a && b || c && d;
  (a && b) || (c && d);
  ```

  - However,the following are different because of `&&`'s higher precedence:

  ```JavaScript
  a = true;
  b = false;
  c = false;
  d = false
  a || b && c || d; // a OR (b AND c) OR d. Returns true because a is true.
  (a || b) && (c || d); // (a OR b) AND (c OR d). While the (a OR b) is true because a is true, (c OR d) is false, so the entire expression evaluates as false.
  ```

## !(NOT)

- Converts operand to boolean and returns the inverse value.
- Can be used to convert something into a boolean value, by doing a double NOT `!!`
- _Highest precedence_, so it executes before `&&` and `||`

## Tasks

1. What is the code below going to output?

   ```JavaScript
   alert( null || 2 || undefined );
   ```

   - Pre-reading answer: I think that since the alert is not referencing an established variable, then what is going to be true is undefined since nothing has been defined. Thus, I think the answer will be true.

   - Post-test, pre-reading: The answer is `2`. This is the answer I got after running the command in the console, but why does it show 2? Well, I think it's because the alert function is supposed to show a message on the screen. Since null doesn't print anything, 2 is the first argument that has an actual value to display. This value will get converted into a string and then displayed. In that case, I think that the null doesn't print anything because it cannot be converted into a string? Can it?

   - I tried to set a variable to null and convert it to a string. This resulted in a TypeError that test is null.
   - When I set a variable to `2`, I was able to successfully convert it into a string using `toString()`. Thus, this would be display-able.
   - Would undefined be displayed if I tried to display it? I think it would because undefined can be converted into a string ( I think it can).
     - Yes. Inputting `undefined` as a parameter (?) prints "undefined". HOWEVER, if I tried to convert a variable with the value of `undefined` to a string, I would get `TypeError: test is undefined`. Therefore, For whatever reason, alert can display `undefined`, but not null and it's not because `undefined` can be converted into a string.
   - Can null be displayed using alert as well?

     - Yes. So why is null not being displayed whe there's a 2?
     - When `alert(null || undefined)` is input, undefined is output. Why isn't null output?

   - Post-skim thoughts:

     > In other words, a chain of OR "||" returns the first truthy value or the last one if no truthy value is found.

     - I think this quote holds the answer. In that, if none of the operands are true, then the || operator will simply return the last value, without conversion into a boolean. That is, it would return `undefined` if it was just `alert( null || undefined)'
       - and`null` if it was just `alert( undefined || null )` ... and it does!
     - Post-reading thoughts: The code of `alert( null || 2 || undefined)` should output 2 because the OR `||` operator will return the first truthy value. That is, it evaluates from left to right, and 2 is the first value that returns when converted into a boolean. Thus the `||` operator will take that, return it, and the `alert` function will display the 2.

2. What's the result of OR'ed alerts?

   ```JavaScript
   alert( alert(1) || 2 || alert(3) );
   ```

   - Post-reading, pre-test thoughts:
     - JavaScript evaluates an expression from left to right, but parenthesis take precedence. Thus, before the first alert executes, operands within must first be evaluated. `||` returns the first "truthy" value, that is, the first value that when converted into a boolean returns true and also follows the left-to-right evaluation protocol. Thus, the first value to be converted into a boolean would be alert(1). Can alert(1) be converted into a boolean? Can functions be converted into a boolean? I think so. I think that it would display 1 and return that as a result, which would then display as another alert. The 2 and the alert(3) won't show because `||` will stop at displying the first operand.
   - Post-test:

     - I was wrong, it turns out it will display 1 followed by 2. Why?

       - alert(1) returns a false when converted into boolean via `!!` . Thus, it will execute the alert, display a 1, then skip the first operand because it returns a false. The second operand will be converted into a boolean, which will return true, and thus be displayed.

       ```JavaScript
       alert( alert(1) || 2 || alert(3) ); /*
       The alert should first display 1, followed by 2. Why?
       The order of operations in JavaScript prioritizes evaluating that which is within the parenthesis first and then from left to right.
       The first operand is alert(1). Before it can be evaluated, that which is within the alert parenthesis (1) must be evaluated.
       The 1 is true, so it will be taken by alert and displayed.
       Then, because the alert function, having displayed 1, is converted into a false, the operation proceeds to the next operand.
       The || operator then evaluates 2, which evaluates as true in boolean. Thus, because 2 is the first truthy value, the || operator returns 2 to the alert function, which then takes that 2 and displays it. */
       ```

3. What is the result of AND?

   ```JavaScript
   alert ( 1 && null && 2 );
   ```

   - Pre-reading answer: I think that the answer will be false, because null wasn't displayed before so it should be false.

   - Post-test: The answer is `null`. What!? Why?

     - I think that this may be because the `&&` operator returns the first falsy value. That is, it evaluates 1 as true, so it proceeds to null. When null is converted into a boolean, e.g. `!!null`, it returns false. Given that `&&` will return the first falsy value, it will therefore return "null" to alert, which displays "null".
       `null` returns `false`

       - If this is the case, then, even if null is placed at the end of the alert, it should still return `"null"`. Similarly, since `undefined` has a boolean value of `false`, the same should happen if you replace `null` with `undefined`.

       ```JavaScript
       alert( 1 && 2 && null); // displays null

       alert( 1 && 2 && undefined); // displays undefined
       ```

4. What is the result of AND'ed alerts?

   ```JavaScript
   alert ( alert(1) && alert(2) );
   ```

   - Pre-test answer: I think it will display 1 and 2.

   - Post-test answer: It displayed an alert of `1` followed by an alert of `undefined`. Okay, I think that this is at the point where any further guessing before the reading is going to be totally off, so it's time to start reading.
   - Building on what I've learned so far, the operation will proceed by evaluating the operands within the parentheses, `alert(1) && alert(2)`. Since there is still a parenthesis left, the operation will proceed by evaluating `1`. 1 will be displayed. Because `&&` returns the first falsy value, it will return the value of `alert(1)` since the boolean value of `alert(1)` is `false`. The value of `alert(1)` when assigned to a variable, say, `someVariable` will be `undefined`. Perhaps, because there is no value that has been explicitly assigned to `alert(1)`. Nevertheless, the value of `alert(1)` is `undefined`, so the alert will display `undefined`.

5. What is the result of OR AND OR?

   ```JavaScript
   alert( null || 2 && 3 || 4 );
   ```

   - Pre-test:
     - Parentheses > `&&` >> `||`. So, we will begin by evaluating `2 && 3`. Both `2` and `3`, when converted to boolean values are `true` and therefore are truthy values. Therefore, the expression of `2 && 3` is `true`. Next, the `||` operator evaluates `null` as `false`, so it proceeds to `2 && 3`. Since `2 && 3` are true, it returns that value. Because `&&` returns the value of the first falsy value or the value of the last truthy value,`&&` will return `3` to `||` and `||` will return `3` to the alert function. Therefore, this expression will display 3.

6. Check the range between:
   Write an "if" condition to check that `age` is between `14` and `90` inclusively.
   "Inclusively" means that `age` can reach the edges `14` or `90`.

   ```JavaScript
   let age; // declare the variable age

    if ( 14 <= age <= 90 ) {
      alert("Age is between 14 and 90, inclusively");
    }

    if ( ( age >= 14 ) && ( age <= 90 ) ) {
      alert("Age is between 14 and 90, inclusively");
    }
   ```

7. Check the range outside:
   Write an `if` condition to check that `age` is NOT between 14 and 90 inclusively.
   Create two variants, the first one using NOT `!`, the second one - without it.

   - NOT variant `!`

     ```JavaScript
     if (!( age >= 14 && age <=90 )) {
       ...
     }
     ```

   - Second variant:

     ```JavaScript
     if ( age <= 14 || age >= 90 ) {
       ...
     }
     ```

8. A question about `if`:

   - Which of these `alerts` are going to execute?
   - What will be the results of the expressions be inside `if(...)`?

     ```JavaScript
     if (-1 || 0) alert( `first` );  // The result will be -1 and will alert.
     if (-1 && 0) alert( `second` );  // The result will be false, 0 and won't alert.
     if (null || -1 && 1) alert( `third` ); // The result will be true with a return value of 1 and will alert.
     ```

9. Check the login

   - Write the code which asks for a login with `prompt`
   - If the visitor enters `"Admin"`, then `prompt` for a password.
   - If the input is an empty line or `Esc` - show "Canceled", otherwise show "I don't know you".
   - If the password equals "TheMaster", then show "Welcome!"
   - Else if it's another string, show "Wrong password"
   - Else if it is an empty string or cancelled input, show "Canceled".

     ```JavaScript
     // Login Prompt
     let login = prompt("Who's there?");

     if ( login == "Admin" ) {
       // Ask for the password
       let password = prompt("Password?");

       if ( password == "TheMaster" ) {
         alert("Welcome!");
       } else if ( password == '' || password == null ) {
         alert("Canceled");
       } else {
         alert("Wrong password");
       }

     } else if ( login == '' || login == null ) {
       alert("Canceled");
     } else {
       alert("I don't know you");
     }
     ```
