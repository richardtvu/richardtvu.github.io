
const inputSquares= document.getElementById("number-entry");
const btnSquares = document.getElementById("btn-generate-squares"); 
const paraSquares = document.getElementById('squares'); 

btnSquares.addEventListener('click', function() {
    let number = inputSquares.value; 

    for (let i = 1; i <= number; i++) {
        let sqRoot = Math.sqrt(i); 
        if (Math.floor(sqRoot) != sqRoot) {
            continue; 
        } else {
            paraSquares.textContent += i + ' '; 
        }
    }

});
