# Arrays

- [TOP](https://www.theodinproject.com/courses/web-development-101/lessons/fundamentals-part-4?ref=lnav)
- [Introduction](https://www.w3schools.com/js/js_arrays.asp)
- [Useful built-in array methods](https://www.w3schools.com/js/js_array_methods.asp)

## Summary

- Arrays are special types of objects whose elements are indexed by numbers. 
- They can contain any variable type, including objects. 
- There are built-in methods to add or remove elements from the back, from the front, from between elements; to find the length of the array; to merge arrays, etc. 
- Arrays are declared using `[]` with the elements going in between the brackets. 
- You should access array elements using indexes, e.g. `array[0]` would access the element in index 0, the first element


## Introduction to Arrays

- Why are arrays useful?

  - They let you store many values in one variable, which lets you

    - organize data, that would otherwise by unruly and difficult to work with, e.g.

      - such as the names of hundreds of cars

    - easily access data in one centralized location

- How do you make arrays?

```javascript
/* using var

  + values accessible globally

  */
  var heroes = ["Jordan Peterson", "Nasim Taleb", "Jonathan Haidt"];

  /* using let

  + access restricted to local scope

  */
  let heroes = ["Jordan Peterson", "Nasim Taleb", "Jonathan Haidt"];

  /* multiple lines */
  let heroes = [
      "Jordan Peterson",
      "Nasim Taleb",
      "Jonathan Haidt"
  ];
```

- How do you access array elements?

  - by referencing index number

```html
<p id="hero-display"></p>

<script>
    let heroes = ["Jordan Peterson", "Nassim Taleb", "Johnathan Haidt"];
    document.getElementById("hero-display").innerHTML = heroes[1];
    // displays "Nassim Taleb" in between p tags
</script>
```

- How do you change elements of an array?

```javascript
array[index] = "New value"; // syntax.

  let heroes = ["Jordan Peterson", "Nassim Taleb", "Johnathan Haidt"];

  // change Jonathan Haidt to George Orwell
  heroes[2] = "George Orwell"
```

- How do you access the full array?

  - Refer to the array name

```javascript
let friends = ["Navdeep Maini", "Shawn Pan", "Dee Dee Maguehi"];
  document.getElementById("element-id").innerHTML = friends;
```

- What type of _variable_ are arrays?

  - a special type of **object** that stores an ordered sequence of values.

    - special because arrays use **numbers** to access "elements", whereas

```javascript
let friends = ["Navdeep Maini", "Shawn Pan", 23];
    console.log(friends[0]); // returns "Navdeep Maini" in console.
```

```
- objects typically use **names** to access "members"
```

```javascript
let hero = {
        firstName: "Jordan",
        lastName: "Peterson",
        age: "approximately 60 plus or minus 10"
    };

    console.log("The first name of my hero is " + hero.firstName); // The first name of my hero is Jordan.
```

- What kind of variable types can arrays contain?

  - the normal data types and including objects and functions

- Where does the real strength of JavaScript arrays come into play?

  - built-in arrays and methods

- What does the length property do?

  - returns the number of elements in the array

```javascript
let numbers = [1, 2, 3, 4, 5, 6];
  numbers.length; // length of numbers is 6
```

- How do you access the first array element?

```javascript
array[0];
```

- How do you access the last array element?

  - Use the length method to get # of elements, and then subtract 1 to get the index of last element.

```javascript
fruits = ["Durian", "Strawberry", "Orange"];
  let lastElement = fruits[fruits.length - 1];
```

- How do you loop array elements?

  - Use a `for` loop

```javascript
let family = ["Navdeep Maini", "B&G", "Uncle Matt", "Shawn Pan"];
    let numFamily = family.length;
    let list = "<ul>";

    for (let i = 0; i < numFamily; i++) {
        list += "<li>" + family[i] + "</li>";
    }
    list += "</ul>";

    document.getElementById("demo").innerHTML = list;
```

- How do you add array elements?

  - To add to the end of arrays, you can use

    - `push()` method - e.g. `array.push("newElement");`
    - `length` property - e.g. `array[array.length] = "newElement";`

  - To add elements at indices other than the end, you can directly specify the index ... but this can cause undefined "holes" in arraay

`array[6] = 'newElement'; // in an array with four elements, will create two indices with undefined values, and add in the newElement`

- What are associative arrays?

  - AKA hashes, arrays in which the indexes have names
  - JavaScript **arrays** do **not** support named indexes. They **always** use **numbered indexes**.

- How are arrays and objects different?

  - Arrays have **numbered** indexes.
  - Objects use **named** indexes.

- When should you use arrays? When should you use objects?

  - When you want element names to be strings/text, use objects.
  - When you want element names to be numbers, use arrays.

- Why should you avoid `new Array()` ?

  - No need to use it to make arrays, when `[]` will do the job more simply and straightforwardly.
  - Can cause unnecessary bugs, like...

    `var points = new Array(40) // creates 40 undefined elements array...`

- How do you know if a variable is an array?

  1. Use the method `Array.isArray()` , e.g.

    `Array.isArray(fruits); //returns true if fruits is array`

  2. Make your own `isArray` method, which will always return true if the argument is an object prototype contains the word "Array".

  ```javascript
  function isArray(x) {
    return x.constructor.toString().indexOf("Array") > -1; 
  }
  ```

  1. Use the `instanceof` operator to check if the variable is an object that was created by the Array constructor.

  ```javascript
  let fruits = ["Banana", "Orange", "Apple", "Mango"];
  fruits instanceof Array;
  ```

### Exercises

1. Get the value "Volve" from the `cars` array.

```javascript
var cars = ["Saab", "Volvo", "BMW"];
var x = cars[1];
```

1. Change the first item of `cars` to "Ford".

```javascript
var cars = ["Volvo", "Jeep", "Mercedes"];
cars[0] = "Ford";
```

1. Alert the # of items in an array, using the correct Array method.

```javascript
var cars = ["Volvo", "Jeep", "Mercedes"];
alert(cars.length);
```

## Built-in Array Methods: What built-in methods can you use to manipulate arrays?

- How do you convert Arrays to Strings?

  - `toString()` - Use this to convert the array into a string of elements separated by commas. e.g.

    ```javascript
    let coworkers = ["CJ", "CR", "JB", "RB"];
    console.log(coworkers.toString()); // CJ,CR,JB,RB
    ```

  - `join()` - when you want to join elements into a string _and_ you want to use a different separator other than commas

    ```javascript
    let coworkers = ["CJ", "CR", "JB", "RB"];
    console.log(coworkers.join(" * ")); // CJ * CR * JB * RB
    ```

- How do you remove and add items into an array?

  - `pop()` - remove last element from array

    ```javascript
    let weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    console.log(weekDays.pop());
    ```

  - `push()` - add an element to end of array.

    ```javascript
    let weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday'];
    weekDays.push("Friday"); 
    console.log(weekDays); //
    ```

  - `length` property: You can add a new element to the using length to access the index after the last element

    ```javascript
    let weekDays = ['Monday']; 
    weekDays[weekDays.length] = 'Tuesday';
    ```

- How do you remove the first element of an array?

  - `shift()`

    ```javascript
    let weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday'];
    weekDays.shift(); // removes 'Monday' and returns that string
    ```

- How do you add a new element to the beginning of the array?

  - `unshift();`

    ```javascript
    let weekDays = ['Tuesday', 'Wednesday', 'Thursday'];
    weekDays.unshift("Monday"); // adds 'Monday' to beginning of the array and returns length of array.
    ```

- How do you change elements?

  - Access the element using their **index number** and use an assignment statement to change the value of that element.

    ```javasscript
    weekDays[0] = 'notMonday';  // changes the first element to notMonday.
    ```

- How do you delete an element?

  - `delete array[index]` will replace the value at that index with an 'undefined'.

- How do you splice an array to add elements?

  - `splice()` - i.e. `splice(insertionPosition, numElementsToRemove, elementsToAdd, anotherElement); 

    ```javascript
    let music = ["Pop", "Electronica", "Rock"];
    music.splice(1, 0, "Classical", "Indie", "Alternative", "Easy Listening");
    ```

- How do you remove elements using splice()?

  ```javascript
  console.log(music); // appends classical, indie, alternative, and easy listening to the index position after 0, beginning with 1\. "Pop", "Classical", "Indie", "Alternative", "Easy Listening", "Electronica", "Rock"
  music.splice(0, 3); // remove three elements beginning at index 0 and returns the three elements removed, which were "Pop" "Classical" and "Indie" 
  console.log(music); //  "Alternative", "Easy Listening", "Electronica", "Rock"
  ```

- How do you concatenate/merge arrays?

  - `concat()` - i.e. `newArray = arrayOne.concat(arrayTwo);`

    ```javascript
    let brothers = ['NM', 'SP'];
    let sisters = ['DM', 'HS'];
    let uncle = ['ML'];
    let brothersAndSisters = brothers.concat(sisters); 
    let family = brothers.concat(sisters, uncle, 'CS', 'IR', 'CL');  // returns a new array with all of the elements stored in a new array called family
    console.log(family);
    ```

- How do you copy a slice of an array over to a new array?

  - `slice()` - i.e. `newArray = oldArray.slice(startingIndex);`
  - Take the elements from index 1 to the end and put it into a new array

    ```javascript
    let dogs = ['Siberian Tiger', 'Dalmation', 'Pomerian', 'Chihuahua'];
    let dogsNoCats = dogs.slice(1);
    ```

  - Slice out a middle section of an array.

  ```javascript
  let maybeTrees = [
    'grass', 
    'pine', 
    'evergreen',
    'oak', 
    'yew', 
    'jesus'
  ]; 
  let beginning = 1; 
  let end = maybeTrees.length - 1; 
  let trees = maybeTrees.slice(beginning, end); // cuts out pine up to, but not including jesus because jesus ain't no tree.
  ```

- What does an array automatically convert to when a _primitive_ value (not an object) is expected? 
  - a string! The following are equivalent:
  ```html
  <p id='demo'></p>
  
  <script>
  let mangoMania = ['Yellow Mango', 'Orange Mango', 'Yellow-Green Mango', 'Golden Mango'];
  document.getElementById('demo').innerHTML = mangoMania.toString(); 

  document.getElementById('demo').innerHTML = mangoMania; 
  </script>
  ```

### Exercises

1. Which Array method do you use to remove the last item of the following array?

```javascript
var fruits = ["Banana", "Orange", "Apple"];
```

Method:

```javascript
fruits.pop();
```

1. Which Array method do you use to add "Kiwi" to the following array?

```javascript
var fruits = ["Banana", "Orange", "Apple"];
```

Method:

```javascript
fruits.push("Kiwi");
```

1. How do you remove "Orange" and "Apple" from `fruits` ?

```javascript
var fruits = ["Banana", "Orange", "Apple"];

   fruits.splice(1, 2); // beginning at the index one, which is the second element, remove two elements
```
