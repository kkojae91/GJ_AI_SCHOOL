# 1주일 내용 10문제로 끝내기
# 1. 파이썬 조건문을 활용하여 장발장은 빵을 못먹게 하기
# - 실행 예시 : "장발장 차례 입니다, 빵을 드릴 수 없습니다."
# - 실행 예시 : "홍길동 차례 입니다, 빵을 하나 드리겠습니다."

people = ['홍길동', '성진', '심청이', '장발장', '심봉사']

for i in people:
    if i == '장발장':
        print(f'{i} 차례 입니다, 빵을 드릴 수 없습니다.')
    else :
        print(f'{i} 차례 입니다, 빵을 하나 드리겠습니다.')

print('-'*30)
print('-'*30)
# 2. 1번 문제의 구현된 부분을 함수로 바꾸기
# - 조건 : 입력값(사람 한 명씩) 을 받아서 빵을 먹으면 안되는 사람이면 0을, 먹어도 되면 1을 반환하기
# - 실행 예시 : "홍길동은 빵을 먹을 수 있는 사람 입니다."
# - 실행 예시 : "장발장은 빵을 먹을 수 없는 사람 입니다."
# 반복문을 활용하여 5 명 전원 다 출력 할 것

def bread_eat_people(people):
    if people == '장발장':
        print(f'{people}은 빵을 먹을 수 없는 사람입니다.')
        return 0

    else:
        print(f'{people}은 빵을 먹을 수 있는 사람입니다.')
        return 1

for i in people:
    bread_eat_people(i)
    

print('-'*30)
print('-'*30)

# 3. 지역변수와 전역변수 이해하기

# 아래의 코드는 num_stamp 라는 전역변수를 함수 내에서 global 명령을 통해 수정가능하게 억지로 만든상태이다.
# 하지만, 함수의 기능과 본질을 생각하면 아래의 예시는 굉장히 바람직하지 못하다!
# global 명령은 안쓰는 것이 좋다!
# 그렇다면, global 명령을 사용하지 않고 아래의 로직을 함수의 입력값과 반환값을 활용하여 수정해보기!

num_stamp = 0  # 쿠폰 스탬프가 찍힌 횟수 (전역변수)

def stamp(num_stamp):
    num_stamp += 1
    print(num_stamp)
    return num_stamp

num_stamp = stamp(num_stamp)
num_stamp = stamp(num_stamp)

print('-'*30)
print('-'*30)
# 4. 클래스 이용하기
# 요구사항
# - 교통수단 클래스 만들기 (속성 : 이름, 가격, 출발시간, 도착시간 / 기능 : 출발시간, 도착시간 보기)
# - 비행기 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 수하물 가능여부
# 기능 : 출발시간, 도착시간 보기, 수하물 맡기기(수하물이 가능하면 "수하물을 맡겼습니다!"출력, 불가능하면 "이 비행기는 수하물을 못맡깁니다!" 출력)
# - 기차 클래스 만들기
# 속성 : 이름, 가격, 출발시간, 도착시간, 좌석등급
# 기능 : 출발시간, 도착시간 보기, 좌석등급 보기

# 클래스를 상속을 활용해서 효율적으로 만들어 볼것! (메소드 오버라이딩)
# 두 개 이상의 인스턴스를 비행기, 기차 각각 만들어 볼것

class Transportation():
    def __init__(self, name, price, departure_time, arrival_time):
        self.name = name
        self.price = price
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def print_departure_time(self):
        print(f'{self.name} 출발시간 = {self.departure_time}')

    def print_arrival_time(self):
        print(f'{self.name} 도착시간 = {self.arrival_time}')

    
class Airplain(Transportation):
    def __init__(self, name, price, departure_time, arrival_time, baggage):
        super().__init__(name, price, departure_time,arrival_time)
        self.baggage = baggage

    def baggage_can(self):
        if self.baggage == 1 :
            print('수화물을 맡겼습니다.')
        else:
            print('수화물을 맡기지 않았습니다.')

class Train(Transportation):
    def __init__(self, name, price, departure_time, arrival_time, seatclass):
        super().__init__(name, price, departure_time, arrival_time)
        self.seatclass = seatclass
    
    def your_seatclass(self):
        if self.seatclass == 1:
            print('1등석입니다.')
        elif self.seatclass == 2:
            print('2등석입니다.')
        else:
            print('일반석입니다.')

airplain = Airplain('대한한공','20000','05:00','07:00','1')
train = Train('srt','15000','05:00','06:00','2')

airplain.print_departure_time()
airplain.print_arrival_time()
airplain.baggage_can()

train.print_departure_time()
train.print_arrival_time()
train.your_seatclass()
