#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;


void func2(string s, string& u, string& v)
{
    int l = 0, r = 0;
    
    int idx;
    for(idx = 0; idx < s.size(); idx++)
    {
        if(s[idx] == '(')
        {
            u += s[idx];
            l++;
        }
        else if(s[idx] == ')')
        {
            u += s[idx];
            r++;
        }
        if(l == r)
        {
            break;
        }
    }
    if(idx+1 >= s.size()  ) v = "";
    else v = s.substr(idx+1);
}



bool func3(string u)
{
    stack<char> st;
    bool flag = true;

    if(u[0] == ')')
    {
        return false;
    }
    else
    {
        st.push(u[0]);
        
        for(int i = 1; i < u.size(); i++)
        {
            if(u[i] == '(')
            {
                st.push(u[i]);
            }
            else
            {
                if(st.empty())
                {
                    flag = false;
                    break;
                }
                st.pop();
            }
        }
        
        if(flag == false)// 올바른 괄호 문자열이 아니라면.
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    
}

string recur(string s, int index)
{
    
    string res = "";
    
    
    if(s.size() == 0)
    {
        cout << "empty"<<endl;
        return "";
    }
    
    string u = "", v = "";
    
    func2(s, u, v);//짝이 맞는 첫번째 괄호가 되어야한다.
    cout << u << " "<< v <<endl;
    if(func3(u))// 올바른 괄호 문자열이면,
    {
        res += u;
        res += recur(v, index + 1);
    }
    else
    {
        
        res += "(";
        res += recur(v, index + 1);
        res += ")";
        u.pop_back();
        u = u.substr(1);

        string tmp = "";
        for(int i = 0; i < u.size(); i++)
        {
            if(u[i] == '(')
            {
                tmp += ")";
            }
            else tmp += "(";
        }
        res += tmp;
    }
    return res;
}
string solution(string p) {
    string answer = "";
    
    answer = recur(p, 0);
    cout << answer;
    
    return answer;
}
