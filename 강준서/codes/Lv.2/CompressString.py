def solution(s):
    answer = 1000
    n = len(s) # 문자열 길이

    # 1부터 압축 진행
    for i in range(1,n+1):
        temp = n
        depth = 1

        for j in range(0,n,i):
            if(n>=j+2*i and s[j:j+i]==s[j+i:j+2*i]):
                temp -= i # 압축
                # 추가되는 숫자 고려
                if(depth==1): temp += 1 
                elif(depth==9): temp += 1 
                elif(depth==99): temp += 1 
                elif(depth==999): temp += 1 
                depth += 1
            else: depth = 1 # 연속이 끊기면 초기화

        answer = min(temp,answer) # 더 작은 값을 취함

    return answer
  
