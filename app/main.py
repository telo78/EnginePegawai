from fastapi import FastAPI
from app.routers import CategoryRoute, LoginRoute
from .models import Model
from .db.database import engine
from .routers import UserRoute, LoginRoute, CategoryRoute, CourseRoute, ProviderRoute
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Model.Base.metadata.create_all(engine)

# App Route


@app.router.get("/")
async def index():
    return {"message": "Playbook v1"}

app.include_router(UserRoute.router)
app.include_router(LoginRoute.router)
app.include_router(CategoryRoute.router)
app.include_router(CourseRoute.router)
app.include_router(ProviderRoute.router)
