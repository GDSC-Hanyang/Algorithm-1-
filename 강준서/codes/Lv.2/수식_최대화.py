def solution(expression):
    # oper로 들어간 연산자만 연산하는 함수
    def calc(nums, ops, oper):
        dels = 0
        used = []
        for idx in range(len(ops)):
            if ops[idx] == oper:
                if oper == '-': nums[idx-dels]-=nums[idx-dels+1]
                elif oper == '*': nums[idx-dels]*=nums[idx-dels+1]
                else: nums[idx-dels]+=nums[idx-dels+1]
                del nums[idx-dels+1]
                used.append(idx)
                dels+=1

        dels = 0
        for i in used: 
            del ops[i-dels]
            dels+=1

        return nums, ops

    answer = []

    # expression을 숫자들(nums)과 연산자들(ops)로 파싱
    nums, ops = [], []
    start= 0
    for i in range(len(expression)):
        if expression[i] in '*-+':
            nums.append(expression[start:i])
            ops.append(expression[i])
            start = i+1
    nums.append(expression[start:])
    nums = list(map(int, nums))

    # 모든 연산자 우선순위 경우의 수에 대해 연산
    for comb in ['-*+','-+*','*-+','*+-','+-*','+*-']:
        temp_nums, temp_ops = nums[:], ops[:]  # deep copy 방식을 사용하기 위해 list 슬라이싱 사용
        for oper in comb: temp_nums, temp_ops = calc(temp_nums, temp_ops, oper)
        answer.append(temp_nums[0])

    answer = [abs(x) for x in answer]
    return max(answer)
