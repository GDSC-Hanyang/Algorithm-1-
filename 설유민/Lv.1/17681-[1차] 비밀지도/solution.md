# 비밀지도
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><h2>비밀지도</h2>

<p>네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.</p>

<ol>
<li>지도는 한 변의 길이가 <code>n</code>인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.</li>
<li>전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.</li>
<li>"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.</li>
<li>암호화된 배열은 지도의 각 가로줄에서 벽 부분을 <code>1</code>, 공백 부분을 <code>0</code>으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.</li>
</ol>

<p><img src="http://t1.kakaocdn.net/welcome2018/secret8.png" title="Secret Map" alt="secret map"></p>

<p>네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.</p>

<h3>입력 형식</h3>

<p>입력으로 지도의 한 변 크기 <code>n</code> 과 2개의 정수 배열 <code>arr1</code>, <code>arr2</code>가 들어온다.</p>

<ul>
<li>1 ≦ <code>n</code> ≦ 16</li>
<li><code>arr1</code>, <code>arr2</code>는 길이 <code>n</code>인 정수 배열로 주어진다.</li>
<li>정수 배열의 각 원소 <code>x</code>를 이진수로 변환했을 때의 길이는 <code>n</code> 이하이다. 즉, 0 ≦ <code>x</code> ≦ 2<sup>n</sup> - 1을 만족한다.</li>
</ul>

<h3>출력 형식</h3>

<p>원래의 비밀지도를 해독하여 <code>'#'</code>, <code>공백</code>으로 구성된 문자열 배열로 출력하라.</p>

<h3>입출력 예제</h3>
<table class="table">
        <thead><tr>
<th>매개변수</th>
<th>값</th>
</tr>
</thead>
        <tbody><tr>
<td>n</td>
<td>5</td>
</tr>
<tr>
<td>arr1</td>
<td>[9, 20, 28, 18, 11]</td>
</tr>
<tr>
<td>arr2</td>
<td>[30, 1, 21, 17, 28]</td>
</tr>
<tr>
<td>출력</td>
<td><code>["#####","# # #", "### #", "#  ##", "#####"]</code></td>
</tr>
</tbody>
      </table><table class="table">
        <thead><tr>
<th>매개변수</th>
<th>값</th>
</tr>
</thead>
        <tbody><tr>
<td>n</td>
<td>6</td>
</tr>
<tr>
<td>arr1</td>
<td>[46, 33, 33 ,22, 31, 50]</td>
</tr>
<tr>
<td>arr2</td>
<td>[27 ,56, 19, 14, 14, 10]</td>
</tr>
<tr>
<td>출력</td>
<td><code>["######", "###  #", "##  ##", " #### ", " #####", "### # "]</code></td>
</tr>
</tbody>
      </table>
<p><a href="http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/" target="_blank" rel="noopener">해설 보러가기</a></p>
</div>
    </div>

## 답안
> 4. 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

처음에는 이 조건에 집중하여 입력으로 주어진 배열의 정수들을 이진수로 변환해야 한다고 생각했다.    
이진수로 변환하기 위해 수를 2로 계속 나누어서 나오는 나머지들을 이용하고자 했다.
```python
# dec: 주어진 십진수, answer: 이진수 변환 결과 문자열
while dec >= 1:
    answer += str(dec % 2)
    dec //= 2

# 예시
dec = 10
answer = ''
while dec >= 1:
    answer = str(dec % 2) + answer
    dec //= 2
print(answer)
>>> '1010'
```
찾아보면서 위와 같은 과정을 거치지 않더라도 파이썬에서는 'bin'을 활용하여 십진수를 쉽게 이진수로 표현할 수 있다는 것을 알게 되었다.
```python
bin(10)
>>> '0b1010'
```
그런데 생각해보니까 굳이 비교할 두 수를 모두 이진수로 직접 변환할 필요가 없었다.  
> 2. 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.  

