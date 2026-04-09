
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

logs = []
try :
    with open("D:/work/project/aiStudy/logs.txt", "r") as f:
        for line in f:
            try:
                if not line: # EOF
                    continue
                    
                line = line.strip()
                parts = line.split(",")

                if len(parts) != 2 :
                    continue

                log = {"user" : parts[0], "action" : parts[1]}
                logs.append(log)
            except Exception as e:
                print(f"파일 라인 처리 실패: {line} / 에러 : {e}")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"파일 처리 중 오류 발생 : {e}")

print(len(logs))
login_users = login_counting(logs)
print(login_users)