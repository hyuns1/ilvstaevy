def solution(cards1, cards2, goal):
    answer = ''
    for i in goal:
#리스트가 비어있을 때 인덱스 접근 시 에러, cards1, cards2가 비어있으면 뒤 조건을 확인 X
        if cards1 and cards1[0] == i:
            cards1.pop(0)
        elif cards2 and cards2[0] == i:
            cards2.pop(0)
        else:
            return "No"
    
    answer = "Yes"
    return answer