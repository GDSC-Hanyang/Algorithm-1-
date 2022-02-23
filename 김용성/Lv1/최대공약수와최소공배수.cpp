#include <string>
#include <vector>
#include <iostream>
using namespace std;
int gcd(int n, int m)
{
    while(m != 0)
    {
        int temp = n % m;
        n = m;
        m = temp;
    }
    
    return n;
}

int lcm(int n, int m)
{
    int g = gcd(n,m);
    return ( (n/g)  * (m / g) ) * g;
}

vector<int> solution(int n, int m) {
    vector<int> answer;
    answer.push_back(gcd(n,m));
    answer.push_back(lcm(n,m));
    cout << answer[0] <<" "<< answer[1]<< endl;
    return answer;
}

