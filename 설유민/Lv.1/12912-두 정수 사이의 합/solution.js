function solution(a, b) {
    return a >= b ? (a + b) * (a - b + 1) / 2 : (a + b) * (b - a + 1) / 2;
}