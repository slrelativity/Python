/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

function reverse_string(str){
    if (str.length < 1){ //Edge if string length is less than 1
        return str
    }
   
    var new_string = ""  //Looking to create a new variable to hold the new string
    for (var i = str.length - 1;  i >= 0; i--){ //Loop through the string starting from the last index
        new_string += str[i]; //Concatinating new string with the new character
    }
    return new_string //Returning newly created string
}

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "cat";
const expected2 = "tac";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

console.log(reverse_string(str1))
console.log(reverse_string(str2))
console.log(reverse_string(str3))
console.log(reverse_string(str4))
// 1. Driver 🚗
// 2. Presenter 👩‍💻
// 3. Navigator 🧭

// take 5-8 mins to write the pseudocode here:


// create the function and decide what params it needs and what it will return


var myArr =  [11,22,33,44]
var expected = [44,33,22,11] 

function reverseArr(arr) {
  // write your sudo code here
}