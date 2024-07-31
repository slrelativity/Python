//create a count variable
function greaterThanY(arr,y){
    var count = 0
    for (var i = 0; i < arr.length; i++){
        //loop through the array
        if (arr[i] > y){
            //test to see if the index value is greater than the given y value
            // console.log(arr[i])
            //log the numbers greater than y
            count += 1
            //add to the count if index value is greater than y value
        } 
    }
    return count;
    //return the final count
}
console.log(greaterThanY([1,2,3,4,5,6,7], 5))
//log the function



//create a count variable
function printMaxMinAverageArrayVals(arr){
    var min = arr[0]
    var max = arr[0]
    var sum = arr[0]
    var avg = 0
    //loop through the array
    for (var i = 1; i < arr.length; i++){
        //find the smallest index value
        if (arr[i] < min){
            min = arr[i]
        }
        //find the largest index value
        if (arr[i] > max){
            max = arr[i]
        }
        sum = sum + arr[i]
    }
    //log minimum and maximum
    console.log("Minimum =", min)
    console.log("Maximum =", max)
    //calculate the average index value
    avg = sum / arr.length
    return avg
}
console.log(printMaxMinAverageArrayVals([-7,2,3,1,5,6,4]))
//log the function

function shiftArrayValuesLeft(arr){
    //loop through the array
    for (var i = 0; i < arr.length; i++){
        //copy the next value over to where i is currently at
            arr[i] = arr[i + 1]
        //assign the new index position
            
    }
    arr[arr.length - 1] = 0
    // console.log(arr)
    return arr
}
console.log(shiftArrayValuesLeft([2,9,7,8,4]))