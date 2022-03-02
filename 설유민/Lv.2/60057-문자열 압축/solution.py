from math import log10
def solution(s):
    answer = len(s)
    
    for step in range(1, len(s) // 2 + 1):
        # 주어진 문자열을 쪼개서 각각 리스트의 원소로 함
        sub_s = [s[index:index + step] for index in range(0, len(s) - step + 1, step)]
        length = len(s)
        
        # 쪼개진 문자열별로 반복되는 횟수 저장
        repeat = [0 for i in range(0, len(sub_s))]
        repeat_index = 0
        
        for index in range(0, len(sub_s) - 1):
            if sub_s[index] == sub_s[index + 1]:
                repeat[repeat_index] += 1
                length -= step
            else: # 앞뒤 문자열이 일치하지 않는 경우
                repeat_index += 1
                
        length += sum([int(log10(num + 1) + 1) for num in repeat if num != 0])
        if length < answer:
            answer = length

    return answer