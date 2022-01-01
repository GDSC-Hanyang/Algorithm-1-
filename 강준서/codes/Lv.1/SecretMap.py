def bitmask(n,x):
    bits=[]
    for i in range(n):
        if(x >= 2**(n-i-1)):
            bits.append(True)
            x -= 2**(n-i-1)
        else:
            bits.append(False)
    return bits

def solution(n, arr1, arr2):
    bitmap = []
    answer = []
    for i in arr1:
        bitmap.append(bitmask(n,i))

    for idx, i in enumerate(arr2):
        for jdx, bit in enumerate(bitmask(n,i)):
            if (bit): bitmap[idx][jdx] = True

    for bits in bitmap:
        string = ''
        for bit in bits:
            if(bit): string += '#'
            else: string += ' '
        answer.append(string)

    return answer
  
