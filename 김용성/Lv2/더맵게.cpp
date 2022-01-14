#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <iostream>
#include <queue>

using namespace std;
typedef vector<int> vi;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for(int i = 0; i < scoville.size();i++)
    {
        pq.push(scoville[i]);
    }
    cout << pq.top();
    
    if(pq.top() < K)
    {
        while(pq.top() < K)
        {
            if(pq.size() < 2)
            {
                answer = -1;
                break;
            }
            
            int num1 = pq.top();
            pq.pop();
            int num2 = pq.top();
            pq.pop();
            answer++;
            pq.push(num1 + num2 * 2);
        }
    }
    
    return answer;
}
