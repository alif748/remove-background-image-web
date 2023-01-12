from typing import Union
from fastapi import FastAPI
from starlette.responses import FileResponse
from app.rmbg.rmbg import rmbg
# import sys
# sys.path.insert(0, '/code/app/rmbg')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/rmbg")
def read_item(url: str):
    return FileResponse(rmbg(url))
    # return rmbg(url)
    # return "ok"