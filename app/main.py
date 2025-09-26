from fastapi import FastAPI

app = FastAPI(title="Priority API")

@app.get("/priority")
def read_root():
    return{'message': 'Welcome to the Priority API'}
