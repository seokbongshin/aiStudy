from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Study API")

class EchoRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/echo")
def echo(req: EchoRequest):
    return {"echo": req.message}

@app.get("/async-demo")
async def async_demo():
    return {"message": "this is async endpoint"}