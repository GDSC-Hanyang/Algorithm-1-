class Solution {
    public String solution(int a, int b) {
        int date = 0;
        for(int i = 1; i < a; i++ ){
            if( i == 2) date += 29;
            if( (i == 1)||(i == 3)||(i == 5)||(i == 7)||(i == 8)||(i == 10)||(i == 12)) date += 31;
            if( (i == 4)||(i == 6)||(i == 9)||(i == 11)) date += 30;
        }
        date += b - 1;
        String answer = "";
        int day = date % 7;
        
        String[] arr = {"FRI","SAT","SUN","MON","TUE","WED","THU"};
        
        answer = arr[day];
        return answer;
    }
}