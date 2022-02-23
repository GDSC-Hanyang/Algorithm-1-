#include <string>
#include <vector>
#include <math.h>
using namespace std;
//1000000 0000000

long long sqrt2(long long n)
{
    bool flag = false;
    long long i;
    for( i = 1; i <= 10000000; i++)
    {
         if( n == i * i)
         {
             flag = true;
             break;
         }
    }
    if(flag) return (i+1) * (i+1);
    else return -1;
}
long long solution(long long n) {
    long long answer = 0;
    
    answer = sqrt2(n);
    
    
    return answer;
}

