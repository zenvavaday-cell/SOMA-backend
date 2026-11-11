from fastapi import FastAPI

app = FastAPI(title="SOMA Backend", version="0.1.0")

@app.get("/")
def read_root():
    return {"status": "active", "message": "SOMA backend is online"}

@app.post("/chat")
def handle_chat(payload: dict):
    user_message = payload.get("message", "")
    return {"response": f"Echo from SOMA: {user_message}"}
