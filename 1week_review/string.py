# 파이썬 문자열, 리스트, 딕셔너리 다루기 마스터해보자

import json

# swit_chat_data 의 키 값을 먼저 뽑아내 준다.
def json_read_file():
    with open('./swit_chat.json', 'r', encoding='UTF8') as jsonfile:
        swit_chat_data = json.load(jsonfile)
        return swit_chat_data


# user_name 글쓴 횟수 찾기

def find_user():
    swit_chat_data = json_read_file()
    user_list = {}
    for user in swit_chat_data['data']:
        if user['content'] != None:
            if user_list.get(user['user_name']):
                user_list[user['user_name']] += 1
            else:
                user_list[user['user_name']] = 1

    return user_list

# user_name 가장 많이 채팅한 사람 찾기
def max_chat():
    users = find_user()
    max_count = 0
    max_chat_user = []
    for chat_user, chat_count in users.items():
        if max_count < chat_count:
            max_count = chat_count
            max_chat_user = chat_user
        elif max_count == chat_count:
            max_chat_user += ','+chat_user

    print(f'가장 많이 채팅한 사람 : {max_chat_user} 채팅 횟수 : {max_count}')


max_chat()






# swit_chat_data 에 담긴 데이터는 실제 광주인공지능사관학교 스윗의 데이터이다.
# 문제 :
# 가장 많이 글을 쓴 채팅을 작성한 사람은 누구일까..?

# 힌트 ) 유저 별 content 수를 세서 누가 가장 많이썼을지 알아보기