# 알고리즘 공부 보초법 순열검색
import time
import random
import copy
def myCode(data_arr,target_num):
    #본인이 짠 순차검색
    #시작시간 체크
    start_time = time.time()
    # 횟수 카운팅을 위한 cnt 선언
    cnt=0
    # 배열 반복문 돌기
    for i in range(len(data_arr)):
        #숫자 비교 횟수 체크
        cnt+=1
        # 배열을 순차적으로 돌면서 target_num와 같은 번호를 찾으면 종료 및 출력
        if data_arr[i] == target_num:
            print(f'{cnt}만큼 비교했습니다.')
            print(f"검색하신 숫자인 {target_num}은 배열에 {i+1}번째에 있습니다.")
            # 종료시간 체크
            end_time=time.time()
            print(f'순수하게 검색에 걸린 시간은 {end_time-start_time}입니다.')
            break
        #만약 target_num과 다르다면 pass
        else:
            if i == len(data_arr)-1:
                print('찾지 못했습니다.')
            pass

def sentinelMethod(data_arr, target_num):
    #보초법으로 풀기
    print('보초법')
    #시작시간 체크
    # 횟수 카운팅을 위한 cnt 선언
    i=0
    copy_data_arr = copy.deepcopy(data_arr)
    # 배열 마지막에 target_num 추가
    copy_data_arr.append(target_num)
    # 배열 반복문 돌기
    start_time = time.time()
    while True:
        if copy_data_arr[i]==target_num:
            break
        i+=1
        end_time = time.time()
    if i ==len(data_arr):
        return print('찾지못했습니다.')
    else:
        return print(f'{i+1}만큼 비교했습니다.\n검색하신 숫자인 {target_num}은 배열에 {i+1}번째에 있습니다.\n순수하게 검색에 걸린 시간은 {end_time-start_time}입니다.')



# 숫자 num을 입력
num = int(input('배열의 크기를 입력해주세요: '))

# 0~(num-1)까지의 정수 배열 생성
data_arr = list(range(num))

#랜덤으로 섞기
random.shuffle(data_arr)

#사용자에게 target_num을 입력 받기
target_num = int(input('검색할 값을 입력해주세요: '))
#함수 실행
myCode(data_arr=data_arr, target_num=target_num)
sentinelMethod(data_arr=data_arr, target_num=target_num)

