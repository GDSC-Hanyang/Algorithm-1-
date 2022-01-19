import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = {};
     
        for(int i = 0; i < commands.length; i++){// commands 길이만큼 돌아야 한다
            //Step 0. i, j, k를 찾기 
            int i_1 = commands[i][0];
            int j_1 = commands[i][1];
            int k_1 = commands[i][2];
            //Step 1. 임시 배열 만들기
            int[] tmp_arr = {};
            for(int j =0; j < j_1 - i_1 + 1; j++){
                tmp_arr[j] = array[j+i_1];
            }
            //Step 2. 정렬하기
            Arrays.sort(tmp_arr);
            //Step 3. k_1번째 것 answer에다가 넣기
            answer[i] = tmp_arr[k_1-1];
            
        }
        return answer;
    }
}