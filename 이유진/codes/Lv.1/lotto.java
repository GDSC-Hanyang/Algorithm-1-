class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        
        int zer_num = 0; // 0의 개수
        int ans = 0; // 일치하는 것의 개수
        for(int i=0; i<6; i++){
            if(lottos[i] == 0) zer_num ++;
            for(int j = 0; j<6; j++){
                if(win_nums[j] == lottos[i]){
                    ans++;
                    break;
                }else continue;
            }
        }
        
        int max = zer_num + ans;
        int min = ans;
        int max_result, min_result;
        
        if((7-max)>=6){
            max_result = 6;
        }else max_result = 7-max;
        
        if((7-min)>=6){
            min_result = 6;
        }else min_result = 7-min;
         
        int[] answer = new int[2];
        answer[0] = max_result;
        answer[1] = min_result;
        return answer;
    }
}