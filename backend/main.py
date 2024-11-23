from fastapi import FastAPI

from controllers import chat_history_controller

app = FastAPI()

app.include_router(chat_history_controller.chat_history_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
