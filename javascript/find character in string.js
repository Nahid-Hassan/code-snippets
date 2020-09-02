// using bracket notation find first character into the string

var word = "love";
var firstCharacter = word[0];
console.log(firstCharacter)

// string are immutable
word[0] = 'L';
console.log(word) // no change

// bracket notation to find nth character
var secondCharacter = word[1]
console.log(secondCharacter)

// find last character
var lastCharacter = word[word.length - 1]
console.log(lastCharacter)