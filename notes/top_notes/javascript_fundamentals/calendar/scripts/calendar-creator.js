// Check out https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals for script 

const select = document.querySelector('select');
const list = document.querySelector('ul');
const h1 = document.querySelector('h1');

select.onchange = function() {
    const choice = select.value; 

    // ADD CONDITIONAL HERE
    if ( choice === 'february' ) {
        days = 28; 
    } else if ( choice === 'april' || choice === 'june' || choice === 'september' || choice === 'november') {
        days = 30; 
    } else {
        days = 31; 
    }


    createCalendar(days, choice); 
}

function createCalendar(days, choice) {
    list.innerHTML = '';
    h1.textContent = upperCaseFirstLetter(choice); 
    for (let i = 1; i <= days; i++) {
        const listItem = document.createElement('li'); 
        listItem.textContent = i; 
        list.appendChild(listItem); 
    }
}

function upperCaseFirstLetter(choice) {
    choice = choice.charAt(0).toUpperCase() + choice.slice(1);
    return choice; 
}

createCalendar(31, 'January'); 

