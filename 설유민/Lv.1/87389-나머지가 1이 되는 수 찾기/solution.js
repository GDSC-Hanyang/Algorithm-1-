function solution(n) {
    for (let i = 0; i <= parseInt(Math.sqrt(n)); i++) {
        if (n % i == 1) return i;
    }
    return n - 1;
}

/*
function solution(n) {
    for (let i = 0; i <= n >> 1; i++) {
        if (n % i == 1) return i;
    }
    return n - 1;
}
*/