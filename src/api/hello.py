from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/hello")
def hello_world():
    return "Hello World!"

@router.get("/goodbye")
def goodbye():
    return {"message": "Do widzenia!"}