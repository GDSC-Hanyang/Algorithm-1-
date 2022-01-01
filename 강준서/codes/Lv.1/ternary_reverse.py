def solution(n):
    ans = 0
    three = ''
    ex = 1

    # Check n's max exponential at 3.
    while(n >= 3**ex): ex+=1
    ex -= 1

    # Make it ternary number
    while(n>0):
        next = n//(3**ex)
        three += str(next)
        n -= next*(3**ex)
        ex -= 1
    
    # Calculate it reversely
    for i, num in enumerate(three):
        ans+=int(num)*(3**i)

    return ans
