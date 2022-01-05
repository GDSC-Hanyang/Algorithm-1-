#include <string>
#include <vector>

#include <iostream>

using namespace std;

long long pow2(int x, int y)
{
    int res = 1;
    for(int i = 0 ; i < y; i++)
    {
        res = res * x;
    }
    return res;
}
string solution(int n) {
    string answer = "";
    int i;
    long long num;
    for( i = 1 ; i < 21; i ++)
    {
        num = ( pow2(3, i + 1 ) - 3) / 2;
        if( num  >= n) break;
    }
    
    //n이 이라면
    //i는 2
    //num은 3
    
    
    num = (pow2(3, i ) - 3) / 2;//기준.
    cout << i << endl;
//    cout <<n << endl;
    long long range = pow2(3, i - 1);
//    num += 1;
    while(range != 0)
    {
        if( num + 2 * range < n)
        {
            answer +="4";
            num = num + 2 * range;
        }
        else if(num + range < n)
        {
            answer +="2";
            num = num + range;
        }
        else
        {
            answer +="1";
        }
        range /= 3;
    }
    
    
    return answer;
}
