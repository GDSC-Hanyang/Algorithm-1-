def solution(numbers):
	tmp = []
	for i in range(len(numbers)-1):
		for j in range(i+1, len(numbers)):
			tmp.append(numbers[i]+numbers[j])
	answer = sorted(list(set(tmp)).sort())
	return answer