from fastapi import FastAPI
import api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api_router.router, prefix="/v1/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
def testing():
    return {"Hello":"World!!"}