import java.util.ArrayList;
class Solution {
    public int solution(int n) {
        ArrayList<Integer> integer1 = new ArrayList<>();
        while(n != 0){
            integer1.add(n%3);
            n = n/3;
        }
        int answer = 0;
        for(int i = 0; i < integer1.size(); i++){
            answer += integer1.get(integer1.size()-1-i)*Math.pow(3,i);
        }
        return answer;
    }
}