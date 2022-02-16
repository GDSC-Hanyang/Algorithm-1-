def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        # 이미 사전순으로 정렬 되어있으므로 그 다음 값만 비교해보면 됨
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] : return False
    return True
  
