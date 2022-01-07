class Solution {
    public int solution(String s) {
        int answer = 0;
        String tmp_ans = "";
        char[] arr = s.toCharArray();
        
        String tmp = "";
        for(int i = 0; i<=arr.length; i++){
                    switch(tmp){
                        case "zero":
                            tmp_ans += '0';
                            tmp = "";
                            break;
                        case "one":
                            tmp_ans += '1';
                            tmp = "";
                            break;
                        case "two":
                            tmp_ans += '2';
                            tmp = "";
                            break;
                        case "three":
                            tmp_ans += '3';
                            tmp = "";
                            break;
                        case "four":
                            tmp_ans += '4';
                            tmp = "";
                            break;
                        case "five":
                            tmp_ans += '5';
                            tmp = "";
                            break;
                        case "six":
                            tmp_ans += '6';
                            tmp = "";
                            break;
                        case "seven":
                            tmp_ans += '7';
                            tmp = "";
                            break;
                        case "eight":
                            tmp_ans += '8';
                            tmp = "";
                            break;
                        case "nine":
                            tmp_ans += '9';
                            tmp = "";
                            break;       
                        default:
                            break;
                    }
            if(i != arr.length){
            if(Character.isDigit(arr[i])) 
                tmp_ans += arr[i];
            else
                tmp += arr[i];
            }
        }
        answer = Integer.parseInt(tmp_ans);
        return answer;
    }
}