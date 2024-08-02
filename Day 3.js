function returnOddsArray1To255(){
    //declare a variable for a new array
    var new_arr = []
    //loop through the array from 0 - 255
    for (var i = 0; i <= 255; i++){
        //determine if it is odd 
        if (i % 2 == 1){
            //push the odd values into the new array
            new_arr.push(i)
        }
    }
    return new_arr
}
//log the function
console.log(returnOddsArray1To255())

function zeroOutArrayNegativeVals(arr){
//loop through the array
    for (var i = 0; i < arr.length; i++){
        //find out if the index value is positive
        if (arr[i] < 0){
            //set negative values to 0
            arr[i] = 0
        }
    }
    return arr
}
//log the function
console.log(zeroOutArrayNegativeVals([3,-2,-1,0,1,2,-3]))

function reverseArray(arr){
    //loop through the array to the middle
    for (var left_idx = 0; left_idx < Math.floor(arr.length) / 2; left_idx ++){
        //find the end of the array
        var right_idx = arr.length - 1 - left_idx
        //set the temp variable to the left side to hold it
        var temp = arr[left_idx];
        //reassign the left side to the right side
        arr[left_idx] = arr[right_idx];
        //reassigning temp to the left side
        arr[right_idx] = temp
}
return arr
}
//log the function
console.log(reverseArray([1,2,3,4,5,6,7,8]))