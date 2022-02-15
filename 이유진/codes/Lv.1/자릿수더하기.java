import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        /*
        int len = (int)(Math.log10(n)+1);
        //System.out.print(len);

        int a = (int)Math.pow(10, len-1);
        
        for(int i = 0; i < len; i++){
            answer += n/a;
            n -= (n/a)*a;
            a = a/10;
        }
        */
        while(n!=0){
            answer += n%10;
            n = n/10;
        }
        return answer;
    }
}