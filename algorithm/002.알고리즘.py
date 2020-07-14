# a, b, r 입력 받기
def a_b_R_num():
    while True:
        a,b,R = map(int, input('a b R 값을 차례로 입력해 주세요.').split())
        if (0 <= a <= 100) and (0 <= b <= 100) and (0 <= R <= 100):
            return a,b,R
        else:
            print('다시 입력해주세요.')
# n 값 입력받기
def N_num():
    while True:    
        N = int(input('N값을 입력해주세요.'))
        if (0 <= N <= 1000):
            return N
        else:
            print('다시 입력해주세요.')
# N 번 반복  x_i, y_i 값 입력받기
def Xi_yi_num(N):
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input('x_i y_i 값을 차례로 입력해주세요.').split())
        if (0 <= x_i <= 100) and (0 <= y_i <= 100):
             x.append(x_i), y.append(y_i)
        else:
            print('다시 입력해주세요.')
    return x, y
# 위치 x y 가 공사현장 R 이상 떨어져 있다는 조건
# 출력 silent, noisy
def main():
    a, b, R= a_b_R_num()
    N = N_num()
    x, y = Xi_yi_num(N)
    for i in range(N):
        if ((x[i]-a)**2 + (y[i]-b)**2) >= R**2:
            print('silent')
        else:
            print('noisy')
main()

