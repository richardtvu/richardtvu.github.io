/**
 * This program will print out the primes in the interval
 * from 2 to n. 
 */ 

/* Declare variables */ 
let primes;     // The list of primes. 
let i;          // An integer in the interval from 2 to n. 
let n;          // The max number in the interval from 2 to n. 
let j;          // integer to divide i by 
let isPrime;    // Boolean for whether something is prime

/* Initialize variables */ 
primes = "2"; // 2 is automatically prime. 
i = 0;
j = 0; 
n = 10;         // The max in the example. 


/* Check the interval from 3 to n for primes */ 
for ( i = 3; i <= n; i++ ) { // for each integer in the interval 
    // Check if that integer can be divided by anything other than 1 and n
    isPrime = true; 
    for (j = 2; j < i; j++) {
        // Divide i by each integer in the interval 2 to i-1. 
        // If any can be evenly divided, then set isPrime to false 
        if ( i % j == 0 ) {
            isPrime = false; 
            break; 
        }  
        else continue; 
    }
    if (isPrime) {
        primes += "," + i; 
    }

}


/* Print the primes out */ 
print(primes); 

