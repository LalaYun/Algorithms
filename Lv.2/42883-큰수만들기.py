# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3#

def solution(number, k):
    answer = []
    
    for i in range(0, len(number)):
        while answer and answer[-1] < number[i] and k > 0:
            answer.pop()
            k -= 1
        answer.append(number[i])
    
    answer = "".join(answer)
    return answer[0:len(number) - k]