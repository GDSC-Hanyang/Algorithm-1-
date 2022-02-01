#include <string>
#include <vector>

using namespace std;

string solution(int a, int b) {
    //1월 31
    //2월 29
    //3월 31
    //4월 30
    //5월 31
    //6월 30
    //7월 31
    //8월 31
    //9월 30
    //10월 31
    //11월 30
    //12월 31
    //cnt 0이면 금요일
    //cnt 1이면 토
    //cnt 2이면 일
    //cnt 3이면 월
    //cnt 4이면 화
    //cnt 5이면 수
    //cnt 6이면 목
    
    
    int cnt = 0;
    bool flag = false;
    for(int i = 1; i<=12; i++)
    {
        for(int j = 1; j <=31; j++)
        {
            
            if(i == 2)
            {
                if(j >29) break;
            }
            else if(i == 4)
            {
                if(j > 30) break;
            }
            else if(i == 6)
            {
                if(j > 30) break;
            }
            else if(i == 9)
            {
                if(j > 30) break;
            }
            else if(i == 11)
            {
                if(j > 30) break;
            }
            
            if(i == a && j == b)
            {
                flag = true;
                break;
            }
            cnt++;
            if(cnt == 7) cnt =0;
        }
        if(flag) break;
    }
    string answer = "";
    if(cnt == 0)
    {
        answer = "FRI";
    }
    else if(cnt == 1)
    {
        answer = "SAT";
    }
    else if(cnt == 2)
    {
        answer = "SUN";
    }
    else if(cnt == 3)
    {
        answer = "MON";
    }
    else if(cnt == 4)
    {
        answer = "TUE";
    }
    else if(cnt == 5)
    {
        answer = "WED";
    }
    else if(cnt == 6)
    {
        answer = "THU";
    }
    
    return answer;
}
