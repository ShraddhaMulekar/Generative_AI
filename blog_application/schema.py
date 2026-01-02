from pydantic import BaseModel

# Schema for post request body
class BlogCreation(BaseModel):
    title: str
    content: str

# Schema for response model
class BlogResponseSchema(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True