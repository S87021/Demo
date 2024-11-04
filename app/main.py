from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

app = FastAPI()

# 配置模板目录
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def read_index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/hello")
async def read_hello_html(request: Request):
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
