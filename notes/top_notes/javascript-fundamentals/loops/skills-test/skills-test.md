# Solutions/Work on Skills Test


1. Loop 1

    ```javascript
    <script>
    let myArray = ['tomatoes', 'chick peas', 'onions', 'rice', 'black beans'];
    let list = document.createElement('ul');

    // Add your code here
    for (let i = 0; i < myArray.length; i++) {
        let bullet = document.createElement('li'); 
        bullet.textContent += myArray[i];
        list.appendChild(bullet); 
    }

    // Don't edit the code below here!

    const section = document.querySelector('section');
    section.appendChild(list);
    </script>
    ```

2. Loop 2

    - Instructions: In this next task, we want you to write a simple program that, given a name, searches an array of objects containing names and emails (phonebook) and, if it finds the name, outputs the name and phone number into the paragraph (para) and then exits the loop before it has run its course. 