from fastapi import APIRouter

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

router.get("/")
def get_all_blogs():
    return {"message": "fetch All Blogs"}