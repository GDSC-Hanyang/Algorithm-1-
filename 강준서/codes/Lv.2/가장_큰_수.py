def solution(numbers): return ''.join(map(str,sorted(numbers,key=lambda x : str(x)*3)[::-1])) if sum(numbers) != 0 else '0'
