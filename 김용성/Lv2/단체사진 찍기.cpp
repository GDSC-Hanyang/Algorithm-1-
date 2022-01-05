#include<iostream>
#include<string>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

char character[8];
char order[8];
bool check[8];
int answer;
void dfs(int cnt, vector<string> data)
{
    
    if(cnt == 8)
    {
        bool real = false;
        for(int i = 0; i < data.size(); i++)
        {
            char a = data[i][0];
            char b = data[i][2];
            
            char condition = data[i][3];
            int num = data[i][4] - '0';
//            cout << a <<" "<< b <<" "<< condition <<" "<< num<<endl;
            
            int idx1 = -1, idx2 = -1;
            
            for(int j = 0; j < 8; j++)
            {
                if(a == order[j]) idx1 = j;
                
                if(b == order[j]) idx2 = j;
                
                if(idx1 != -1 && idx2 != -1) break;
            }
            
//            if(idx)
            if(condition == '>')//초과
            {
                if(num < abs(idx1 - idx2)-1)
                {
                    
                }
                else
                {
                    real = true;
                    break;
                }
            }
            else if(condition == '<')//미만
            {
                if(num > abs(idx1 - idx2)-1)
                {
                    
                }
                else {
                    real = true;
                    break;
                }
            }
            else if(condition == '=')
            {
                if (num == abs(idx1 - idx2) - 1)
                {
                    
                }
                else {
                    real = true;
                    break;
                }
            }
        }
        
        if(real ==false) answer ++;
    }
    else{
        for(int i = 0; i < 8; i++)
        {
            if(check[i] == true) continue;
            check[i] = true;
            order[cnt] = character[i];
            dfs(cnt+1, data);
            check[i] = false;
        }
        
    }
    
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
    character[0] = 'A';
    character[1] = 'C';
    character[2] = 'F';
    character[3] = 'J';
    character[4] = 'M';
    character[5] = 'N';
    character[6] = 'R';
    character[7] = 'T';
    answer = 0;
    int cnt = 0;
    dfs(cnt, data);
    cout <<"answer : " << answer <<endl;
    return answer;
}
