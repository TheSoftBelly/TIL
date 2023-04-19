class Stack:
    maxsize = None # 저장할 수 있는 데이터의 수 (배열 크기)
    top = None # 다음에 입력(push)될 데이터를 저장할 인덱스
    items = None # 데이터를 저장할 배열
    
    # 초기화
    def __init__(self, maxsize):
        self.maxsize = maxsize # 배열의 크기
        self.top = 0 # 데이터가 입력되면 0번 인덱스부터 저장
        self.items = [-1] * self.maxsize # 데이터 배열을 -1로 채우기
    
    # 스택에 새로운 값 삽입
    def push(self, inputItem):
        # 스택이 가득 차 있는 경우
        if self.top == self.maxsize:
            print("Error: Stack is full")
        # 스택이 가득 차 있지 않은 경우
        else:
            self.items[self.top] = inputItem
            self.top += 1

    # 스택에서 최상단 데이터 빼기
    def pop(self):
        # 스택이 비어있는 경우
        if self.top == 0:
            print("Error: Stack is empty")
            return None
        # 스택에 데이터가 있는 경우
        else:
            self.top -= 1
            return self.items[self.top]

    # 스택에 들어 있는 데이터 출력
    def Print(self):
        out = '스택 = ['
        for i in range(self.top):
            out += str(self.items[i])
            if i < self.top - 1:
                out += ', '
        out += ']'
        print(out)
    # DFS로 미로를 탐색하는 함수
    def dfs(maze, start, end):
        stc=Stack(maxsize=100)
        stc.push(inputItem=(start, [start]))
        visited = set()
        # 경로 찾기 반복문
        while stc:
            current, path = stc.pop()
            visited.add(current)
            
            print("현재 위치:", current)
            print("지금까지 방문한 위치:", visited)
            stc.Print()
            
            # 현재 위치가 골 지점에 도달하면 종료 및 탈출 성공 시 최종 탈출 경로 출력
            if current == end:
                print("탈출 성공!")
                print("최종 탈출 경로:", path)
                return True
            # 현재위치와 4방위 리스트 호출
            x, y = current
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            # 인접 위치를 확인하면서 탈출하기
            for neighbor in neighbors:
                row, col = neighbor
                # 만약 미로를 초과하지 않는 선에서 인접한게 'O'이거나  'G' 이면 stc에 append 
                if (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and (maze[row][col] == 'O' or maze[row][col] == 'G') and (neighbor not in visited):
                    stc.push(inputItem=(neighbor, path + [neighbor]))
                    
        print("탈출 실패!")
        return False



# "maxe.txt" 파일을 읽어와 미로를 만듦
with open("maze.txt", "r") as f:
    maze = [list(line.strip()) for line in f]
    
# 출발점과 도착점을 찾음
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            end = (i, j)

# DFS로 미로 탐색
Stack.dfs(maze, start, end)