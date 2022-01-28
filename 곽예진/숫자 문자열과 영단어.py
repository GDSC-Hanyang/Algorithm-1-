#https://programmers.co.kr/learn/courses/30/lessons/81301

dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'} 

def solution(s):
  for key,value in dic.items():
    s=s.replace(key,value)
    answer=int(s)
  return answer




#딕셔너리는{key:value}형태로 이루어짐
#딕셔너리에서 key 값은 변하지 않는 형태이어야 한다.

#dic.items() 함수는 딕셔너리에 있는 모든 key와 value를 튜플로 묶어 돌려보낸다.

#replace( , )함수는 앞에 있는 string을 뒤에 있는 string으로 바꿔주는 역할은 한다.
#추가적으로 횟수를 지정하여 replace시키고 싶다면 replace(old,new,count)형태로 나타내주면 된다.

#답을 나타낼 때 숫자로 나타내야하므로 int() 까먹지 말기!
