function solution(a, b) {
    let dayWk = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"];
    let days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    return dayWk[(days.slice(0, a - 1).reduce((sum, month)=>{return sum + month;}, 0) + b) % 7];
}