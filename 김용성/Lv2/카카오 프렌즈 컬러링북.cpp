#include <vector>
#include <iostream>
#include <queue>
#include <utility>
#include <stdio.h>
#include <algorithm>

using namespace std;
bool check[110][110];
int copyArr[110][110];
int direction[4][2];
int number_of_area ;
int max_size_of_one_area;

bool inside(int row, int col, int m, int n)
{
    return (row >=0 && row < m) && (col >= 0 && col < n);
    
}
void bfs(int m, int n, int pictureNum, int currentRow, int currentCol)
{
    number_of_area ++;
    queue<pair<int, int>> q;
    int cnt = 1;
    q.push(make_pair(currentRow, currentCol));
    check[currentRow][currentCol] = true;
    
    while(!q.empty())
    {
        int row = q.front().first;
        int column = q.front().second;
        q.pop();
        
        for(int i = 0; i< 4; i++)
        {
            int nextRow = row + direction[i][0];
            int nextCol = column + direction[i][1];
            
            if(inside(nextRow, nextCol ,m, n) && pictureNum == copyArr[nextRow][nextCol] && check[nextRow][nextCol] == false)
            {
                q.push(make_pair(nextRow, nextCol));
                check[nextRow][nextCol] = true;
                cnt++;
            }
        }
    }
    cout<< "cnt : " << cnt;
    if(cnt > max_size_of_one_area) max_size_of_one_area = cnt;
    
}
void copyMap(int m, int n, vector<vector<int>> picture)
{
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j <n; j++)
        {
            copyArr[i][j] = picture[i][j];
        }
    }
    
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    for(int i = 0; i < m+1; i++)
    {
        for(int j = 0; j < n+1; j++)
        {
            check[i][j] = false;
        }
    }
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j <n; j++)
        {
            copyArr[i][j] = picture[i][j];
        }
    }
    direction[0][0] = 1;
    direction[0][1] = 0;
    
    direction[1][0] = 0;
    direction[1][1] = 1;
    
    direction[2][0] = -1;
    direction[2][1] = 0;
    
    direction[3][0] = 0;
    direction[3][1] = -1;
    
    number_of_area = 0;
    max_size_of_one_area = 0;
//    copyMap(m, n, picture);
    
    for(int i = 0; i < m ; i++)
    {
        for(int j = 0; j < n; j++)
        {
//            cout << picture[i][j];
            if( picture[i][j] != 0 && check[i][j] == false)
            {
                bfs(m, n, picture[i][j], i, j);
            }
        }
//        cout << endl;
    }
    
    vector<int> answer(2);
    cout << answer[0] << " "<<answer[1] <<endl;
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
