/* 
Filling in a guest list 
---------------------------------------------------------
Purpose: This program will take a list of names in a stored array and filter items into a list of guests to refuse and a list of guests to admit. 
---------------------------------------------------------
*/

// create list of names to filter
const people = ['Chris', 'Anna', 'Colin', 'Terri', 'Phil', 'Lola', 'Sam', 'Kay', 'Bruce']; 

// select the admitted list  
const admitted = document.querySelector('.admitted'); 
// select the refused list 
const refused = document.querySelector('.refused'); 
// include 'admitted: ' at the beginning of the list
admitted.textContent = 'Admitted: ';
// include 'refused: ' at beginning of refused list
refused.textContent = 'Refused: '; 

// initialize the loop 

// iterate through people array 
for (let i = 0; i < people.length; i++) {
    let name = people[i]; 
    // IF equal, THEN add item to 'refused' list with a comma and space at the end 
    if (name == 'Phil' || name == 'Lola') {
        refused.textContent += name + ', '; 
    } 
    // ELSE add item to 'admitted' list with a comma and space at the end 
    else {
        admitted.textContent += name + ', '; 
    }
}

let refusedList = refused.textContent;
let refusedListEnd = refusedList.length -2; 
refusedList = refusedList.slice(0, refusedListEnd);
refused.textContent = refusedList + '.';

let admittedList = admitted.textContent; 
let admittedListEnd = admittedList.length -2; 
admittedList = admittedList.slice(0, admittedListEnd); 
admitted.textContent = admittedList + '.'; 