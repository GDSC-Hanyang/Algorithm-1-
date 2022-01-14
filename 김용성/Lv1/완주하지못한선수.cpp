#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <utility>
#include <map>

using namespace std;

typedef vector<string> vi;
//completion에 도착한애들, participant에 모든참가자.
//completion + 1 = participant

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> m;
    
    for(int i = 0; i < participant.size(); i++)
    {
        m[ participant[i] ] = 0;
    }
    for(int i = 0; i < participant.size(); i++)
    {
        m[ participant[i] ] ++;
    }
    for(int i = 0; i < completion.size(); i++)
    {
        m[ completion[i] ] --;
    }
    for(int i = 0; i < participant.size(); i++)
    {
        if( m[ participant[i] ] ==1)
        {
            answer += participant[i];
            break;
        }
    }
    
    return answer;
}

