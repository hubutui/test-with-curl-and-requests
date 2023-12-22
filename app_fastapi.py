#!/usr/bin/env python3
#
from fastapi import FastAPI, Query
import uvicorn
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/api/translate_v1")
async def translate_v1(text: str = Query(..., description="text to translate")):
    return {"message": text}


@app.post("/api/translate_v2")
async def translate_v2(item: Item):
    return {"message": item.text}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
