#[문제출처] 프로그래머스_코딩테스트연습 - 프린터
#1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
#2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
#3. 그렇지 않으면 J를 인쇄합니다.

def solution(priorities, location):
    # 우선순위 큐 queue
    # 가장앞에 있는 문서를 꺼낸다 -> top
    # 나머지 인쇄 대기목록에서 J 보다 중요도가 높은문서가 있다면 J를 마지막에
    # 아니면 J인쇄     
    # queue = []
    # 출력  'C''D','A','B'
    queue = []
    cnt = 0
    answer = 0
    for i in range(0,len(priorities)):            #queue생성
        dic = {"val":"","idx":""}
        dic["val"] = priorities[i]
        dic["idx"] = i
        queue.append(dic)
    
    while queue:
        
        max = queue[0]["val"] 
        target = queue[0]
        
        for j in range(0,len(queue)):
            if max < queue[j]["val"] : #max값 찾기
                max = queue[j]["val"]
        
        if max > target["val"]: 
            
            # 나머지 인쇄 대기목록에서 J 보다 중요도가 높은문서가 있다면 J를 마지막에
            temp = target
            queue.pop(0)
            queue.append(temp)
            
        else:
            cnt +=1 
            queue.pop(0)
            if int(target["idx"]) == location:
                break 
            
            
            
            
    
    return cnt
