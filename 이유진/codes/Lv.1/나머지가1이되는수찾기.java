class Solution {
    public int solution(int n) {
        n -= 1;
        int answer = 2;
        while(true){
            if(n%answer == 0) break;
            else answer++;
        }
        return answer;
    }
}