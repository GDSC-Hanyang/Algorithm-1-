#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef vector<int> vi;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vi v;
    for(int i = 0; i < speeds.size(); i++)
    {
        int remain = 100 - progresses[i];
        int days = remain / speeds[i];
        if(remain % speeds[i] != 0) days++;
        v.push_back(days);
    }
    for(int i = 0; i < v.size(); i++)
    {
        printf("%d ", v[i]);
    }
    printf("\n");
    for(int i = 0; i < speeds.size(); i++)
    {
        int start = v[i];
        cout <<"start : " << start;
        int cnt = 1;
        int j;
        for( j = i + 1; j < speeds.size(); j++ )
        {
            if(start >= v[j]) cnt++;
            else break;
        }
        answer.push_back(cnt);
        i = j - 1;
    }
    
    for(int i = 0; i < answer.size(); i++)
    {
        printf("%d ", answer[i]);
    }
    return answer;
}
