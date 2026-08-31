from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase

from src.database import Base


class VoivodeshipORM(Base):
    __tablename__ = 'voivodeship'

    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=True,nullable=False)
    area = Column(Numeric(15,2))
    population = Column(Integer)
    pkb = Column(Numeric(15,2))


class PowiatORM(Base):
    __tablename__ = 'powiat'
    __table_args__ = (
        UniqueConstraint('region_id','name'),
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(50),unique=False,nullable=False)
    area = Column(Numeric(15,2))
    pkb = Column(Numeric(15,2))
    population = Column(Integer)
    region_id = Column(Integer,ForeignKey('voivodeship.id'),nullable=False)

class GminaORM(Base):
    __tablename__ = 'gmina'
    __table_args__ = (
        UniqueConstraint('powiat_id','name'),
    )
    id = Column(Integer, primary_key=True)
    area_type = Column(String(30))
    latitude = Column(Numeric(9,6))
    longitude = Column(Numeric(9,6))
    name = Column(String(50),unique=False,nullable=False)
    area = Column(Numeric(15,2))
    pkb = Column(Numeric(15,2))
    population = Column(Integer)
    powiat_id = Column(Integer,ForeignKey('powiat.id'),nullable=False)