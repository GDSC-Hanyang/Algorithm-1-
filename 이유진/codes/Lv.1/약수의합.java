class Solution {
    public int solution(int n) {
        
        int answer = 0;
        int a = n, i = 1;
        
        while(i < a){
            if(n%i == 0){ 
                answer += i;
                answer += n/i;
                a = n/i;
                if(i == n/i) answer-=i;
            }
            i++;
        }
        if(n == 1) answer = 1;
        return answer;
    }
}