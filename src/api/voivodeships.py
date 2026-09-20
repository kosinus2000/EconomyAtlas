from fastapi import APIRouter
from database import SessionLocal
from models.sqlalchemy_models import VoivodeshipORM
from repositories.repository_implementation import PostgresRepository

router = APIRouter()

@router.get("/")
def get_all_voivodeships():
    session = SessionLocal()
    repo = PostgresRepository(session, VoivodeshipORM)
    voivodeships = repo.get_all()
    session.close()
    return voivodeships