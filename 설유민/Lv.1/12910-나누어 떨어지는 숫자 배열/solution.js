function solution(arr, divisor) {
    arr = arr.sort((a,b)=>{return a-b});
    let answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] / divisor == parseInt(arr[i] / divisor)) answer.push(arr[i]);
    }
    return answer.length > 0 ? answer : [-1];
}

/*
function solution(arr, divisor) {
    let answer = arr.filter(n => (n / divisor == parseInt(n / divisor))).sort((a, b) => {return a - b});
    return answer.length > 0 ? answer : [-1];
}
*/