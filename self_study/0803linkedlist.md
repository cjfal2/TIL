# 8장 Linked List 연결 리스트

## 리스트

1. 순차 리스트
    - 배열을 기반으로 구현된 리스트
2. 연결 리스트
    - 메모리의 동적할당을 기반으로 구현된 리스트
- 리스트 복사 (아래로 갈수록 시간이 많이 걸림)
    - 주소의 복사(얕은 복사)
        - new_list = old_list
    - 슬라이싱 (깊은 복사)   (시간상 추천!)
        - new_list = old_list[:]
    - extend() : 리스트를 추가하는 함수 (깊은 복사)
        - new_list = []
        - new_list.extend(old_list)
    - list() (깊은 복사)
        - new_list = list(old_list)
    - copy활용 (깊은 복사)
        - import copy       new_list = copy.copy(old_list)
    - 리스트함축 , 리스트컴프리핸션(깊은 복사)
        - new_list = [i for i in old_list]
    - 리스트 원소까지도 깊은 복사 (깊은 복사)
        - import copy     new_list = copy.deepcopy(old_list)

## 연결 리스트

- 초기화 및 생성
    - 변수에 값을 초기화 하는 것으로 리스트를 생성
- 데이터 접근
    - 리스트의 인덱스를 이용해 원하는 위치의 데이터를 변경하고 참조할 수 있음
- 자료의 삽입/삭제 연산
    - 원소의 이동 작업이 필요
    - 원소의 개수가 많고 연산이 빈번하면 소요되는 시간이 크게 증가
- 연결 리스트
    - 리스트의 단점을 보완한 자료 구조
    1. 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, **개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조**를 이룸
    2. 링크를 통해 원소에 접근하므로, 순차 리스트에서 **물리적인 순서를 맞추기 위한 작업이 필요하지 않음**
    3. 자료구조의 크기를 동적으로 조정할 수 있어, **메모리의 효율적인 사용이 가능**
    4. 연결 리스트에서 탐색시 순차탐색이 필요
- 연결 리스트 사용을 위한 주요 함수!
    
    ```python
    addtoFirst()  #연결 리스트의 앞쪽에 원소를 추가하는 연산
    addtoLast()   #연결 리스트의 뒤쪽에 원소를 추가하는 연산
    add()         #연결 리스트의 특정 위치에 원소를 추가하는 연산
    delete()      #연결 리스트의 특정 위치에 있는 원소를 삭제하는 연산
    get()         #연결 리스트의 특정 위치에 있는 원소를 리턴하는 연산 
    ```
    
- 노드
    - 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료단위
        - 데이터 필드 : 원소의 값을 저장하는 자료구조
        - 링크 필드 : 다음 노드의 주소를 저장하는 자료구조
- 헤드
    - 리스트의 처음 노드를 가리키는 레퍼런스
    - 리스트의 처음 노드만을 가리키는 링크필드만 가지고 있어 헤드 자체에는 데이터가 저장되지 않음
- 단순 연결 리스트
    - 노드가 하나의 링크필드에 의해 다음 노드와 연결되는 구조를 가짐
    - 헤드가 가장 앞의 노드를 가리키고, 각 노드의 링크 필드가 연속적으로 다음 노드를 가리킴
    - 최종적으로 None을 가리키는 노드가 리스트의 가장 마지막 노드임
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1aed0f6f-08f5-4d20-b8da-658c95411a7a/Untitled.png)
        
- 단순 연결 리스트 삽입 예시 ( A,C,D를 원소로 가지는 리스트의 두 번째에 B 삽입)
    1. 메모리를 할당하여 새로운 노드 new 생성
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/285f4228-36a1-45cd-9d5f-6b24fa113bfe/Untitled.png)
        
    2. 새로운 노드 new의 데이터 필드에 ‘B’ 저장
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c008cb6-02a3-42af-a3c5-7c41874eca50/Untitled.png)
        
    3. 삽입될 위치의 바로 앞에 위치한 노드의 링크 필드를 new에 복사
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/17bfbe46-411b-4f07-8597-3b6eda7b723b/Untitled.png)
        
    4. new의 주소를 앞 노드의 링크 필드에 저장
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1cc72e1-6c29-40f5-8c11-f27950a841f6/Untitled.png)
        
- 첫 번째 노드로 삽입하는 알고리즘

```python
def addtoFirst(data):         # 첫 노드에 데이터 삽입
		global Head
		Head = Node(data,Head)    # 새로운 노드 생성
```

