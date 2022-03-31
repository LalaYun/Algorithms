from collections import Counter
import itertools

def selAlpha(List1): # orders에 있는 알파벳을 리스트로 나열하는 함수
    value = []
    for i in range(len(List1)) :
        tmp = list(List1[i])
        value.append(list(Counter(tmp).keys())) # orders[i]에 있는 알파벳 list
    return value
        

def solution(orders, course):
    answer = []
    ordersList = selAlpha(orders)
    enableMenu = [] # course 조합에 대한 문제
    for i in range(len(ordersList)) :
        for j in range(i+1, len(ordersList)) :
            cnt = 0
            tmp = ''
            for k in range(len(ordersList[i])) :
                cntK = 0
                if ordersList[i][k] in ordersList[j] :
                    tmp += ordersList[i][k]
                    cnt += 1
            if cnt in course :
                print('tmp :', tmp) 
                enableMenu.append(''.join(sorted(tmp)))

    tmpAns = list(set(enableMenu))
    tmpAns.sort()
    
    for num in course: 
        tmpAnsDict = {}
        for ans in tmpAns:
            if len(ans) == num: tmpAnsDict[ans] = 0
            else: continue
        
            for order in orders:
                flag = True
                for i in ans:
                    if i not in order:
                        flag = False
                        break
                if flag: tmpAnsDict[ans] += 1
        
        # answer.append(max(tmpAnsDict, key = tmpAnsDict.get))
        if len(tmpAnsDict.values()) == 0: continue
        
        Max = max(tmpAnsDict.values())
        for key, value in tmpAnsDict.items():
            print(key, value)
            if value == Max: answer.append(key)
        
    answer.sort()

    return answer