from itertools import permutations

def oper(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    a=[]
    tmp=""
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            a.append(tmp)
            a.append(i)
            tmp=""
    a.append(tmp)
    
    for j in op:
        stack=[]
        while len(a)!=0:
            tmp=a.pop(0)
            if tmp==j:
                stack.append(oper(stack.pop(), a.pop(0), j))
            else:
                stack.append(tmp)
        a=stack
            
    return abs(int(a[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)
