# Fast API
# Installation: pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn

# 1 Create the FASTAPI application instance
app = FastAPI(
    title="My First API",
    description="This is my first FastAPI app",
    version="1.0.0"
)

# 2 Define a route (endpoint)
# get: retrieve data, no modification of the data possible
@app.get("/")
async def root():
    # root: root endpoint / base url
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name:str):
    # root: root endpoint / base url
    return {"message": f"Hello, {name}!"}

# Run our application
if __name__ == "__main__":
    uvicorn.run(
        "Py2:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )