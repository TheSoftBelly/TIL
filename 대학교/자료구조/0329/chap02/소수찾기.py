# 소수 나열하기
# 실습 과제 난이도 3
# 1000이하의 모든 소수를 나열하는 프로그램
# 시간 체크를 위해 time 선언
import time
# 입력받은 자연수까지의 소수 찾기 - 내가 처음 작성한 코드
def myAlgo(maxNumber):
    # 시작시간 체크
    start_time = time.time()
    # 소수를 담아주기 위한 빈 리스트 생성
    i_list =[]
    # 연산횟수 체크를 위한 변수 선언
    cnt_num = 0
    for i in range(1,maxNumber+1):
        # 공간 복잡도를 줄이기 위해 연산한 리스트를 항상 초기화
        k_list = []
        for k in range(1,i+1):
            # 연산횟수 카운트
            cnt_num +=1
            if len(k_list)>2:
                break
            # 나머지가 0이면 약수다 생각해서 list에 넣음
            elif i%k==0:
                k_list.append(k)
            else:
                pass
        # 소수는 1과 자기 자신만을 약수로 가지기 떄문에 리스트 개수가 2인것만 리스트에 넣음
        if len(k_list) ==2:
            i_list.append(i)
    end_time = time.time()
    print("찾은 소수 중에서 가장 큰 소수: ",i_list[-1])
    print("연산 횟수: ",cnt_num)
    print("순수하게 연산하는 시간: ", end_time-start_time)


# 실습 2-8을 참조해서 작성한 코드
def do1Algo(maxNumber):
    # 시작시간 체크
    start_time = time.time()
    counter = 0
    # 소수 마지막 번호 저장을 위한 변수 선언
    num = 0

    for n in range(2,1001):
        for i in range(2,n):
            counter +=1
            if n%i == 0:        # 나누어 떨어지면 소수가 아님
                break           # 반복이 더이상 불필요
        else:
            num = n
    print("찾은 소수 중에서 가장 큰 소수: ",num)
    print("연산 횟수: ",counter)
    end_time = time.time()
    print("순수하게 연산하는 시간: ", end_time-start_time)

# 실습 2-9
def do2Algo(maxNumber):
    # 시작시간 체크
    start_time = time.time()
    counter = 0  # 곱셈과 나눗셈을 합한 횟수
    ptr = 0     # 이미 찾은 소수의 개수
    prime = [None] *500 #소수 저장 배열 생성

    prime[ptr]=2
    ptr +=1
    for n in range(3,maxNumber,2):
        for i in range(1,ptr):
            counter+=1
            if n% prime[i]==0:
                break
        else:
            prime[ptr]=n
            ptr+=1
    end_time = time.time()
    print("찾은 소수 중에서 가장 큰 소수: ",prime[ptr-1])
    print("연산 횟수: ",counter)
    print("순수하게 연산하는 시간: ", end_time-start_time)



# 실습 2-10을 참조해서 작성한 코드
def do3Algo(maxNumber):
    # 시작시간 체크
    start_time = time.time()
    counter = 0  # 곱셈과 나눗셈을 합한 횟수
    ptr = 0     # 이미 찾은 소수의 개수
    prime = [None] *500 #소수 저장 배열 생성

    prime[ptr]=2
    ptr +=1
    prime[ptr]=3
    ptr +=1

    for n in range(5,maxNumber,2):       #홀수만을 대상으로 설정
        i=1
        while prime[i] * prime[i]<=n:
            counter +=2
            if n%prime[i]==0:   # 나누어 떨어지기 때문에 소수가 아니다.
                break
            i+=1
        else:                   # 끝까지 나누어 떨어지지 않으면 소수 배열에 등록
            prime[ptr]=n
            ptr +=1
            counter+=1

    end_time = time.time()
    print("찾은 소수 중에서 가장 큰 소수: ",prime[ptr-1])
    print("연산 횟수: ",counter)
    print("순수하게 연산하는 시간: ", end_time-start_time)

# 사용자에게 자연수 입력받기
maxNumber = int(input("자연수를 입력해주세요: "))
print("내가 작성")
myAlgo(maxNumber)
print("*"*100)
print("2-8")
do1Algo(maxNumber)
print("*"*100)
print("2-9")
do2Algo(maxNumber)
print("*"*100)
print("2-10")
do3Algo(maxNumber)