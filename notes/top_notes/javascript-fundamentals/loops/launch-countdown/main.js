// select an area on the webpage where the countdown will be displayed 
let output = document.querySelector('.output'); 
// set the text in the area to be empty 
output.innerHTML = ''; 

// initialize the variable to keep track of the countdown
let i = 10; 

// loop down from 10 down to 0,
while (i >= 0) {
    //     initialize a new paragraph 
    const para = document.createElement('p'); 
    //     IF the number is 10, add "Countdown 10" to the paragraph,
    if (i === 10) {
        para.textContent = 'Countdown 10'; 
    }
    //     ELSE IF the number is 0, add "Blast off!" to the paragraph,
    else if (i === 0) {
        para.textContent = 'Blast off!';
    }
    //     ELSE add just the number to the paragraph. 
    else {
        para.textContent = i; 
    }

    //     display the new paragraph
    output.appendChild(para); 

    //     decrease the number by 1 for each loop  
    i--;
}

