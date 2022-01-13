function solution(answers) {
    let answer = [];
    let count = [0, 0, 0];
    const firstPattern = [1, 2, 3, 4, 5];
    const secondPattern = [2, 1, 2, 3, 2, 4, 2, 5];
    const thirdPattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] == firstPattern[i % 5]) {
            count[0] += 1;
        }
        if (answers[i] == secondPattern[i % 8]) {
            count[1] += 1;
        }
        if (answers[i] == thirdPattern[i % 10]) {
            count[2] += 1;
        }
    }
    for (let i = 0; i < 3; i++) {
        if (count[i] == Math.max(...count)) answer.push(i + 1);
    }
    return answer;
}
