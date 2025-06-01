from fastapi import FastAPI
from app.controller.item_controller import router as item_router
from app.config.app_config import appConfig

app = FastAPI(title=appConfig.appName)

app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
