# 알고리즘 스터디


발표1 : 시저암호(Lv.1)
------

<문제 설명>

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 

예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 

문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.


<제한 조건>

공백은 아무리 밀어도 공백입니다.

s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.

s의 길이는 8000이하입니다.

n은 1 이상, 25이하인 자연수입니다.


<나의 풀이 방법>

1. n은 1 이상, 25이하의 자연수이므로 대문자와 소문자의 순서대로 각각 두번 반복된 문자열을 만든다.

<pre>
<code>
low = 'abcdefghijklmnopqrstuvwxyz'*2
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
</code>
</pre>


2. s에 속한 문자가 대문자(혹은 소문자)에 속하면 그 대문자(혹은 소문자)의 인덱스에서 n만큼 더해진 위치의 대문자(혹은 소문자)를 가져온다.
 
<pre>
<code>
if i in up:
        answer += up[up.index(i)+n]
if i in low:
        answer += low[low.index(i)+n]
</code>
</pre>

3. 대문자나 소문자가 아닌 공백일 경우 공백을 그대로 더해준다.

<pre>
<code>
if i == ' ':
  answer += ' '
</code>
</pre>
    
<전체 풀이>

<pre>
<code>
def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'*2
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*2
    answer = ''
    for i in s:
        if i in up:
            answer += up[up.index(i)+n]
        elif i in low:
            answer += low[low.index(i)+n]
        else:
            answer += ' '
    return answer
</code>
</pre>

<다른 풀이>

아스키 코드를 이용한 방식


ord(문자) : 문자에 해당하는 ASCII 정수값 반환 

chr(정수) : 정수에 해당하는 ASCII 문자 반환


![image](https://user-images.githubusercontent.com/89207256/154252687-c47a9e36-40fe-47c8-a639-914d940e0cad.png)

(출처: https://wooaoe.tistory.com/72 [개발개발 울었다])

<pre>
<code>
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
</code>
</pre>

발표2 : 거리두기 확인하기
--------------------


<문제 설명>

개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼

아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.

거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.

단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

1. 대기실은 5개이며, 각 대기실은 5X5 크기입니다.

2. 거리두기를 위하여 응시자들끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.

3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우애는 허용합니다.

![image](https://user-images.githubusercontent.com/89207256/158151235-83ed8af1-c7e7-48e4-a06e-fd3ebf6fa913.png)

5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리두기를 잘 기키고 있는지 알고 싶어졌습니다. 

자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 

각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.


<제한 조건>

places의 행 길이(대기실 개수) = 5

places의 각 행은 하나의 대기실 구조를 나타냅니다.

places의 열 길이(대기실 세로 길이) = 5

places의 원소는 P,O,X로 이루어진 문자열입니다.

places 원소의 길이(대기실 가로 길이) = 5

P는 응시자가 앉아있는 자리를 의미합니다.

O는 빈 테이블을 의미합니다.

X는 파티션을 의미합니다.

입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.

return 값 형식

1차원 정수 배열에 5개의 원소를 담아서 return 합니다.

places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.

각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.


<나의 풀이 방법>

1. P를 기준으로 'X'가 아닌 지점을 방문하는 문제 = BFS 문제

<pre>
<code>
from collections import deque
</code>
</pre>

2. P를 출발점으로 하여 시작점이 되는 P의 좌표를 모두 Ps 리스트에 저장

<pre>
<code>
    Ps = []

    for i in range(5): # P의 좌표
        for j in range(5):
            if p[i][j] == 'P':
                Ps.append([i, j])
</code>
</pre>

3. Ps 리스트 내부의 P를 하나씩 BFS 하면서 거리두기 여부를 모두 확인 >> visit 방문 리스트와 distance 경로 길이 리스트를 모두 초기화

<pre>
<code>
 for s in Ps:
        que = deque([s])  # 큐에 초기 P의 좌표
        visit = [[0]*5 for i in range(5)]   # 방문 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visit[s[0]][s[1]] = 1
 </code>
 </pre>
 

4. P는 BFS 탐색을 시작하면 다른 P를 만나거나 모든 탐색 가능한 지점에 도달할 때까지 상하좌우로 이동을 반복

- 'X'를 만나면 벽에 가로막힌 것이므로 해당 방향으로 탐색 불가
- 'O'를 만나면 열려있는 공간이므로 P가 탐색 가능
- 또다른 'P'를 만나면 경로 거리를 판단하여 맨해튼 거리 2보다 작으면 0을 return하고 2보다 크면 1을 return
  (모든 P의 위치에서 BFS를 해서 성공해야 1을 return)
  
<pre>
<code>
while que:
            y, x = que.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        que.append([ny, nx])
                        visit[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
</code>
</pre>

<전체 풀이>

<pre>
<code>
from collections import deque

def bfs(p):
    Ps = []

    for i in range(5): # P의 좌표
        for j in range(5):
            if p[i][j] == 'P':
                Ps.append([i, j])

    for s in Ps:
        que = deque([s])  # 큐에 초기 P의 좌표
        visit = [[0]*5 for i in range(5)]   # 방문 리스트
        distance = [[0]*5 for i in range(5)]  # 경로 길이 리스트
        visit[s[0]][s[1]] = 1

        while que:
            y, x = que.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<5 and 0<=ny<5 and visit[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        que.append([ny, nx])
                        visit[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer
    
</code>
</pre>

<BFS와 DFS>

![image](https://user-images.githubusercontent.com/89207256/158154698-be61381f-b334-4774-941e-96c929d6edca.png)

Breath First Search (너비 우선 탐색) : A - B - C - H - D - I - J - M - E - G - K - F - L
Depth First Search (깊이 우선 탐색) : A - B - C - D - E - F - G - H - I - J - K - L - M

1. 한 노드를 중심으로 연결되어 있는 노드를 모두 표현하는 방식으로 그래프 표현 

<pre>
<code>
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
</code>
</pre>

2. BFS 구현
<pre>
<code>

def bfs(graph, start_node):
      visit = list()
      queue = list()
 
      queue.append(start_node)
 
      while queue:
          node = queue.pop(0)
          if node not in visit:
              visit.append(node)
              queue.extend(graph[node])
 
      return visit
      
</code>
</pre>

3. DFS 구현
<pre>
<code>
def dfs(graph, start_node):
     visit = list()
     stack = list()

     stack.append(start_node)

     while stack:
         node = stack.pop()
         if node not in visit:
             visit.append(node)
             stack.extend(graph[node])

     return visit
     
</code>
</pre>

4. BFS와 DFS의 차이점
pop() : 맨 마지막에 넣었던 아이템을 가져옴  == stack
pop(0) : 맨 앞에 있는 아이템을 가져옴 == queue

(출처 : https://itholic.github.io/python-bfs-dfs/)
