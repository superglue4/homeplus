import os.path
import shutil
from typing import Annotated
from fastapi import APIRouter, Request, Depends, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from starlette.templating import _TemplateResponse

from models.coupon import Coupon
coupon_router = APIRouter()

coupon_list = []

templates = Jinja2Templates(directory="templates/")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "images/")
IMG_URL = os.path.join("http://127.0.0.1:8000/","images/")



@coupon_router.post("/coupon")
async def post_coupon(coupon_no: Annotated[str, Form()], coupon_exp: Annotated[str, Form()], coupon_img: UploadFile):

    local_path = os.path.join(IMG_DIR, coupon_img.filename)
    #파일 저장
    with open(local_path, "wb") as buffer:
        shutil.copyfileobj(coupon_img.file, buffer)
    #변수 저장
    coupon_list.append({
        "coupon_no": coupon_no,
        "coupon_exp": coupon_exp,
        "coupon_img": coupon_img.filename,
        "coupon_url": f"{IMG_URL}{coupon_img.filename}",
    })
    return {"coupon_list": coupon_list}


@coupon_router.get("/coupon")
async def get_coupon(request:Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {
        "request": request,
        "coupon_list": coupon_list

    })


@coupon_router.get("/images/{filename}")
async def get_image(filename: str):
    return FileResponse(f"{IMG_DIR}/{filename}")
