from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    size: str
    price: float
    amount: float


class DegreeType(Enum):
    junior = 'junior'
    middle = 'middle'
    senior = 'senior'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    name: str
    role: str
    degree: Optional[List[Degree]]
