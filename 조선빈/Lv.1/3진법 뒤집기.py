def solution(n):
    reverse = ''

    while n > 0:
        n, mod = divmod(n, 3)
        reverse += str(mod)

    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    answer = int(reverse,3)
    return answer
