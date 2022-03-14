def solution(numbers, target):
    def dfs(idx, sum):
        if idx == len(numbers)-1:
            return 1 if sum == target else 0
        return dfs(idx+1, sum + numbers[idx+1]) + dfs(idx+1, sum - numbers[idx+1])

    answer = dfs(0, numbers[0]) + dfs(0, -numbers[0])
    return answer