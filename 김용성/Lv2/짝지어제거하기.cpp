#include <iostream>
#include<string>
#include <vector>

using namespace std;

int solution(string s)
{
    int answer = -1;
    vector<char> v;
    v.push_back(s[0]);
    for(int i = 1; i < s.size(); i++)
    {
        v.push_back(s[i]);
        size_t size = v.size();
        if(v[size - 1] == v[size - 2])
        {
//            cout << "before : " << s << endl;
            v.pop_back();
            v.pop_back();
//            cout << "after : "<< s << endl;
        }
//        cout <<  endl;
    }
    if(v.size() == 0) answer = 1;
    else answer = 0;
    return answer;
}
