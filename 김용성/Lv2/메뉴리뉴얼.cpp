#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>

using namespace std;
map<string, int> m;
bool compare(pair<string, int> a, pair<string, int> b)
{
    
    return a.second > b.second;
}

void comb(int index, int order_size, int course_size, string s, string order)
{
    if(course_size == s.size())
    {
        m[s]++;
        return;
    }
    
    for(int i = index; i < order_size; i++)
    {
        s += order[i];
        comb( i + 1, order_size, course_size, s, order );
        s.pop_back();
    }
}
vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    
    for(int i = 0; i < course.size(); i++)
    {
        m.clear();
        for(int j = 0; j < orders.size(); j++)
        {
            sort(orders[j].begin(), orders[j].end());
            
            comb( 0, (int) orders[j].size(), course[i], "", orders[j] );
        }
        vector<pair<string, int>> vis(m.begin(), m.end());
        sort(vis.begin(), vis.end(), compare);
        for(int k = 0; k < vis.size(); k++)
        {
            cout << vis[k].first << " "<< vis[k].second << " ";
            
        }
        cout << endl;
        if(vis.size() == 0) continue;
        int idx = vis[0].second;
        if(idx >= 2) 
        {
            for(int k = 0; k < vis.size(); k++)
            {
                if(vis[k].second == idx)
                {
                    answer.push_back(vis[k].first);
                }
                else break;
            }
        }
        
    }
    sort(answer.begin(), answer.end() );
    return answer;
}
