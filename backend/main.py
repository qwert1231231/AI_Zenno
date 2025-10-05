from fastapi import FastAPI
from pydantic import BaseModel
import os
from . import ai_core, memory, auth, utils

app = FastAPI(title="Zenno AI - Backend")

class ChatRequest(BaseModel):
    user_id: str | None = None
    message: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(req: ChatRequest):
    # simplistic flow: persist to memory, call ai_core, return response
    memory.save_message(req.user_id or "anon", req.message)
    resp = ai_core.generate_reply(req.message)
    memory.save_message(req.user_id or "anon", resp, incoming=False)
    return {"reply": resp}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("HOST", "127.0.0.1"), port=int(os.getenv("PORT", 8000)), reload=True)
