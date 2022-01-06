def solution(n):
    primes = [2]

    for i in range(3,n+1,2):
        flag = True
        for j in primes:
            if i%j==0:
                flag = False
                break
            elif j>i**(0.5): break
        if (flag): primes.append(i)

    return len(primes)
