class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        int num = left;
        while(num <=  right){
            int n = 0;
            for(int i = 1; i <= num; i++){
                if(num%i == 0) n++;
            }
            if(n%2 == 0) answer += num;
            if(n%2 != 0) answer -= num;
            num++;
        }
        return answer;
    }
}