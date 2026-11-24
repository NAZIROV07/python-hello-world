from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.db import Base, engine
from app.api import books, categories


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    engine.dispose()


app = FastAPI(
    title="Book Store API",
    description="API книжного магазина на Python и PostgreSQL",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}