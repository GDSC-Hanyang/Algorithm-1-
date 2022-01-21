#include <string>
#include <vector>
#define INF 10000000
using namespace std;
int map[110][110];
vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    int cnt = 1;
    for(int i = 1; i <=rows; i++)
    {
        for(int j = 1; j <=columns; j++)
        {
            map[i][j] = cnt++;
        }
    }
    
    
    for(int i = 0; i < queries.size(); i++)
    {
        int x1 = queries[i][0];
        int y1 = queries[i][1];
        int x2 = queries[i][2];
        int y2 = queries[i][3];
        
        int minimize = INF;
        
        int a = map[x1 + 1][y1];
        int b = map[x1][y1];
        
        if(a < minimize) minimize = a;
        for(int j = y1; j < y2; j++)//위
        {
            
            map[x1][j] = a;
            a = b;
            b = map[x1][j + 1];
            if(a < minimize) minimize = a;
        }
        
        
        for(int j = x1; j < x2; j++)//오른쪽
        {
            map[j][y2] = a;
            a = b;
            b = map[j + 1][y2];
            if(a < minimize) minimize = a;

            
        }
        
        
        
        for(int j = y2 ; j > y1; j--)//아래
        {
            map[x2][j] = a;
            a = b;
            b = map[x2][j - 1];
            if(a < minimize) minimize = a;
        }

            
        for(int j = x2; j > x1; j--)//왼쪽
        {
            
            map[j][y1] = a;
            a = b;
            b = map[j - 1][y1];
            if(a < minimize) minimize = a;
        }
            
            
//        for(int i = 1; i <=rows; i++)
//        {
//            for(int j = 1; j <=columns; j++)
//            {
//                printf("%d ",map[i][j]);
//            }
//            printf("\n");
//        }
//            printf("\n");
            
        answer.push_back(minimize);
        
    }
    return answer;
}