- 새  노드를 가운데 노드로 삽입하는 알고리즘
    - 노드 pre의 다음 위치에 노드 삽입
        - pre 노드의 데이터가 None이 아닐 때만 새 노드를 생성
        - 데이터 필드를 작성한 후 삽입할 노드의 링크 필드에 프리 노드의 링크를 복사
        - pre 의 링크를 삽입할 노드의 주소로 바꿔줌

```python
def add(pre,data):
		if pre == None :
				print('error')
		else :
				pre.link = Node(data,pre.link)
```

- 마지막 노드로 삽입하는 알고리즘
    - 새로운 노드를 생성하고 삽입하려는 리스트가 빈리스트인 경우 최초 노드로 추가
    - 비어있지 않은 리스트인 경우, 마지막 노드를 찾을 때까지 (link가 None을 받을 때까지) 링크를 순회하고 링크의 마지막 위치에 노드를 추가

```python
def addtoLast(data):
		global Head
		if Head == None :
				Head = Node(data, None)
		else :
				p = head
				while p.link != None :
						p = p.link
				p.link = Node(data, None)
```

- 단순 연결 리스트의 삭제 연산
    1. 삭제할 노드의 앞 노드(선행 노드) 탐색
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/afe5f93c-e8c3-4823-9172-828385f0d021/Untitled.png)
        
    2. 삭제할 노드의 링크 필드를 선행 노드의 링크 필드에 복사
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/86cddb26-f172-4b1f-9edf-8b5ead032eb9/Untitled.png)
        
        → 결과적으로 B를 가리키는 노드가 아무것도 없기 때문에 삭제된 것이나 마찬가지
        
- 첫 번째 노트를 삭제하는 알고리즘
    
    ```python
    def deletetoFist():
    		global Head
    		if Head == None :
    				print('error')
    		else :
    				Head = Head.link
    ```
    
- 노드를 삭제하는 알고리즘
    - 노드 pre의 다음 위치에 있는 노드 삭제
    - 삭제할 노드에 있던 링크필드를 선행 노드의 링크필드에 복사
    
    ```python
    def delete(pre):
    		if pre == None or pre.link==None: 
    				print('error')
    		else:
    				pre.link = pre.link.link
    ```
    
- 이중 연결 리스트
    - 양쪽 방향으로 순회할 수 있도록 노드를 연결할 리스트
    - 두 개의 링크 필드와 한 개의 데이터 필드로 구성
- 이중 연결 리스트 삽입 과정 (cur이 가리키는 노드 다음에 D값을 가진 노드를 삽입)
    1. 메모리를 할당하여 새로운 노드 new를 생성하고 데이터 필드에 ‘D’를 저장
    2. cur의 next를 new의 next에 저장하여 cur의 다음 노드를 삽입할 노드의 다음 노드로 연결
    3. new의 값을 cur의 next에 저장하여 삽입할 노드를 cur의 다음 노드로 연결
    4. cur의 값을 new의 prev 필드에 저장하여 cur를 new의 이전 노드로 연결
    5. new의 값을 new가 가리키는 노드의 다음 노드의 prev 필드에 저장하여 삽입하려는 노드의 다음 노드와 삽입하려는 노드를 연결
    - 모두 4개의 링크연산이 필요하다.
- 이중 연결 리스트의 삭제 연산
    1. 삭제할 노드의 다음 노드의 주소를 삭제할 노드의 이전 노드의 next 필드에 저장하여 링크를 연결
    2. 삭제할 노드의 다음 노드의 prev 필드에 삭제할 노드의 이전 노드의 주소를 저장하여 링크를 연결
    3. cur이 가리키는 노드에 할당된 메모리를 반환

# 삽입 정렬

- 자료 배열의 모든 원소들을 앞에서부터 차례대로 이미 정렬된 부분과 비교하여, 자신의 위치를 찾아냄으로써 정렬을 완성
- n의 개수가 작을 때 효과적이다.
- 과정 (시간복잡도 O(n^2) - 각 부분집합의 원소를 매번 비교해야 해서)
    1. 정렬할 자료를 두 개의 부분집합 S와 U로 가정
        - 부분집합 S : 정렬된 앞부분의 원소들
        - 부분집합 U : 아직 정렬되지 않은 나머지 원소들
    2. 정렬되지 않은 부분집합 U의 원소를 하나씩 꺼내서 이미 정렬 되어있는 부분집합 S의 마지막 원소부터 비교하면서 위치를 찾아 삽입 (반복)
    3. 삽입 정렬을 반복하면서 부분집합 S의 원소는 하나씩 늘리고 부분집합 U의 원소는 하나씩 감소하게 함
    4. 부분집합 U가 공집합이 되면 삽입 정렬이 완성됨

