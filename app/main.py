from fastapi import FastAPI, Depends

app = FastAPI()

@app.get("/test")
def testing():
    return {"Hello":"World!!"}