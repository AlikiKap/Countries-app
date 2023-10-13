from fastapi import FastAPI
import httpx
app = FastAPI()


@app.get("/")
async def root():
    url = "https://countriesnow.space/api/v0.1/countries/iso"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()


# @app.get("/countries/{name}")
# async with httpx.AsyncClient() as client:
#     response = await client.get()
# return response.json()
