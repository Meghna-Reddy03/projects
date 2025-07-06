from fastapi import FastAPI

app = FastAPI()

library = []

@app.post("/book/add")
def add_book(name, desc):
    library.append({"name": name, "desc": desc})
    return library

@app.put("/book/update")
def update_book(name, updated_desc):
    for book in library:
        if book['name'] == name:
            book["desc"] = updated_desc
            return library
    else:
        return "No book found"


@app.delete("/book/delete")
def delete_book():
    return "Hello"

@app.get("/book/get")
def get_book():
    return "Hello"



#Adding somethign else