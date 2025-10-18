from fastapi import FastAPI

app = FastAPI()
# RANDOM data just to test our study case
todolist =[
    {
        "IDtodo":1,"TodoText":"Study" , "Due":"Tommorow" 
    },
      {
        "IDtodo":2,"TodoText":"Go to gym" , "Due":"Tommorow" 
    },
      {
        "IDtodo":3,"TodoText":"Buy a new Laptop" , "Due":"Next Month" 
    }
]

@app.get("/")
def main():
    return {"message": "Hello, World"}

@app.get("/todos")
def returnton(n: int = None):
    return {"AllElementsUntiln": todolist[:n]}

# let's define a route by the task idk and return the coressponding id data
# should cast the IDtodo from the url to be compared to int in the list
@app.get("/tododata/{IDtodo}")
def returndatasync(IDtodo):
    for TodoE in todolist:
        if TodoE["IDtodo"] == int(IDtodo):
            return {"UserReq":TodoE}
        
    return{"error":"Id Not Found in DB"}
        
