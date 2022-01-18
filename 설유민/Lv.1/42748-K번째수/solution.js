function solution(array, commands) {
    let answer = [];
    for (let arrIndex = 0; arrIndex < commands.length; arrIndex++) {
        answer.push(array.slice(commands[arrIndex][0] - 1, commands[arrIndex][1]).sort((a, b)=>{return a - b})[commands[arrIndex][2] - 1]);
    }
    return answer;
}