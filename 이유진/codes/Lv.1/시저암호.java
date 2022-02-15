class Solution {
    public String solution(String s, int n) {
        
        String answer = "";
        int a = 0;
        for(int i = 0; i < s.length(); i++){
            //공백이면 걍 더하기
            if((int)s.charAt(i)==32) answer += " ";
            else{
                a = (int)s.charAt(i) + n;
                if((int)s.charAt(i) <=90)
                    if(a > 90 ) a -= 26;
                if((int)s.charAt(i) > 90)
                    if(a > 122) a-= 26;
                answer += (char)a;
            }
        }
        return answer;
    }
}