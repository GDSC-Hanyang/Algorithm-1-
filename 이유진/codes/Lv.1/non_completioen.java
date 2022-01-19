class Solution { //효율성 테스트 통과하지 못함
    public String solution(String[] participant, String[] completion) {
        int len = participant.length;
        
        for(int i = 0; i < len - 1; i++){
            for(int j = 0; j < len; j++){
                if(completion[i].equals(participant[j])){
                    participant[j] = null;
                    break;
                }else continue;
            }
        }
        
        String answer = "";
        
        for(int i = 0; i < participant.length; i++){
            if(participant[i] != null) answer = participant[i];
        }
        return answer;
    }
}