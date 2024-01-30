from fastapi import FastAPI

app = FastAPI()

@app.get('/{id}')
def getId(id):
    return {"id": id}

@app.get('/')
def getAll():
    return {"all": "Todos"}