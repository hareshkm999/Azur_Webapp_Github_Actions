import uvicorn
from fastapi import FastAPI
import os

# load environment variables
port = 5200

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data": "Application ran successfully - FastAPI release v2.0"}

 
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)