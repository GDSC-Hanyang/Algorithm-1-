import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] numbers) {
        //int[] answer = {};
        ArrayList<Integer> tmp_arr = new ArrayList<>();
        for(int i = 0; i < numbers.length; i++)
            for(int j = 0; j < numbers.length; j++){
                if(i == j) break;
                int sum = numbers[i] + numbers[j];
                if(tmp_arr.contains(sum) == false) 
                    tmp_arr.add(sum);
            }
        Collections.sort(tmp_arr);
        int len = tmp_arr.size();
        int[] answer = new int[len];
        for(int i = 0; i < len; i++)
            answer[i] = tmp_arr.get(i);
        return answer;
    }
}