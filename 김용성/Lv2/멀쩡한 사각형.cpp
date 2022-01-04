#include <stdio.h>

using namespace std;

long long gcd(long long a, long long b)
{
    while(b != 0)
    {
        long long temp = a;
        a = b;
        b = temp % b;
    }
    return a;
    
}

long long solution(int w,int h) {
    
    long long a = (long long) w;
    long long b = (long long) h;
    long long answer = 1;
    answer =  a*b - (a + b - gcd(a, b) ) ; //a*b가 int이면 overflow 발생. 따라서 Long long으로 바꿔서 하기. 
    
    return answer;
}
