from fastapi import FastAPI
from typing import List, Optional  
# List[int], List[str], Optional[str] → type hints for lists and optional values
from enum import IntEnum  
# Example: class Status(IntEnum): OK = 1; ERROR = 2
from pydantic import BaseModel, Field  
# Example: class User(BaseModel): name: str = Field(..., max_length=50)


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

#define a schema for base , use type and size definations for certain fields
class TodoBase(BaseModel):
    text: str = Field(...,max_length=20) #must be filled with str from  4 to 20
    due : str = Field(...,max_length=10)
    priority : Priority =Field(default=Priority.HIGH)

class ATodo(TodoBase):
    id: int =Field(...)

class CreateTodo(TodoBase):
    pass

class UpdateTodo(BaseModel):
    text:  Optional[str] = Field(None,max_length=20) 
    due : Optional[str] = Field(None,max_length=10)
    priority : Optional[Priority] =Field(None)
        
app = FastAPI()

# RANDOM data just to test our study case
todo_list = [
    ATodo(id=1,text="School",due="Today",priority=Priority.HIGH),
    ATodo(id=3,text="gym",due="Tommorow",priority=Priority.LOW),
    ATodo(id=2,text="Buy A laptop",due="Next Week",priority=Priority.MEDIUM),
]

@app.get("/")
def main():
    return {"message": "Hello, World"}

@app.get("/todos",response_model=List[ATodo])
def get_todos(n: int = None):
    return {"todos_until_n": todo_list[:n]}

@app.get("/todos/{todo_id}",response_model=ATodo)
def get_todo_by_id(todo_id: int):
    for item in todo_list:
        if item.id == todo_id:
            return item
    return {"error": "ID not found in DB"}

@app.post("/todos",response_model=ATodo)
def add_todo(todo: CreateTodo): #pass the todo create becaus eit doesnt have an id
    new_id = max(item.id for item in todo_list) + 1
    new_todo = ATodo(
        id= new_id,
        text= todo.text,
        due= todo.due,
        priority= todo.priority
    )
    todo_list.append(new_todo)
    return new_todo

@app.put("/todos/{todo_id}",response_model=ATodo)
def update_list(todo_id:int,new_todo:UpdateTodo):
    for item in todo_list:
        if item.id == todo_id:
            item.text= new_todo.text
            item.due= new_todo.due
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