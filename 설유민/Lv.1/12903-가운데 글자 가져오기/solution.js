function solution(s) {
    return s.length % 2 == 1 ? s[Math.floor(s.length / 2)] : s[s.length / 2 - 1] + s[s.length / 2];
}