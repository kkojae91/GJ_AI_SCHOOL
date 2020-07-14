# 최대값 최소값 구하기.
# 함수 구현 없이 구하기.
num = [1, 2, 100, 3, 30]

num_max = num[0]
num_min = num[0]
for i in range(len(num)):
    if num_max <= num[i]:
        num_max = num[i]
    if num_min >= num[i]:
        num_min = num[i]
print(num_max,num_min)
