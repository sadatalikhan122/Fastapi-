from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

book=[

    {"Tittle":"titleone","author":"authorone"},
    {"Tittle":"titlesecond","author":"authorsecond"},
    {"Tittle":"titlethird","author":"authorthird"},
    {"Tittle":"titlefourth", "author":"authorfourth"}
]
@app.get("/book")
async def get_book():
    return book
@app.get("/books/{book_title}")
async def get_books(book_title: str):
    for b in book:
        if b.get("Tittle").casefold()== book_title.casefold():
            return b
       