#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
bool comp(int a, int b)
{
    
    return a > b;
}
vector<int> solution(long long n) {
    vector<int> answer;
    
    while(n != 0 )
    {
        answer.push_back(n % 10);
        n = n / 10;
    }
    return answer;
}
