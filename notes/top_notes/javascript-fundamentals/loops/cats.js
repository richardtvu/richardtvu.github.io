let cats = [];
let message = 'My cats are called '; 
const paraCat = document.getElementById('cat-display'); 
const btnAddCat = document.getElementById('add-cat'); 
const btnDisplayCat = document.getElementById('display-cats'); 
const catInput = document.getElementById('cat-input'); 

btnAddCat.addEventListener('click', function() {
    let input = catInput.value;
    if ( typeof(input) === "string" ) {
        paraCat.textContent = '';
        cats.push(input);
        paraCat.textContent = "You've added " + input; 
    } else {
        paraCat.textContent = "You didn't input a number. Try again."
    }

});

btnDisplayCat.addEventListener('click', function() {
    let lastCat = cats.length - 1; 
    for (let eachCat = 0; eachCat < cats.length; eachCat++) {
        if (eachCat < lastCat) {
            message += cats[eachCat] + " "; 
        } else {
            message += cats[eachCat] + '.';
        }
    }
    if (cats.length > 1) {
        paraCat.textContent = message;
    } else {
        paraCat.textContent = "My cat is called " + catInput.value; 
    }
    
});