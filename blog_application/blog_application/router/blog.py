from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from db.models import Blog

from db.database import get_db
from db import models
from schema import BlogCreation, BlogResponseSchema as BlogDisplay, BlogUpdate


router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

@router.get("/", response_model=List[BlogDisplay])
def get_all_blogs(db:Session=Depends(get_db)):
    return db.query(models.Blog).all()

@router.post("/", response_model=BlogDisplay)
def create_blog(request:BlogCreation, db:Session=Depends(get_db)):
    # {title, content} = request
    new_blog = Blog(title=request.title, content=request.content)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# //patch req
@router.patch("/{id}", response_model=BlogDisplay)
def patch_blog(id:int, blog_update:BlogUpdate, db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    if blog_update.title is not None:
        blog.title = blog_update.title
    
    if blog_update.content is not None:
        blog.content = blog_update.content

    db.commit()
    db.refresh(blog)
    return blog