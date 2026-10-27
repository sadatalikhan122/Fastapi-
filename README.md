
# 📚 FastAPI Book API

A beginner-friendly REST API developed using Python and FastAPI.

This project demonstrates how to build API endpoints, retrieve books, search by title, and handle HTTP requests using FastAPI.

## 🚀 Features

- Retrieve all available books.
- Search for a book by its title.
- Case-insensitive book searching.
- JSON response handling.
- HTTP 404 error handling.
- Interactive Swagger API documentation.

## 🛠️ Technologies Used

- Python
- FastAPI
- Uvicorn
- REST API
- JSON

## 📁 Project Structure

```text
FastAPI-Books-API/
│
├── main.py
└── README.md
```

## ⚙️ Installation

### Step 1: Install Dependencies

```bash
pip install fastapi uvicorn
```

### Step 2: Run the Application

```bash
python -m uvicorn main:app --reload
```

The server will start at:

http://127.0.0.1:8000

### Step 3: Open API Documentation

Visit:

http://127.0.0.1:8000/docs

## 💻 Python Code

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

book = [
    {"Tittle": "titleone", "author": "authorone"},
    {"Tittle": "titlesecond", "author": "authorsecond"},
    {"Tittle": "titlethird", "author": "authorthird"},
    {"Tittle": "titlefourth", "author": "authorfourth"}
]

@app.get("/book")
async def get_book():
    return book

@app.get("/books/{book_title}")
async def get_books(book_title: str):
    for b in book:
        if b.get("Tittle").casefold() == book_title.casefold():
            return b

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /book | Retrieve all books |
| GET | /books/{book_title} | Search for a specific book |
| GET | /docs | Swagger API documentation |

## 📌 Example API Request

### Get All Books

```http
GET http://127.0.0.1:8000/book
```

### Response

```json
[
  {
    "Tittle": "titleone",
    "author": "authorone"
  },
  {
    "Tittle": "titlesecond",
    "author": "authorsecond"
  },
  {
    "Tittle": "titlethird",
    "author": "authorthird"
  },
  {
    "Tittle": "titlefourth",
    "author": "authorfourth"
  }
]
```

### Search Book by Title

```http
GET http://127.0.0.1:8000/books/titleone
```

### Response

```json
{
  "Tittle": "titleone",
  "author": "authorone"
}
```

## 🧠 Concepts Learned

Through this project, I practiced:

- Building REST APIs using FastAPI.
- Creating GET endpoints.
- Working with path parameters.
- Handling Python lists and dictionaries.
- Returning JSON responses.
- Using casefold() for case-insensitive searching.
- Handling errors with HTTPException.
- Testing APIs using Swagger UI.

## 📈 Future Improvements

- Add POST endpoints to create books.
- Implement PUT and DELETE operations.
- Integrate Pydantic models for data validation.
- Connect the API with a SQL database.
- Build an HTML and JavaScript frontend.

## 👨‍💻 Author

**Sadat Ali Khan**

GitHub: https://github.com/sadatalikhan122

LinkedIn: https://www.linkedin.com/in/sadat-ali-khan-90ba701a0/

## 📜 Project Purpose

This project was developed as part of my Python backend development learning journey.

The main objective was to understand fundamental FastAPI concepts, API endpoint creation, path parameters, JSON responses, and basic REST API development.
