from fastapi import FastAPI
from typing import List, Optional  
# List[int], List[str], Optional[str] → type hints for lists and optional values
from enum import IntEnum  
# Example: class Status(IntEnum): OK = 1; ERROR = 2
from pydantic import BaseModel, Field  
# Example: class User(BaseModel): name: str = Field(..., max_length=50)


app = FastAPI()

# RANDOM data just to test our study case
todo_list = [
    {"id": 1, "text": "Study", "due": "Tomorrow"},
    {"id": 2, "text": "Go to gym", "due": "Tomorrow"},
    {"id": 3, "text": "Buy a new Laptop", "due": "Next Month"},
]

@app.get("/")
def main():
    return {"message": "Hello, World"}

@app.get("/todos")
def get_todos(n: int = None):
    return {"todos_until_n": todo_list[:n]}

@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todo_list:
        if todo["id"] == todo_id:
            return {"todo": todo}
    return {"error": "ID not found in DB"}

@app.post("/todos")
def add_todo(todo: dict):
    new_id = max(item["id"] for item in todo_list) + 1
    new_todo = {
        "id": new_id,
        "text": todo["text"],
        "due": todo["due"],
    }
    todo_list.append(new_todo)
    return new_todo

@app.put("/todos/{todo_id}")
def update_list(todo_id:int,new_todo:dict):
    for item in todo_list:
        if item["id"]==todo_id:
            item["text"]= new_todo["text"]
            item["due"]= new_todo["due"]
            return item #return the list after we have put into it 
    return "Error The Id to Be edited Wasn't Found"

@app.delete("/todos/{todo_id}")
def  del_list(todo_id:int):
    for index,item in enumerate(todo_list):
        if item["id"]==todo_id:
            deleted_todo=todo_list.pop(index) #remove the item with that id correspending 
            #equally u can just remove it
            return deleted_todo #to check the updated list 
    return "Error The Id to Be edited Wasn't Found"