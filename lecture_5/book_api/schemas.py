from pydantic import BaseModel
from typing import Optional 

class BookBase(BaseModel):
    title: str
    author: str
    year: Optional[int] = None 

class Book(BookBase):
    id: int
    class Config:
        from_attributes = True 