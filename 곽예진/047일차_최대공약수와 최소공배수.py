#최대공약수와 최소공배수
#https://programmers.co.kr/learn/courses/30/lessons/12940

#소인수분해해서 최대공약수는 겹치는 얘로 최소공배수는 두개를 더해서 겹치는 것 빼줘서 구하기=> so so
#함수가 존재하리라...?
#'두수의 곱은 최대공약수*최소공배수'이다
##결론: 소인수분해해서 겹치는 얘로 최소공배수 구하고 법칙이용해서 최소공배수 구하기 => nice

#소인수분해...? 약수 구하기랑 비슷한 느낌!

def solution(n, m):
    nlist=[]
    mlist=[]
    #n,m 약수구하기
    for i in range(1,int(n**(1/2))+1):
        if n%i==0:
            nlist.append(i)
            nlist.append(int(n/i))
    for k in range(1,int(m**(1/2))+1):
        if m%k==0:
            mlist.append(k)
            mlist.append(int(m/k))
    #큰수부터 정렬
    nlist.sort(reverse=True)
    mlist.sort(reverse=True)
    #최대공약수 구하기
    c_max=1
    for l in nlist:
        if l in mlist:
            c_max=l
            break
    #최소공배수 구하기
    c_min= n * m / c_max
    return [c_max,c_min]
