#include <string>
#include <vector>
#define INF 100000000
using namespace std;

vector<int> solution(vector<int> arr) {
    
    int idx;
    int mini = INF;
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] < mini)
        {
            idx = i;
            mini = arr[i];
        }
    }
    arr.erase(arr.begin()+idx);
    vector<int> answer(arr.begin(), arr.end());
    if(answer.empty()) answer.push_back(-1);
    
    
    
    
    return answer;
}

