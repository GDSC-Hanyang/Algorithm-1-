function solution(sizes) {
    let side1 = 0;
    let side2 = 0;
    for (let i = 0; i < sizes.length; i++) {
        sizes[i] = sizes[i].sort((a, b)=>{return a-b;});
        if (side1 < sizes[i][0]) side1 = sizes[i][0];
        if (side2 < sizes[i][1]) side2 = sizes[i][1];
    }
    return side1 * side2;
}