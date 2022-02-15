class Solution {
    public String solution(String s) {
        String answer = "";
        int a = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == ' ') {
                a = -1;
                answer += " ";
            }else if(a%2 == 0) //짝수
                answer += Character.toUpperCase(s.charAt(i));
            else answer += Character.toLowerCase(s.charAt(i));
            a++;
        }
        return answer;
    }
}