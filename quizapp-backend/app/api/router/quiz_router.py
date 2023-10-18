from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz App"]
)

@router.get("/home")
async def home():
    return {"data":"This is home"}