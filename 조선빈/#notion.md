count
=====

list에서 어떠한 원소의 개수를 세는 명령어

<pre>
<code>
listA.count('a')
</pre>
</code>

lower
=====

str에서 대문자를 소문자로 바꾸어주는 명령어

<pre>
<code>
strA = strA.lower()
</pre>
</code>

replace
=======

str에서 값을 치환해주는 명령어

<pre>
<code>
strA = strA.replace('치환당할 값','치환할 값')
</pre>
</code>

join
====

list에서 str로 변환하는 방법

<pre>
<code>
strA="".join(listA)

strA=".".join(listA) 

    —>listA의 아이템들을 합치면서 사이에 . 추가

strA="/".join(['a','b','c'])

      —>'a/b/c'
</pre>
</code>

isalpha
=======
str에서 알파벳인지 확인하는 방법

<pre>
<code>
strA.isalpha()
</pre>
</code>

isdigit
=======

str에서 숫자인지 확인하는 방법

<pre>
<code>
strA.isdigit
</pre>
</code>

isalnum
=======

str에서 숫자 또는 알파벳인지 확인하는 방법

<pre>
<code>
strA.isalnum
</pre>
</code>

lambda
======

인자, 표현식을 한줄에 나타낼 수 있음

<pre>
<code>
(lambda x,y: x+y)(10,20)
</pre>
</code>

filter
======

조건에 맞는 것만 골라 새로운 리스트 생성

<pre>
<code>
filter(함수, 리스트)

filter(lambda x: x<5, range(10))

     —>[0,1,2,3,4] 
</code>
</pre>

split
=====

str 나누어서 새로운 리스트 생성

<pre>
<code>
strA.split(',') 

     —>,를 기준으로 나누어서 새로운 리스트 생성

'an,cn,bc'.split(',') 

     —>['an','cn','bc']

"".join(filter(lambda x: x≠'', strA.split('.'))

     —>.을 기준으로 모두 나눠져 새로운 리스트가 생성된 후 다시 

     문자열로 합쳐짐
</pre>
</code>

sum
===

숫자로만 이루어져 있는 리스트나 튜플 ( 인덱스 순환 접근 가능 자료형)

<pre>
<code>
sum(iterable) 

    —> 모든 요소의 합

sum(iterable, start = 0) 

    —> iterable의 합 + start 값
</pre>
</code>

pop
===

리스트의 가장 마지막 요소를 돌려주고 리스트 내에서는 그 요소를 삭제
<pre>
<code>
a = [1,2,3]
a.pop()
    —> 3
    —> a = [1,2]
a.pop(1)
    —> 2
    —> a = [1]
</pre>
</code>

dictionary
==========

대응하는 자료형 저장
<pre>
<code>
dic = {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic[KeyN] = 'ValueN'
    —> dic = {Key1:Value1, Key2:Value2, Key3:Value3, ... , KeyN:ValueN}
    -> 새 항목 추가 또는 기존 항목 
</pre>
</code>

divmod
======

몫과 나머지
작은 수일 때는 a//b와 a%b가 더 빠름
<pre>
<code>
몫, 나머지 = divmod(a,b)
</code>
</pre>

set
===

리스트 순서대로 + 중복되는 아이템 제거
<pre>
<code>
a = [5,3,4,1,2,2]
b = set(a)
    —> [1,2,3,4,5]
</code>
</pre>

sort
====

리스트 순서대로
// 기본값 : 오름차순
// reverse = True : 내림차순
// key = len : 원소 길이순
// key = 옵션
<pre>
<code>
a = [5,3,4,1,2,2]
b = a.sort()
    —> [1,2,2,3,4,5]
c = a.sort(reverse = True)
    —> [5,4,3,2,2,1]
d = sorted(a)
    —> [1,2,2,3,4,5]
</code>
</pre>

int(string, base)
=================

base진법을 10진법으로 변환
<pre>
<code>
int(11,2)
    —> 1011
</code>
</pre>

heapq
=====

이진트리 기반의 min heap (최소 힙) 자료구조를 제공하는 내장 모듈
원소들이 항상 정렬된 상태로 추가되고 삭제됨
최솟값은 항상 index 0에 위치

<pre>
<code>
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

     1  ---> root
   /   \
  3     5
 / \   /
4   8 7
</code>
</pre>


<pre>
<code>
import heapq

heap = []
heapq.heappush(heap, 4) #이진트리에 원소 추가
heapq.heappop(heap) #힙에서 최솟값 원소 삭제
heapq.heapify(heap) #리스트를 힙으로 변환

</code>
</pre>


combinations
=============

서로 다른 n개 중에서 r개를 취하여 만든 조합

<pre>
<code>
import itertools

nCr = itertools.combinations(list, r)
list(nCr) —> [조합들]

</code>
</pre>

permutation
===========

몇 개를 골라 순서를 고려해 나열한 경우의 수를 구하는 순열

<pre>
<code>
import itertools

nPr = itertools.permutations(list, 2)
list(nPr) —> [순열들]

</code>
</pre>

Coounter from collections
================

중복이 많이 된 것부터 중복 횟수를 세주는 클래스

<pre>
<code>
from collections import Counter

Counter('hello world') 
    —>Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
</code>
</pre>
