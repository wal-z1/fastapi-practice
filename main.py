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

# let's define a route by the task idk and return the coressponding id data
@app.get("/tododata/{IDtodo}")
async def returndatasync(IDtodo):
    for TodoE in todolist:
        if TodoE["IDtodo"] == IDtodo:
            return {"UserReq":TodoE}