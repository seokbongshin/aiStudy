logs = [
    {"user": "kim", "action": "login"},
    {"user": "lee", "action": "login"},
    {"user": "kim", "action": "logout"},
    {"user": "park", "action": "login"},
    {"user": "lee", "action": "logout"},
    {"user": "kim", "action": "login"},
]

users = ["kim", "lee", "park", "choi"]

login_users = {}
login_user_list = []
not_logged_in_users = []
total_login = 0
total_logout = 0

for log in logs:
    if log["action"] == "login":
        user = log["user"]
        login_users[user] = login_users.get(user, 0) + 1
        login_user_list.append(user)
        total_login += 1
    if log["action"] == "logout":
        total_logout += 1

for user in users:
    found = False
    for log in logs:
        if log["user"] == user and log["action"] == "login":
            found = True
    if found == False:
        not_logged_in_users.append(user)

top_user = ""
top_count = 0

for user in login_users:
    if login_users[user] > top_count:
        top_count = login_users[user]
        top_user = user

print("=== 로그인 횟수 ===")
print(login_users)

print("=== 로그인 사용자 ===")
print(login_user_list)

print("=== 미로그인 사용자 ===")
print(not_logged_in_users)

print("=== 로그 통계 ===")
print("총 로그 수:", len(logs))
print("총 로그인 수:", total_login)
print("총 로그아웃 수:", total_logout)

print("=== 가장 많이 로그인한 사용자 ===")
print(top_user)