# 병합 정렬

- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 연결 리스트에서 가장 효율적인 방식
- 분할 정복 알고리즘 활용
    - 자료를 최소 단위의 문제까지 나눈 후에 차례대로 정렬하여 최종 결과를 얻어냄
    - Top-down 방식이라고도 함
    - 시간 복잡도 : O(n log n )
- 과정
    1. 분할 단계
        - 전체 자료 집합에 대하여, 최소 크기의 부분집합이 될 때까지 분할 작업을 계속함
        - 분할 과정의 알고리즘 (재귀!)
        
        ```python
        def merge_sort(m):
        		if len(m) <= 1 : #사이즈가 0이거나 1인 경우, 바로 리턴을 줌
        				return m
        		# 1. DIVIDE 부분
        		mid = len(m)//2
        		left = m[:mid]
        		right = m[mid:]
        		
        		# 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
        		left = merge_sort(left)
        		right = merge_sort(right)
        
        		# 2. CONQUER 부분 : 분할된 리스트들 병합
        		return merge(left, right)
        	
        ```
        
    2. 병합 단계
        - 2개의 부분집합을 정렬하면서 하나의 집합으로 병합
        - 8개의 부분집합이 1개로 병합될 때까지 반복함
        - 병합 과정의 알고리즘
            
            ```python
            def merge(left,right)
            		result = []  #두 개의 분할된 리스트를 병합하여 result를 만듦
            		
            		while len(left) > 0 and len(right) > 0 : #양쪽 리스트에 원소가 남아있는 경우
            				# 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가함
            				if left[0] <= right[0] :
            						result.append(left.pop(0))
            				else :
            						result.append(right.pop(0))
            				
            		if len(left) > 0 :  #왼쪽 리스트에 원소가 남아있는 경우
            				result.extend(left)
            		if len(right) > 0 : #오른쪽 리스트에 원소가 남아있는 경우
            				result.extend(right)
            		return result
            ```
            
            - 병합 과정에서 사용할 수 있는 자료구조는 배열과 연결 리스트가 있다.
                - 배열 : 분리 병합 과정에서 자료의 비교연산과 이동연산이 빈번하게 발생하여 비효율적이다.
                - 연결 리스트 : 배열의 단점 극복 가능

# Linked List의 활용

- 연결 리스트를 활용하여 Stack을 구현할 수 있다.
    - 스택의 원소 : 리스트의 노드
    - 스택 내의 순서는 리스트의 링크를 통해 연결됨
    - Push : 리스트의 마지막에 노드 삽입
    - Pop : 리스트의 마지막 노드 반환/삭제
    - Top 변수 : 연결 리스트의 맨 앞 노드를 가리키게 된다. 초기 상태는 None 이다.
- 리스트를 이용한 psuh와 pop 연산 구현
    1. None 값을 가지는 노드를 만들어 스택 초기화
    2. 원소 A 삽입 : push(A)
    3. 원소 B 삽입 : push(B) (A의 뒤에 삽입됨)
    4. 원소 C 삽입 : push(C)
    5. 원소 반환 : pop()  (맨 뒤에 있는 C가 반환되고 Top노드가 B를 가리키게 됨)
    
    ```python
    def push(i):    # 원소 i를 스택 top(맨 앞) 위치에 push
    		global top
    		top = Node(i,top)   # 새로운 노드 생성
    
    def pop():   # 스택의 top을 pop
    		global top
    		
    		if top == None :  # 빈 리스트이면
    			print("error")
    		else :
    			data = top.data
    			top = top.link # top이 가리키는 노드를 바꿈
    			return data
    ```
    
- 우선순위 큐
    - 연결 리스트를 이용한 우선순위 큐
    - 기본 연산
        - 삽입 : enQueue
        - 삭제 : deQueue
- 우선순위 큐 구현 - 배열
    - 순차 리스트를 이용하여 자료 저장
    - 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조
    - 가장 앞에 최고 우선순위의 원소가 위치하게 됨
    
    → 문제점
    
    - 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때, 원소의 재배치가 발생하여 소요시간과 메모리 낭비가 큼
- 우선순위 큐 구현 - 연결 리스트
    - 연결 리스트를 이용하여 자료 저장
    - 원소를 삽입하는 과정에서 리스트 내 노드의 원소들과 비교하여 적절한 위치에 노드를 삽입
    - 리스트의 가장 앞쪽에 최고 우선순위가 위치하게 됨
    
    → 배열 대비 장점
    
    - 삽입 / 삭제 연산 이후 원소의 재배치가 필요 없음
    - 메모리의 효율적인 사용
