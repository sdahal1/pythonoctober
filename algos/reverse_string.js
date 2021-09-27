var greeting = "hello hay hi how you durrring"


//start at last index of the input string
//put the value from the last index into the resulting string
//put in a loop this process and repeat unitl we reach index 0: 
    //decrement the index nubmer by 1 and put the value from that index into the resulting string



""

function reverseString(stringInput){
    // console.log(stringInput[stringInput.length-1])
    var result = ""
    for(var i = stringInput.length-1; i>=0; i-- ){
        // console.log(stringInput[i])
        result += stringInput[i]
    }
    console.log(result)
    return result
}

reverseString(greeting)
reverseString("hello there")
reverseString("potato")










