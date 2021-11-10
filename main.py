from fastapi import FastAPI
import api

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "api_name": "dtu-api",
        "repository": "https://github.com/dvishal485/dtu-api",
        "author": "dvisha485@gmail.com",
        "author_github": "https://github.com/dvishal485",
        "description": "Unofficial API for Delhi Technological University (DTU) website",
        "usage": "https://dtu-api.vercel.app/api"
    }


@app.get("/api")
def getAPI():
    result = api.dtu()
    return result
