def solution(nums):
    answer = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                is_prime = True
                num = nums[i] + nums[j] + nums[k]
                for l in range(2, num // 2):
                    if num % l == 0:
                        is_prime = False
                        break
                if is_prime == True:
                    print(f"{num}, sum of {nums[i]}, {nums[j]}, and {nums[k]} is a prime number")
                    answer += 1

    return answer
