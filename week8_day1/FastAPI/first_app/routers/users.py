from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.get("/{username}")
def get_user(username:str):
    return {"message": f"User profile for, {username}!"}

@router.get("/{username}/post/{post_id}")
def get_post(username:str, post_id:int):
    return {"message": f"Post {post_id} for user {username}!"}
