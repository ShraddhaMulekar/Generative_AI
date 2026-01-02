from pydantic import BaseModel
from typing import Optional

class BlogCreation(BaseModel):
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: str
    content: Optional[str] = None

class BlogDisplay(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True
