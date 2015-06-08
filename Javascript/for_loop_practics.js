// --------The following are loop practice problems from codecademy---------

// prints 1 through 10 to console
for (var counter = 1; counter < 11; counter++) {
	console.log(counter);
}

// prints 5 to 50 in increments of 5 to console
for (var i = 5; i < 51; i += 5) {
	console.log(i);
}

// 8 to 120 in increments of 12, stops at 116
for (var i = 8 ; i < 120; i += 12) {
	console.log(i);
}

// counts down from 10
for (var i = 10; i >= 0; i--) {
	console.log(i);
}

// Once more, for practice: write a for loop that gets the computer to count down from 100 until 0 by 5.
// This time, make sure not to print 0.
for (var counter = 100; counter >= 0; counter -= 5) {
    console.log(counter);
    }