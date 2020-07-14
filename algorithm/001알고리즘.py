# 내 코드
n = int(input('숫자를 입력하세요'))
# sum_num = []
# for i in range(n):
#     sum_num.append((n+1)*i)
# print(sum(sum_num))


# 선생님 코드
def get_res():
    res = 0
    for i in range(1,n):
        res += i(n+1)
    print(res)

# 선생님 코드
def get_sum():
    res = 0
    for i in range(1,n):
        res += (i*n)+i
    print(res)

# 한줄 짜리 코드
print((n*(n+1)*(n-1))/2)