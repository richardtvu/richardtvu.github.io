# Parameters vs. Arguments

[Fundamentals Part 3](https://www.theodinproject.com/courses/web-development-101/lessons/fundamentals-part-3?ref=lnav)

## What is the difference between parameters and arguments?

- Parameters are the expected inputs for a function, they go between the parentheses of the function definition.Paramters are _placeholders_ for the values that will be input.
- Arguments are the actual inputs that go into the function when called.

  ```JavaScript
  // `person` is the parameter
  function favoritePerson(person) {
      console.log(person + " is my favorite person!");
  }
  // Dr. Jordan Peterson is the argument.
  favoritePerson('Dr. Jordan Peterson');

  // You can also pass in a variable as an argument.
  let hero = 'Dr. Jordan Peterson';
  favoritePerson(hero);
  ```

- Changing the parameter name won't change the result.

  ```JavaScript
  function favoriteAnimal(mammal) {
      console.log(mammal + " is my favorite animal!")
      }

  favoriteAnimal('Goat')
  ```
