"""
TODO
"""

import uvicorn

from fastapi import FastAPI, status, HTTPException

from src.routes.generate import router as generate_router

app = FastAPI(
    title="Narrify | Generation API",
    description="API for generating stories and dialogues",
    version="1.0.0"
)

app.include_router(generate_router, prefix="/generate")


@app.get("/", status_code=status.HTTP_200_OK)
async def hello_world():
    """
    TODO xd
    """

    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
