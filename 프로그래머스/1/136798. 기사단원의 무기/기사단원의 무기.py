def solution(number, limit, power):
    answer = 0
    
    #약수 개수 저장 배열
    divisors = [0] * (number + 1)
    

    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
    
    for n in range(1, number + 1):
        if divisors[n] > limit:
            answer += power
        else:
            answer += divisors[n]
    
    return answer