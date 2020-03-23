let myArray = ['tomatoes', 'chick peas', 'onions', 'rice', 'black beans'];
let list = document.createElement('ul');

/* Code goes under here */ 

// FOR each item, 
for (let index = 0; index < myArray.length; index++) {
    // append the element to the list as a list item 
    let listItem = document.createElement('li'); 
    listItem.textContent = myArray[index]; 
    
    // append and display the new list item 
    list.appendChild(listItem);

}


// Don't edit the code below here!

const section = document.querySelector('section');
section.appendChild(list);