from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# 환경변수 로드
load_dotenv()

app = FastAPI(
    title="AI Study API",
    description="Backend engineer AI study project",
    version="0.0.1"
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "AI Study Server Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/echo")
def echo(req: ChatRequest):
    return {"reply": req.message}