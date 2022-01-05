#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    int answer = 0;
    
    size_t size = s.size();
    string res;
    string temp;
    for(int i = 0; i < size; i++)
    {
        if(s[i] >= 48 && s[i] <=57)//숫자.
        {
            res += s[i];
        }
        else{
            
            temp += s[i];
            
            if(temp == "zero")
            {
                res += "0";
                temp.clear();
            }
            else if(temp == "one")
            {
                res += "1";
                temp.clear();
            }
            else if(temp == "two")
            {
                res += "2";
                temp.clear();
            }
            else if(temp == "three")
            {
                res += "3";
                temp.clear();
            }
            else if(temp == "four")
            {
                res += "4";
                temp.clear();
            }
            else if(temp == "five")
            {
                res += "5";
                temp.clear();
            }
            else if(temp == "six")
            {
                res += "6";
                
                temp.clear();
            }
            else if(temp == "seven")
            {
                res += "7";
                temp.clear();
            }
            else if(temp == "eight")
            {
                res += "8";
                temp.clear();
            }
            else if(temp == "nine")
            {
                res += "9";
                temp.clear();
            }
        }
        
    }
    
    answer = stoi(res);
    
    return answer;
}
