# random 함수 선언
import random

# 해시 함수 생성
def hash_function(data, array_size):
    return data % array_size

# 1000개의 중복되지 않은 정수 데이터를 랜덤 생성
data_set = set()
while len(data_set) < 1000:
    data_set.add(random.randint(0, 999))

# 배열 사이즈 생성 및 해쉬테이블 생성
array_size = 1000
hash_table = [None] * array_size

# 충돌 횟수를 초기화
cnt = 0

# 데이터를 배열에 삽입
for data in data_set:
    index = hash_function(data, array_size)
    if hash_table[index] is not None:
        cnt += 1
    hash_table[index] = data

# 충돌 횟수 출력
print("충돌 횟수:", cnt)
