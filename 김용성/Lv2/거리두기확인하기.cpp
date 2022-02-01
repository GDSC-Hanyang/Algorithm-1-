#include <string>
#include <vector>

#include <iostream>

using namespace std;
vector<string> map;
bool inside(int row, int col)
{
    return ( row >= 0 && row < 5 ) && ( col >= 0 && col < 5 );
}
bool checkPlaces(int row, int col)
{
    if(inside(row, col-2) && map[row][col - 2] == 'P')//left
    {
        if(map[row][col-1] != 'X') return false;
    }
    
    if(inside(row - 2, col) && map[row - 2][ col ] == 'P')//top
    {
        if(map[row - 1][ col ] != 'X') return false;
    }
    
    if(inside(row , col + 2) && map[row ][col + 2] == 'P')//right
    {
        if(map[row ][col + 1] != 'X') return false;
    }
    
    if(inside(row + 2, col) && map[row + 2][col] == 'P')//bot
    {
        if(map[row + 1][col] != 'X') return false;
    }
    
    if(inside(row - 1, col - 1) && map[row - 1][col - 1] == 'P')//left top 대각
    {
        if(map[row - 1][col] != 'X' || map[row][col - 1] != 'X') return false;
    }
    
    if(inside(row - 1, col + 1) && map[row - 1][col + 1] == 'P')//right top 대각
    {
        if(map[row - 1][col] != 'X' || map[row][col + 1] != 'X') return false;
    }
    
    if(inside(row + 1, col + 1) && map[row + 1][col + 1] == 'P')//right bot 대각
    {
        if(map[row + 1][col] != 'X' || map[row][col + 1] != 'X') return false;
    }
    
    if(inside(row + 1, col - 1) && map[row + 1][col - 1] == 'P')//left bot 대각
    {
        if(map[row + 1][col] != 'X' || map[row][col - 1] != 'X') return false;
    }
    
    
    if(inside(row , col - 1) && map[row][col - 1] == 'P') return false;//left
    
    
    if(inside(row + 1, col) && map[row + 1][col ] == 'P') return false;//bot
    
    
    if(inside(row , col + 1) && map[row ][col + 1] == 'P') return false;//right
    
    if(inside(row - 1, col ) && map[row - 1][col ] == 'P') return false;//top
    
    
    return true;
    
    
}
vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    
    
    for(int i = 0; i < places.size(); i++)
    {
        map.clear();
        for(int j = 0; j < places[i].size(); j++)
        {
            map.push_back(places[i][j]);
        }

        
        
        bool flag = true;
        
        for(int j = 0; j < 5; j++)
        {
            for(int k = 0; k < 5; k++)
            {
                if(map[j][k] == 'P')
                {
                    if(checkPlaces(j, k) == false)
                    {
                        flag = false;
                        break;
                    }
                }
            }

            if(flag == false) break;
        }
        
        if(flag == true) answer.push_back(1);
        else answer.push_back(0);
        
    }
    return answer;
}
