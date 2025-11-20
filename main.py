from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from api.routes.user import user_router
from api.routes.news import news_router

app = FastAPI(title="Beshpagir Church")

main_api_router = APIRouter()
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(news_router, prefix="/news", tags=["news"])

app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
