function solution(n, arr1, arr2) {
    let answer = [];
    for (let i = 0; i < n; i++) {
        answer.push((arr1[i] | arr2[i]).toString(2).padStart(n, '0').replace(/0/g, ' ').replace(/1/g, '#'));
    }
    return answer;
}