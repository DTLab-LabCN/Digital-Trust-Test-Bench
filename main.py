from fastapi import FastAPI, APIRouter
from app.routers import authentication, users
from config import settings

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    contact=settings.PROJECT_CONTACT,
    # license_info=settings.PROJECT_LICENSE_INFO,
)

api_router = APIRouter()

# routes for authentication (mostly inherited from "FastAPI Users")
api_router.include_router(authentication.router, prefix="/auth")

# routes for user management (mostly inherited from "FastAPI Users")
api_router.include_router(users.router, prefix='/users')

app.include_router(api_router)

# This is to initialize the DB used by our "FastAPI Users" module
@app.on_event("startup")
async def on_startup():
    from app.db import create_db_and_tables
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()