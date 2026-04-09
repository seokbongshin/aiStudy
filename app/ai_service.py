import httpx
import os


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_summary(stats, login_users, top_user):
    prompt = f"""
    다음 로그 통계를 보고 사람이 읽기 쉽게 3줄로 요약해줘.

    총 로그 수 : {stats['total_count']}
    로그인 수 : {stats['login_count']}
    로그아웃 수 : {stats['logout_count']}

    사용자 로그인 횟수 :
    {login_users}

    가장 많이 로그인한 사용자:
    {top_user}
    """

    print(f"============ key :: {OPENAI_API_KEY}")
    response = httpx.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization" : f"Bearer {OPENAI_API_KEY}",
            "Content-Type" : "application/json"
        },
        json={
            "model" : "gpt-4.1-mini",
            "input" : prompt
        },
        timeout=10.0
    )

    if response.status_code != 200:
        print(f"이거 뭐야 :: {response}")
        return "AI 요약 생성 실패"

    data = response.json()

    return data["output"][0]["content"][0]["text"]