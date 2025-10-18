from fastapi import FastAPI

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
