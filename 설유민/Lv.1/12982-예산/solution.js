function solution(d, budget) {
    let answer = 0;
    d = d.sort((a, b) => {return a - b});
    for (let i = 0; i < d.length; i++) {
        if (d[i] > budget) {
            break;
        }
        budget -= d[i];
        answer += 1;
    }
    return answer;
}