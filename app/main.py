from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# 配置模板目录
templates = Jinja2Templates("templates")
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# 你可以添加更多的路由和逻辑
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
