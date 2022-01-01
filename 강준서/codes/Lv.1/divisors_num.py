def divisors(num):
    n = 0
    for i in range(1,int(num**0.5)+1):
        if(num%i==0):
            if(i==num**0.5):
                n+=1
            else:
                n+=2
    return n

  
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if(divisors(i)%2==0):
            answer+=i
        else:
            answer-=i
    return answer
  
