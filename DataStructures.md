# Data Structures 대표 키워드 위주 공부
Stack, Queue, Linked-list, Circulat linked list, Doubly linked list, Header node

  ## Stack ) Last In First Out (LIFO) 
  - Method ) push, pop , delete
  - 후입 선출
  - 데이터가 들어온 방향과 나가는 방향이 같다.
  - 표기법 (notation) 구현 예제 : infix notation (중위표현식) , prefix notation (전위표현식), postfix notation (후위표현식 or polish)
  - ex ) A - B * C (중위)
  -      BC*A- (후위)
  -      -*BCA (전위)
  - DFS(깊이우선탐색) 구현시 이용 
  
  ## Queue ) First In Fist Out (FIFO)
  - Method ) inqueue, dequeue
  - 선입 선출
  - 데이터가 들어온 방향과 니가는 방향이 다르다.
  - BFS(너비우선탐색) 구현시 이용 
  - 선착순 서버 (FCFS) 
  - 평균대기시간 (average wating time), 작업처리능력 (throughput), 다중 큐 서버 (multiple queue server)

  ## Linked-list ) value 와 linke 를 가진 node들의 연결 형태
  - Method ) insert , delete
  - 선형 연결리스트 (linear linked list) - 마지막 노드의 link는 null 
      - 삽입 : 1) 추가할 새 노드 생성  2) 새노드의 link를 전노드의 link로 변경 3) 추가할 위치의 전노드를 찾아 전노드의 link를 새노드로 변경
      - 소스 : 
      - 1) new_Node = {"value":null,"link":null}   
      -    new_Node["value"] = '10'
      - 2) new_Node["link"] = pre_Noew["link"]
      - 3) pre_Node["link"] = new_Node
      
      - 삭제 : 1) 삭제할 노드의 이전 노드 찾기 2) 이전노드의 link를 삭제할노드의 link로 변경 3) 삭제할 노드의 link를 null 로 변경
      - 소스 :
      - 1 ) find(pre_Node)
      - 2 ) pre_Node["link"] = target["link"]
      - 3 ) target["link"] = null
      
      
  - 원형 연결리스트 (Circular linked list) - 마지막 노드의 link는 header 
  - 이중 연결리스트 (Doubly linked list) 
      - llink,rlink,value 로 노드 구성
      - 이전값 정보를 가지고 있어, 단순 연결리스트 보다 이전노드 제어가 빠르다.
  - 헤더노드 (Header Node) 
      - 모든리스트에 사용가능
      - length, header, tail 정보 저장
  
  
  
