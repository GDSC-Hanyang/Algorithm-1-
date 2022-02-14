class Solution {
    public int solution(String s) {
        int a = 0;
        if(s.charAt(0) == '+') a = 1;
        if(s.charAt(0) == '-') a = -1;
        
        s.replace("+","");
        s.replace("-","");
    
        int answer = Integer.parseInt(s);
        //if(a == -1) answer *= -1;
        
        return answer;
    }
}