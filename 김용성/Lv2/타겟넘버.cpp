#include <string>
#include <vector>

using namespace std;

bool visit[30];
int answer = 0;

void dfs(int index, size_t size, int sum, vector<int> numbers, int target)
{
    if(index == size)
    {
        if(sum == target) answer++;
        return;
    }

    dfs(index + 1, size, sum + numbers[index], numbers, target);
    
    dfs(index + 1, size, sum - numbers[index], numbers, target);
}
//numbers         target  return
//[1, 1, 1, 1, 1]    3    5
int solution(vector<int> numbers, int target) {
    
    size_t size = numbers.size();
    dfs(0, size, 0, numbers, target);
    
    return answer;
}
