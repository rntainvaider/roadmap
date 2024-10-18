from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app"), name="static")

apps = Jinja2Templates(directory="app")

@app.get("/item/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return apps.TemplateResponse(
        request=request, name="index.html", context={"id": id}
        )