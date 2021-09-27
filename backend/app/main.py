import uvicorn
from fastapi import FastAPI

from api.endpoints.login import router

app = FastAPI()

app.include_router(router, tags=["LOGIN"])

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
