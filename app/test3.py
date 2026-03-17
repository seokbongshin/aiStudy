
logs = [
    {"user": "kim", "action": "login"},
    {"user": "lee", "action": "login"},
    {"user": "kim", "action": "logout"},
    {"user": "park", "action": "login"},
    {"user": "lee", "action": "logout"},
    {"user": "kim", "action": "login"},
]

users = ["kim", "lee", "park", "choi"]

def login_counting(logs) :
    login_users = {}
    for log in logs:
        if log["action"] == "login":
            user = log["user"]
            login_users[user] = login_users.get(user, 0) + 1
    return login_users

def log_action(logs, action) :
    user_list = set()
    for log in logs :
        if log["action"] == action :
            user_list.add(log["user"])
        elif log["action"] == action :
            user_list.add(log["user"])
    return user_list

def find_not_login_users(users, login_user_list) :
    not_login_users = [users for user in users if user not in login_user_list]
    return not_login_users

def calc_logStats(logs) :
    logStats = {"totCount" : 0, "totLoginCnt" : 0,"totLogoutCnt" : 0}
    logStats["totCount"] = len(logs)
    logStats["totLoginCnt"] = len( [log for log in logs if log["action"] == "login"] )
    logStats["totLogoutCnt"] = len( [log for log in logs if log["action"] == "logout"] )
    return logStats

def top_login_user(login_users) :
    top_user = ""
    top_count = 0
    for user in login_users:
        if login_users[user] > top_count:
            top_count = login_users[user]
            top_user = user
    
    return top_user

def top_login_user_dict(login_users) :
    top_login_user_dict = {"user" : "", "count" : 0}
    for user in login_users:
        if login_users[user] > top_login_user_dict["count"]:
            top_login_user_dict["count"] = login_users[user]
            top_login_user_dict["user"] = user
    
    return top_login_user_dict

login_users = login_counting(logs)
login_user_list = log_action(logs, "login")
not_logged_in_users = find_not_login_users(users, login_user_list)
total_login = 0
total_logout = 0
logStats = calc_logStats(logs)
top_user = top_login_user(login_users)

print("=== 로그인 횟수 ===")
print(login_users)

print("=== 로그인 사용자 ===")
print(login_user_list)

print("=== 미로그인 사용자 ===")
print(not_logged_in_users)

print("=== 로그 통계 ===")
# print("총 로그 수:", len(logs))
# print("총 로그인 수:", len(log_action(logs, "login")))
# print("총 로그아웃 수:", len(log_action(logs, "logout")))
print(logStats)

print("=== 가장 많이 로그인한 사용자 ===")
print(top_user)
print(top_login_user_dict(login_users))


# GPT 버전
# def login_counting(logs):
#     login_users = {}

#     for log in logs:
#         if log["action"] == "login":
#             user = log["user"]
#             login_users[user] = login_users.get(user, 0) + 1

#     return login_users


# def get_users_by_action(logs, action):
#     user_list = set()

#     for log in logs:
#         if log["action"] == action:
#             user_list.add(log["user"])

#     return user_list


# def find_not_login_users(users, login_user_list):
#     not_login_users = [user for user in users if user not in login_user_list]
#     return not_login_users


# def count_action(logs, action):
#     return len([log for log in logs if log["action"] == action])


# def calc_log_stats(logs):
#     log_stats = {
#         "total_count": len(logs),
#         "total_login_count": count_action(logs, "login"),
#         "total_logout_count": count_action(logs, "logout")
#     }
#     return log_stats


# def top_login_user(login_users):
#     top_user = ""
#     top_count = 0

#     for user, count in login_users.items():
#         if count > top_count:
#             top_count = count
#             top_user = user

#     return top_user


# def top_login_user_dict(login_users):
#     top_login_user_info = {"user": "", "count": 0}

#     for user, count in login_users.items():
#         if count > top_login_user_info["count"]:
#             top_login_user_info["count"] = count
#             top_login_user_info["user"] = user

#     return top_login_user_info


# login_users = login_counting(logs)
# login_user_list = get_users_by_action(logs, "login")
# not_logged_in_users = find_not_login_users(users, login_user_list)
# log_stats = calc_log_stats(logs)
# top_user = top_login_user(login_users)

# print("=== 로그인 횟수 ===")
# print(login_users)

# print("=== 로그인 사용자 ===")
# print(login_user_list)

# print("=== 미로그인 사용자 ===")
# print(not_logged_in_users)

# print("=== 로그 통계 ===")
# print(log_stats)

# print("=== 가장 많이 로그인한 사용자 ===")
# print(top_user)
# print(top_login_user_dict(login_users))