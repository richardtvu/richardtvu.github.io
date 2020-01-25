# Fundamentals Part 3: Functions
- https://www.theodinproject.com/courses/web-development-101/lessons/fundamentals-part-3?ref=lnav 

## Assignments
- [x] [MDN Functions Article](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
- [x] [Return values](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Return_values)
- [x] Parameters and arguments
- [x] [Newer JavaScript.info](http://javascript.info/function-basics)
- [x] [Functions Context](http://javascript.info/function-expressions)
- [x] [Arrow Function](http://javascript.info/arrow-functions-basics)
- [ ] Practice

### Practice 

Write some functions in the `script` tag of a skeleton HTML file and test the output with `console.log`: 
1. Write a function called `add7` that takes a number and returns that number + 7. 
2. Write a function called `multiply` that takes 2 numbers and returns their product. 
3. Write a function called `capitalize` that takes a string and returns that string with *only* the first letter capitalized. Make sure that it can take strings that are lowercase, UPPERCASE, or BoTh. 
4. Write a function called `lastLetter` that takes a string and returns the very last letter of that string: 
    1. `lastLetter("abcd") should return "d" 

```JavaScript
        // function that takes a number and returns that number + 7 
        function add7(number) {
            return number += 7;
        }

        // function that returns product of two numbers
        function multiply(firstNum, secondNum) {
            return firstNum * secondNum; 
        }

        // function that takes a string and returns a string with only the first letter capitalized. 
        function capitalize(string) {
            smallLetters = string.substr(1).toLowerCase(); 
            bigLetter = string.charAt(0).toUpperCase(); 
            return bigLetter + smallLetters; 
        }

        // function called lastLetter that takes a string and returns the very last letter of that string 
        function lastLetter(string) {
            let last = string.length - 1; 
            return string.charAt(last); 
        }
```