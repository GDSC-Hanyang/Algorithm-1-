import math
def solution(w,h): return w*h - w - h + math.gcd(w,h)

# 잘리는 부분이 gcd(최대공약수)만큼 반복되는 구조
# 각 패턴마다 (w/gcd + h/gcd -1)만큼 못쓰는 사각형이 생김
# 이를 정리하면 위 코드 처럼 한줄로 간단하게 나오게 된다. (유사 한줄코딩)
