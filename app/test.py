
users = [
    {"name": "kim", "age": 30},
    {"name": "lee", "age": 25}
]

for user in users:
    print(f"{user['name']} : {user['age']}")

logs = [
    {"user": "kim", "action": "login"},
    {"user": "lee", "action": "login"},
    {"user": "kim", "action": "logout"},
    {"user": "park", "action": "login"},
    {"user": "lee", "action": "logout"},
    {"user": "kim", "action": "login"},
]

users = ["kim", "lee", "park", "choi"]

loginUsers = {}
loginUsers2 = []
set_loginUsers = set()
notLogingUsers = []

logStats = {"totCount" : 0, "totLoginCnt" : 0
            ,"totLogoutCnt" : 0}


logStats['totCount'] = len(logs)

for log in logs:
    if(log['action'] == 'login'):
        set_loginUsers.add(log['user'])
        loginUsers[log['user']] = loginUsers.get(log['user'],0) + 1
        logStats['totLoginCnt'] = logStats['totLoginCnt'] + 1
        loginUsers2.append(log['user'])
    if(log['action'] == 'logout'):
        logStats['totLogoutCnt'] = logStats['totLogoutCnt'] + 1
    


for user in users:
    logCount = 0
    for log in logs:
        if(user == log['user'] and log['action'] == 'login') :
            logCount = logCount + 1
    if(logCount <= 0) :
        notLogingUsers.append(user)

def calcAction(logs, action) :
    count = 0
    for log in logs:
        if(log['action'] == action):
            count = count + 1

    return count

print('=== 로그인 횟수 ===')
print(loginUsers)

print('=== 로그인 사용자 ===')
print(set_loginUsers)

print('=== 미로그인 사용자 ===')
print(notLogingUsers)

print('=== 로그 통계 ===')
print(f"총 로그 수 : {logStats['totCount']}")
print(f"총 로그인 수 : {logStats['totLoginCnt']}")
print('=== 로그인 횟수 함수 ===')
print(calcAction(logs, 'login'))
print(f"총 로그아웃 수 : {logStats['totLogoutCnt']}")
print('=== 로그아웃 횟수 함수 ===')
print(calcAction(logs, 'logout'))

print('=== 로그인 사용자2 ===')
print(loginUsers2)

manyUser = ""
maxLogin = 0
countLogin = 0

for user in loginUsers:
    countLogin = loginUsers[user]
    if(countLogin > maxLogin):
        maxLogin = countLogin
        manyUser = user

print('=== 가장 많이 로그인한 사용자 ===')
print(manyUser)
    





# data = ['a', 'b', 'a', 'c']
# count_dict = {}
# for item in data:
#     count_dict[item] = count_dict.get(item, 0) + 1

# print(count_dict)