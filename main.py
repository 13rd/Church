from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRouter
from sqladmin import Admin

from api.admin import register_admin_views
from db.session import engine
from api.routes.user import user_router
from api.routes.news import news_router
from api.routes.textblock import textblock_router

app = FastAPI(title="Beshpagir Church")

admin = Admin(app, engine=engine,)

main_api_router = APIRouter()
main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(news_router)
main_api_router.include_router(textblock_router)

app.include_router(main_api_router)

register_admin_views(admin)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
