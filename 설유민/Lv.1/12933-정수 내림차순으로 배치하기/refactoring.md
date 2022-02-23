# 정수 내림차순으로 배치하기
<div class="guide-section-description">
      <h6 class="guide-section-title">문제 설명</h6>
      <div class="markdown solarized-dark"><p>함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.</p>

<h5>제한 조건</h5>

<ul>
<li><code>n</code>은 1이상 8000000000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th style="text-align: center">return</th>
</tr>
</thead>
        <tbody><tr>
<td>118372</td>
<td style="text-align: center">873211</td>
</tr>
</tbody>
      </table></div>
    </div>

## 런타임 에러가 발생한다
런타임 에러가 발생했던 코드는 아래와 같다.
```python
def solution(n):
    n_list = list(map(int,str(n)))
    n_list.sort(reverse = True)
    answer = ''.join(map(str,n_list))
    return int(answer)
```

내가 제출했던 답안은 아래와 같다.  
```python
def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))
```
제출 당시에는 정확도 100으로 통과했는데, 다른 계정으로 새로 채점해본 결과 내 코드도 2, 3, 11번 테스트 케이스에서 런타임 에러가 발생했다.  

오답으로 인한 실패가 아닌 런타임 에러가 발생한 것을 보고, 어떤 종류의 에러를 발생시키는지 알아보고자 했다.  
```python
def solution(n):
    try:
        n_list = list(map(int,str(n)))
        n_list.sort(reverse = True)
        answer = ''.join(map(str,n_list))
        return int(answer)
    except ValueError:
        print("Something went wrong.")
```
except가 잡아내는 에러의 종류를 ValueError로 지정해주자, 실패 원인이 런타임 에러에서 잘못된 결과값이 도출되었을 때 나오는 문구로 변경되었다.  
채점 결과를 통해 코드의 어디선가 ValueError가 발생한다는 사실을 찾아낼 수 있었다.

TypeError가 아닌 ValueError가 발생하는 것을 보고, 아래 두 줄의 코드를 의심해볼 수 있었다.
```python
def solution(n):
    try:
        n_list = list(map(int,str(n))) # 에러 발생 의심
        n_list.sort(reverse = True)
        answer = ''.join(map(str,n_list)) # 에러 발생 의심
        return int(answer)
    except ValueError:
        print("Something went wrong.")
```
[str()의 경우 object로 list가 들어가는 데에 전혀 문제가 없어보였다.](https://www.w3schools.com/python/ref_func_str.asp)  
int()의 경우 value로 문자열을 받을 수 있기 때문에 TypeError는 발생하지 않았지만, int로 바꿀 수 없는 형태의 문자열이 입력되어 ValueError가 발생하는 것이 아닐지 의심할 수 있었다.

주어진 조건에 따르면 그래서는 안 되지만 입력이 실수인 경우, 문자열 변환 과정에서 '.' 등 특수문자가 그대로 포함될 수 있다.
입력값을 문자열로 변환했을 때, 실수의 소수점 등 숫자가 아닌 문자가 포함될 수 있다는 가정을 하고 코드를 아래와 같이 수정했다.  
```python
from re import sub
def solution(n):
    return int(''.join(sorted(list(sub(r'[^0-9]', '', str(n))), reverse=True)))
```
그러나 해결할 수 없었다.  
다시 생각해보니 소수점이 문제가 되는 거라면 소수점만 없앨 게 아니라 소수점 아래의 수를 버려야한다는 사실을 깨달았다.  
```python
from re import sub
def solution(n):
    return int(''.join(sorted(list(str(int(n))), reverse=True)))
```
입력값 n을 int로 바꿔주는 작업을 한 후, 정확도 100을 달성할 수 있었다.  

위와 같은 입력이 들어오는지는 테스트 케이스를 공개하지 않기 때문에 알 수 없었지만, 완벽한 정수가 아닌 입력이 들어오는 경우가 존재하는지 확인하기 위해 아래와 같이 코드를 수정했다.
```python
from re import sub
def solution(n):
    if sub(r'[^0-9]', '', str(n)) != str(n):
        raise ValueError
    else:
        return int(''.join(sorted(list(sub(r'[^0-9]', '', str(n))), reverse=True)))
```
그 결과, 계속 문제가 되었던 2, 3, 11번 테스트 케이스에서 다시 런타임 에러가 발생하였다.  
정말 정수가 아닌 입력을 주었나보다...  
질문받았던 코드도 아래와 같이 수정하니 잘 작동되었다!  
```python
def solution(n):
    n = int(n) # 추가한 부분
    n_list = list(map(int,str(n)))
    n_list.sort(reverse = True)
    answer = ''.join(map(str,n_list))
    return int(answer)
```
> 왜 정수 n이라고 조건을 주고 정수가 아니라고 의심되는 테스트 케이스를 줬을까?  

분명 테스트 케이스를 추가하는 부분에서는 입력값 n의 형식이 'long'으로 기재되어 있었고, 문제 조건에도 정수 n이라고 표기되어 있었으나, int형이 아니더라도 우리가 생각했을 때 정수인 표현을 사용할 수 있다는 사실을 깨달았다.
```python
print(12345e+2)
>>> 1234500.0
print(type(12345e+2))
>>> <class 'float'>
```


