from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {
        'api_name': 'dtu-api',
        'repository': 'https://github.com/dvishal485/dtu-api',
        'author': 'dvisha485@gmail.com',
        'author_github': 'https://github.com/dvishal485',
        'description': 'Unofficial API for Delhi Technological University (DTU) webpage',
        'usage': {
            'information': 'https://dtu-api.vercel.app/api',
            'full_webpage': 'https://dtu-api.vercel.app/webpage',
            'result_page': 'https://dtu-api.vercel.app/exam'
        }
    }


@app.get('/api')
def getAPI():
    result = api.dtuMainWebpage()
    return result


@app.get('/webpage')
def getAPIextended():
    result = api.dtuMainWebpage(extended=True)
    return result


@app.get('/exam')
def getExamAPI():
    result = api.exam()
    return result


@app.get('/notices')
def getAPI():
    result = api.fetch_notices()
    return result
