from fastapi import FastAPI
from api.voivodeships import router as voivodeships_router
from api.hello import router as hello_router

app = FastAPI(
    title="EconomyAtlas API",
    description="Polish administrative & economic data",
    version="0.1.0",
)

app.include_router( voivodeships_router, prefix="/api/voivodeships", tags=["voivodeships"])
app.include_router(hello_router, prefix="/api", tags=["hello"] )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)