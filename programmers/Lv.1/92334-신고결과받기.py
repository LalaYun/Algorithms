def solution(id_list, report, k):
    
    # id와 report 횟수를 연결할 딕셔너리
    reporting_num = {}
    reported_num = {}
    
    reported_list = []
    RR = []
    
    Report = set(report)
    
    # 딕셔너리에 값 할당
    for key in id_list :
        reporting_num[key] = 0
        reported_num[key] = 0
    
    # 몇 번 신고당했는지 count
    for id in Report :
        reported = id.split(' ')
        RR.append(reported)
        reported_num[reported[1]] = reported_num.get(reported[1]) + 1
        
    # 해당되는 k만 남겨두기
    for key in reported_num.keys() :
        if reported_num[key] >= k : reported_list.append(key)
    
    # k 값과 비교하여 몇 번 메일을 받았는지 count  
    for i in range(len(RR)) :
        if RR[i][1] in reported_list :
            reporting_num[RR[i][0]] = reporting_num.get(RR[i][0]) + 1

    return list(reporting_num.values())