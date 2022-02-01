#include <string>
#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
vector<string> v1;
vector<string> v2;
map<string, int> m1;
map<string, int> m2;

string lowercase(string s)
{
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}
int solution(string str1, string str2) {
    

    for(int i = 0; i < str1.size() - 1; i++)
    {
        string s = lowercase(str1.substr(i,2));
        if( ( s[0] >= 'a' && s[0] <= 'z') && s[1] >= 'a' && s[1] <= 'z' )
        {
            m1[s] = 0;
            v1.push_back(s);
        }
        
    }
    for(int i = 0; i < str2.size() - 1; i++)
    {
        string s = lowercase(str2.substr(i,2));
        if( ( s[0] >= 'a' && s[0] <= 'z') && s[1] >= 'a' && s[1] <= 'z' )
        {
            
            m2[s] = 0;
            v2.push_back(s);
        }
        
    }
    
    for(int i = 0; i < v1.size(); i++)
    {
        
        m1[v1[i]] ++;
        
    }
    
    for(int i = 0; i < v2.size() ; i++)
    {
        m2[v2[i]] ++;
    }
    
    map<string, int> :: iterator it = m1.begin();
    
    
    it = m2.begin();
    
    
    it = m1.begin();
    int intersect = 0;
    for(;it != m1.end(); it++)//교집합.
    {
        
        if( m2.find(it->first) != m2.end())
        {
            intersect += min(it->second, m2.find(it->first)->second);
        }
    }
    
    int uni = 0;
    vector<pair<string, int>> v(m1.begin(), m1.end());
    for(int i = 0; i < v.size(); i++)//합집합.
    {
        if(m2.find(v[i].first) != m2.end())//m2에 존재하면 max로 값 변경.
        {
            v[i].second = max(v[i].second, m2.find(v[i].first)->second);
            m2.erase(m2.find(v[i].first));
            
        }
        uni += v[i].second;
    }
    
    it = m2.begin();
    for(;it != m2.end(); it++)//합집합.
    {
        uni += it->second;
    }
    
    int answer;
    if(intersect == uni) answer = 65536;
    else answer = ((double) intersect / (double)uni) * 65536;
    
    return answer;
}
