from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        count_dict={}
        for order in orders:
            if(len(order)<i): continue
            order = ''.join(sorted(order)) # 각각의 order를 사전순으로 정렬
            for case in list(combinations(order,i)):
                letter = ''.join(case)
                if letter not in count_dict: count_dict[letter] = 1
                else: count_dict[letter]+=1

        answer+=[k for k,v in count_dict.items() if (max(count_dict.values()) == v and v > 1)]

    return sorted(answer)
  
