function solution(s) {
    return /^\d+$/.test(s) && (s.length == 4 || s.length == 6);
}