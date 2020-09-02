var firstName = "Alan";
var lastName = "Turing";

// using backslash
var myStr = "I am a \"double quoted\" string inside \"double quoted\" string";

console.log(myStr)

// using single code
myStr = 'I am a "double quoted" string inside "double quoted" string';

console.log(myStr)

/*
CODE   OUTPUT
----   ------
\'     single quote
\"     double quote
\\     backslash
\n     newline
\r     carriage return
\t     tab
\b     backspace
\f     from feed
*/

myStr = "FirstLine\n\t\\SecondLine\nThirdLine";
console.log(myStr)

// concatenating string with plus operator
myStr = "I come first. " + "I come second."
console.log(myStr)

// plus equal operator
var ourStr = "I come first. ";
ourStr += "I come second.";

console.log(ourStr)

// concatenate string with variables
var fullName = firstName + " " + lastName;
console.log(fullName)

// find length of string
var fullNameLength = fullName.length;
console.log(fullNameLength)