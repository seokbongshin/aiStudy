from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File, HTTPException
from app.ai_service import generate_summary


app = FastAPI(
    title="Log Analysis API",
    description="Upload log file and analyze it",
    version="0.0.1"
)

def parse_logs(lines):
    logs = []
    total_count = 0
    valid_count = 0

    for raw_line in lines:
        total_count += 1

        line = raw_line.strip()

        if not line:
            continue

        parts = line.split(",")

        if len(parts) != 2:
            continue

        user, action = parts
        user = user.strip()
        action = action.strip().lower()

        if action not in ["login", "logout"]:
            continue

        logs.append({"user": user, "action": action})
        valid_count += 1

    return logs, total_count, valid_count

def count_login_users(logs):
    login_users = {}

    for log in logs:
        if log["action"] == "login":
            user = log["user"]
            login_users[user] = login_users.get(user, 0) + 1

    return login_users


def count_action(logs, action):
    count = 0

    for log in logs:
        if log["action"] == action:
            count += 1

    return count

def find_top_login_user(login_users):
    top_user = ""
    top_count = 0

    for user, count in login_users.items():
        if count > top_count:
            top_count = count
            top_user = user

    return {
        "user": top_user,
        "count": top_count
    }

def make_log_stats(logs, total_count, valid_count):
    return {
        "total_count": total_count,
        "valid_count": valid_count,
        "login_count": count_action(logs, "login"),
        "logout_count": count_action(logs, "logout")
    }

@app.get("/")
def root():
    return {"message": "Log Analysis API is running"}

@app.post("/analyze")
async def analyze_log_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".txt"):
            raise HTTPException(status_code=400, detail="Only .txt files are allowed")
        
        content = await file.read()
        text = content.decode("utf-8")
        lines = text.splitlines()

        logs, total_count, valid_count = parse_logs(lines)
        login_users = count_login_users(logs)
        top_user = find_top_login_user(login_users)
        stats = make_log_stats(logs, total_count, valid_count)
        summary = generate_summary(stats, login_users, top_user)

        return {
            "file_name" : file.filename,
            "login_users" : login_users,
            "stats" : stats,
            "top_login_user" : top_user,
            "summary": summary,
            "logs" : logs
        }

    except UnicodeEncodeError:
        raise HTTPException(status_code=400, detail="File Must be UTF-8 encoded text")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error : {e}")