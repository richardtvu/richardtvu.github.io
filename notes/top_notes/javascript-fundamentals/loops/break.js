const contacts = ['Chris:2232322', 'Sarah:3453456', 'Bill:7654322', 'Mary:9998769', 'Dianne:9384975'];
const paraSearch = document.getElementById('p-search'); 
const inputSearch = document.getElementById('i-search'); 
const btnSearch = document.getElementById('btn-search');

btnSearch.addEventListener('click', function() {
    // Store search value in another variable and clear the input Search variable to facilitate next search
    let searchName = inputSearch.value.toLowerCase(); 
    inputSearch.value = '';
    inputSearch.focus(); 

    
    for (let i = 0; i < contacts.length; i++) {
        let splitContact = contacts[i].split(':'); 
        if (splitContact[0].toLowerCase() === searchName) {
            paraSearch.textContent = splitContact[0] + '\'s number is ' + splitContact[1] + '.'; 
            // Start the loop over from the beginning, after incrementing the index, so that we can check each element in the contacts array 
            break; 
        } else {
            paraSearch.textContent = 'Contact not found';
        }
    }

});

