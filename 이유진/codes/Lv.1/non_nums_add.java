class Solution {
    public int solution(int[] numbers) {
        int a = 0;
        int[] arr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        for(int i = 0; i < numbers.length; i++) {
            a = numbers[i];
            arr[a] = 0;
        }
        int answer = 0;
        for(int i = 0; i <10; i++){
            answer += arr[i];
        }
        return answer;
    }
}