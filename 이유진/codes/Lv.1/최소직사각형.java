class Solution {
    public int solution(int[][] sizes) {
        int num = sizes.length;
        int tmp = 0;
        for(int i = 0; i < num; i++){
            if(sizes[i][0] >= sizes[i][1]) continue;
            else {
                tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        int w = 0, h = 0;
        for(int i = 0; i < num; i++){
            if(w < sizes[i][0]) w = sizes[i][0];
            if(h < sizes[i][1]) h = sizes[i][1];
        }
        int answer = w*h;
        return answer;
    }
}