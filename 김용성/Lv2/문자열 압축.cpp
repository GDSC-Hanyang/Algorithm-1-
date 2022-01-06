#include <string>
#include <vector>
#include <stdio.h>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = s.size();
    int size = s.size();
    
    string criteria;

    
    for(int i = 1; i <= (size/2) ; i++)
    {
        int cnt = size;
        bool check = false;
        int index = 0;
        int repeat = 1;
        criteria.clear();
        
        for(int j = 0; j < i; j++)
        {
            criteria += s[j];
        }
        index = index + i;
        
        bool condition = false;
        for(; index < size;)
        {
            string compare;
            compare.clear();
            
            for(int k = index; k < index + i; k++)
            {
                if(k >= size)
                {
                    condition = true;
                    break;
                }
                compare += s[k];
            }
            
            if(condition == true)
            {
                break;
            }
            index = index + i;

            if(criteria == compare)
            {
                if(check == true)
                {
                    cnt = cnt - i;
                }
                else
                {
                    cnt = cnt - i + 1;
                    check = true;
                }
                repeat++;
                if(repeat == 10 || repeat == 100 || repeat ==1000)
                {
                    cnt++;
                }
            }
            else
            {
                criteria = compare;
                repeat = 1;
                check = false;
            }
        }
        if(cnt < answer)
        {
            answer = cnt;
        }
    }
    
    return answer;
}
