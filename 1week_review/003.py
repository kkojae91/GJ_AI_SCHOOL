import json


with open('./swit_chat.json', 'r', encoding='UTF8') as jsonfile:
    swit_chat_data = json.load(jsonfile)

    users_content = {}
    for user in swit_chat_data['data']:
        if user['content'] is not None:
            if users_content.get(user['user_name']):
                users_content[user['user_name']] += 1
                print(users_content)
            else:
                users_content[user['user_name']] = 1

# print(users_content)