from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import MetaData, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, create_engine
from config import DB_HOST, DB_PORT, DB_USER, DB_NAME, DB_PASS

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)
Base = declarative_base()


class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Roles")
