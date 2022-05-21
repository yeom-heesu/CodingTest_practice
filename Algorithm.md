# Algorithm

## Tree ) 노드들을 선으로 연결한 계층형 자료구조 (Hieraechical)
  - root : 최상위 노드 ,부모노드
  - internal node (내부노드) : 단말노드가 아닌 노드
  - leaf node (리프노드),ternal node (단말노드) : 자식이 더이상 존재하지 않는 노드
  - level : root 부터 0, 부모의 자식은 부모 level + 1
  - degree : 차수, 서브트리의 수(자식의 수)
  - degree of tree : 트리의 최대 차수

## Binary Search Tree (BST)
  - 모든 원소는 상이한 키를 갖는다.
  - 왼쪽 서브트리의 원소 키들은 그 루트의 키보다 작다.
  - 오른쪽 서브트리의 원소 키들은 그 루트의 키보다 크다.
  -         10              10
  -       5     30  (O)  20      30 (X)
  - Complete Binary Search Tree (완전이진트리)
      - 이진트리와 같지만, 단말노드(리프노드) 외 모든 노드가 채워져 있어야한다.
      -            10                   10
      -               15  (X)        3     15  (O)
      -            13    19              7    20
## Heap (히프) 
  - 노드의 키값이 그자식의 키값보다 작지않은 완전이진트리
  -           30                
  -       10     20
  -      3  5  10  15
