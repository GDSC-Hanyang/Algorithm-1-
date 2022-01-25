#include <vector>
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
vi prime;
bool visit[3010];
void findPrime()
{
   
    for(int i = 2; i <3002; i++)
    {
        if( visit[i] ) continue;
        prime.push_back(i);
        for(int j = i; j <3002; j += i)
        {
            visit[j] = true;
        }
        
    }
    
}
int solution(vector<int> nums) {
    int answer = 0;

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    // cout << "Hello Cpp" << endl;
    findPrime();
    for(int i = 0; i < prime.size(); i++)
    {
        cout << prime[i] << " ";
        
    }
    vector<int> v;
    for(int i = 0; i < nums.size(); i++)
    {
        for(int j = i + 1; j < nums.size(); j++)
        {
            for(int k = j + 1; k < nums.size(); k++)
            {
                v.push_back(nums[i] + nums[j] + nums[k]);
            }
        }
    }
    
    for(int i = 0; i <v.size(); i++)
    {
        if(binary_search(prime.begin(), prime.end(), v[i]))
        {
            answer++;
        }
        
    }
    
    
    return answer;
}
