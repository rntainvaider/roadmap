from fastapi import FastAPI
import httpx
import uvicorn
from database import add_in_database_quote

app = FastAPI()

QUOTE_API_URL = "https://api.quotable.io/random"


@app.get("/fetch-quote/")
async def get_quote():
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get(QUOTE_API_URL)
        data = response.json()
    return {"content": data["content"], "author": data["author"]}


@app.post("/save-quote/")
async def add_in_database_random_quote():
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.get("http://127.0.0.1:8000/fetch-quote/")
        data = response.json()
        # add_in_database_quote(data["content"], data["author"])
        return {"content": data["content"], "author": data["author"]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
