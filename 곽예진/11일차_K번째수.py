#K번째수
#https://programmers.co.kr/learn/courses/30/lessons/42748
#난이도 중

def solution(array, commands):
    answer = []
    for i in commands:
        cut=array[i[0]-1:i[1]]
        #숫자 정렬
        cut.sort()
        mid=cut[i[2]-1]
        answer.append(mid) 
    
    return answer
  
  
  
  
  #숫자 정렬 시
  ##숫자열은 그냥 list.sort()
  ##문자열의 경우 list.sort(key=int) ***
  
  #<1>
  a = [3, 2, 8, 4, 1, 10, 99, 5] 
  b = [3, 2, 8, 4, 1, 10, 99, 5] 
  c = [3, 2, 8, 4, 1, 10, 99, 5]
  
  # 기본값 (오름차순) 
  a.sort() 
  print("a.sort()") 
  print(a) 
  
  # 오름차순 
  b.sort(reverse=False) 
  print("\nb.sort(reverse=False)") 
  print(b) 
  
  # 내림차순 
  c.sort(reverse=True) 
  print("\nc.sort(reverse=True)") 
  print(c)

출처: https://blockdmask.tistory.com/564 [개발자 지망생]
