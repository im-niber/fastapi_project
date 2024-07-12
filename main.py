from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class HelloResponse(BaseModel):
    message: str | None = None


@app.get("/", response_model=HelloResponse)
async def root() -> HelloResponse:
    return HelloResponse(message="hello world")


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)