#include <string>
#include <vector>
#include <stdio.h>
#include <iostream>
#include <string>
#include <utility>
#include <map>

using namespace std;
map<string, string> s;
vector<pair<string, string>> change;
vector<pair<string, string>> p;

vector<string> solution(vector<string> record) {
    vector<string> answer;
    
    for(int i = 0 ;i < record.size(); i++)
    {
        size_t index = 0;
        size_t current;
        current = record[i].find(' ', index);
        if( (index = record[i].find("Enter")) != string::npos)
        {
            
            index = current + 1;
            current = record[i].find(' ', index);
            
            string id = record[i].substr(index, current - index);
            index = current + 1;
            current = record[i].find(' ', index);
            
            string name = record[i].substr(index, current - index);
            s[id] = name;
            
//            change.push_back(make_pair(id, name));
            p.push_back(make_pair(id, "님이 들어왔습니다."));
//            cout << id << " " << name<<endl;
            
        }
        else if( (index = record[i].find("Change")) != string::npos)
        {
            index = current + 1;
            current = record[i].find(' ', index);
            
            string id = record[i].substr(index, current - index);
            index = current + 1;
            current = record[i].find(' ', index);
            
            string name = record[i].substr(index, current - index);
            
            s[id] = name;
//            cout << id << " " << name<<endl;
        }
        else // Leave
        {
            index = current + 1;
            current = record[i].find(' ', index);
            string id = record[i].substr(index, current - index);
            p.push_back(make_pair(id, "님이 나갔습니다."));
        }
    }
    
   
    for(int i = 0; i < p.size(); i++)
    {
        answer.push_back(s[p[i].first] + p[i].second);
    }
    
    
    return answer;
}
