class Solution { //다시 하기
    public String solution(int[] numbers, String hand) {
        
        int[] column = {3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3};
        int[] row = {1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 2};
        //0, 1, 2, 3, 4, 5, 6, 7, 8, 9, *, #
        //*: 10, #: 11
        int L_status = 10;
        int R_status = 11;
        String answer = "";
        
        for(int i = 0; i < numbers.length; i++){
            
            if(numbers[i]==1 || numbers[i]==4 ||numbers[i]==7){
                answer += 'L';
                L_status = numbers[i];
            }
            
            if(numbers[i]==3 || numbers[i]==6 || numbers[i] == 9){
                answer += 'R';
                R_status = numbers[i];
            }
            
            else {
                int a, L_distance, R_distance, L_c, L_r, R_c, R_r;
                a = numbers[i];
                L_c = column[a]-column[L_status];
                L_r = row[a]-row[L_status];
                R_c = column[a]-column[R_status];
                R_r = row[a]-row[R_status];
                L_distance = Math.abs(L_c) + Math.abs(L_r);
                R_distance = Math.abs(R_c) + Math.abs(R_r);
                
                if(L_distance < R_distance){
                    answer += 'L';
                    L_status = numbers[i];
                }
                if(L_distance > R_distance){
                    answer += 'R';
                    R_status = numbers[i];
                }
                if(L_distance == R_distance){ 
                    if(hand == "left"){
                         answer += 'L';
                         L_status = numbers[i];
                    }
                    if(hand == "right"){
                         answer += 'R';
                         R_status = numbers[i];
                    }
                    
                }
            }
            
            continue;
        }
        
        return answer;
    }
}