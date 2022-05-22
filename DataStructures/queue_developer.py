# [출처]프로그래머스_ 기능개발
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
# 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

import math
def solution(progresses, speeds):
    # progresses + speeds * 날수 > 100 일때 배포가능
    answer = []
    temp = []
    res =[]
    for i in range(0,len(progresses)):      #몇일이 남은지 리스트에 저장
        day_left = 100 - progresses[i]
        temp.append(math.ceil(day_left / speeds[i]))
    
    # 1 7 9 -> 2, 1
    # 5 10 1 1 20 1 -> 1, 3, 2
    while temp:
        left = temp.pop(0)      #pop해서 기준 값보다 작은날들 추가
        result = 1              #같은날 배포 수(최소 본인포함해야하므로 1)
        while len(temp) !=0 and left >= temp[0] :   #temp[0]이 처음값보다 작으면 추가
            result += 1         #같은날 배포수 추가
            temp.pop(0)         #temp에서 제거
        answer.append(result)   #배포수 append

    return answer
