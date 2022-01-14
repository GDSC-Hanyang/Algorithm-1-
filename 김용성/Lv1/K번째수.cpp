#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;

typedef vector<int> vi;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    vector<int> answer;
    
    for(int i = 0; i < commands.size(); i++)
    {
        int start = commands[i][0];
        int end = commands[i][1];
        vi v;
        for(int j = start; j <= end ; j++)
        {
            v.push_back(array[j-1]);
        }
        sort(v.begin(), v.end());
        
        int pick = commands[i][2] - 1;
        
        answer.push_back( v[pick] );
        v.clear();
    }
    
    
    
    return answer;
}

