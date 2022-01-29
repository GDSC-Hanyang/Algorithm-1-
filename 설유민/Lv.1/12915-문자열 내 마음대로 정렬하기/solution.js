function solution(strings, n) {
    return strings.sort().sort((a, b) => {return a.charCodeAt(n) - b.charCodeAt(n)});
}