#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    
    int cnt = 0;
    for(int i = 0; i < lottos.size(); i++)
    {
        if(lottos[i] == 0)
        {
            cnt ++;
        }
    }
    printf("%d\n",cnt);
    
    for(int i = 0; i < win_nums.size(); i++)
    {
        printf("%d ",win_nums[i]);
    }
    printf("\n");
    
    sort(win_nums.begin(),win_nums.end());
    for(int i = 0; i < win_nums.size(); i++)
    {
        printf("%d ",win_nums[i]);
    }
    printf("\n");
    int rank = 0;
    
    for(int i = 0; i < win_nums.size(); i++)
    {
        if(binary_search(win_nums.begin(), win_nums.end(), lottos[i]))
        {
            rank++;
        }
    }
    printf("%d\n",rank);
    vector<int> answer;
    
    
    
    if(rank +cnt == 6) answer.push_back(1);
    else if(rank+cnt == 5) answer.push_back(2);
    else if(rank+cnt == 4) answer.push_back(3);
    else if(rank+cnt == 3) answer.push_back(4);
    else if(rank+cnt == 2) answer.push_back(5);
    else  answer.push_back(6);
    
    if(rank == 6) answer.push_back(1);
    else if(rank == 5) answer.push_back(2);
    else if(rank == 4) answer.push_back(3);
    else if(rank == 3) answer.push_back(4);
    else if(rank == 2) answer.push_back(5);
    else answer.push_back(6);

    return answer;
}
