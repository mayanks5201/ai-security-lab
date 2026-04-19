from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Security Lab Active"}

@app.get("/chat")
def chat(user_input: str):
    return {"response": f"AI received: {user_input}"}