즉, 암호화된 두 지도에서 같은 위치에 #이 하나라도 있으면 해독된 지도(결과)에는 해당 칸에 #이 있도록 해야 한다.  
'#이 하나라도 있으면'을 일일이 이진수 변환 없이 두 수의 'OR' 연산을 사용해 구현할 수 있다는 생각이 떠올랐다.
```python
9 | 30
>>> 31
bin(31)
>>> '0b11111'
```
심지어 이진수로 바꾼 다음에 '|' 연산을 사용하여 비교하는 것이 애초에 불가능했다.
```python
'0b1001' | '0b11110'
>>> TypeError: unsupported operand type(s) for |: 'str' and 'str'
```
이진수를 표현하기 위해 문자열을 사용했기 때문에 문자열을 지원하지 않는 '|' 연산을 사용할 수 없었다.  

그래서 이진수로 변환하는 과정을 처음부터 거치지 말고,  
1. 두 정수에 대해 '|' 연산을 먼저 수행한 후 이진수로 표현하고,
2. 이진수 문자열의 '1'을 '#'으로, '0'을 공백으로 바꾸는 방향으로 코드를 작성했다.
```python
answer = []
for i in range(0, n):
    answer.append(bin(arr1[i] | arr2[i]).replace('0b', ''))
```   
이 때 문자열이 n개보다 적은 문자로 구성되는 경우를 방지하기 위해 앞에 0 padding이 필요했다.  
이중 for문을 사용해서 앞에 0을 붙이는 방법을 생각했는데, 더 간단하게 할 수 있는 방법이 있을 것 같아 고민하다가 f-string을 활용할 수 있겠다는 생각을 했다.  

f-string을 활용하여 아래 답안을 최종적으로 제출했다.
```python
def solution(n, arr1, arr2):
    return [f'{(arr1[i] | arr2[i]):0{n}b}'.replace('1', '#').replace('0', ' ') for i in range(0, n)]
```
모든 이진수 결과가 n개의 문자로 이루어진 문자열이 될 수 있도록 앞에 0을 붙여주고, 결과 문자열에서 '1'은 '#'으로, '0'은 ' '로 대체했다.

<div class="console-message">정확성  테스트</div>
<table class="console-test-group" data-category="correctness"><tbody><tr data-testcase-id="30892"><td valign="top" class="td-label">테스트 1 <span>〉</span></td><td class="result passed">통과 (0.02ms, 10.1MB)</td></tr><tr data-testcase-id="30893"><td valign="top" class="td-label">테스트 2 <span>〉</span></td><td class="result passed">통과 (0.02ms, 10.2MB)</td></tr><tr data-testcase-id="30894"><td valign="top" class="td-label">테스트 3 <span>〉</span></td><td class="result passed">통과 (0.01ms, 10.2MB)</td></tr><tr data-testcase-id="30895"><td valign="top" class="td-label">테스트 4 <span>〉</span></td><td class="result passed">통과 (0.01ms, 10.1MB)</td></tr><tr data-testcase-id="30896"><td valign="top" class="td-label">테스트 5 <span>〉</span></td><td class="result passed">통과 (0.01ms, 10.3MB)</td></tr><tr data-testcase-id="30897"><td valign="top" class="td-label">테스트 6 <span>〉</span></td><td class="result passed">통과 (0.02ms, 10.2MB)</td></tr><tr data-testcase-id="30898"><td valign="top" class="td-label">테스트 7 <span>〉</span></td><td class="result passed">통과 (0.01ms, 10.2MB)</td></tr><tr data-testcase-id="30899"><td valign="top" class="td-label">테스트 8 <span>〉</span></td><td class="result passed">통과 (0.01ms, 10.2MB)</td></tr></tbody></table>
<div class="console-heading">채점 결과</div>
<div class="console-message">정확성: 100.0</div>
<div class="console-message">합계: 100.0 / 100.0</div>