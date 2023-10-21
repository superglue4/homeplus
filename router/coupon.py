import os
import shutil
from typing import Annotated
from fastapi import APIRouter, Request, Depends, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from starlette.templating import _TemplateResponse
from models.coupon import Coupon
from database.database import engineconn
from sqlalchemy import insert, update, bindparam

engine = engineconn()
session = engine.sessionmaker()

coupon_router = APIRouter()

coupon_list = []
for row in session.query(Coupon).all():
    coupon_list.append({
        "coupon_no": row.no,
        "coupon_exp": row.exp,
        "coupon_url": row.img
    })

templates = Jinja2Templates(directory="templates/")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "images/")


@coupon_router.post("/coupon")
async def post_coupon(coupon_no: Annotated[str, Form()], coupon_exp: Annotated[str, Form()], coupon_img: UploadFile):
    local_path = os.path.join(IMG_DIR, coupon_img.filename)
    # 파일 저장
    with open(local_path, "wb") as buffer:
        shutil.copyfileobj(coupon_img.file, buffer)
    # 변수 저장
    IMG_URL = os.environ['IMG_URL']
    coupon_list.append({
        "coupon_no": coupon_no,
        "coupon_exp": coupon_exp,
        "coupon_url": f"{IMG_URL}{coupon_img.filename}",
    })
    # db 입력
    print(session.execute(insert(Coupon), [
        {"no": coupon_no, "use": "N", "month": "202310", "exp": coupon_exp, "img": f"/images/{coupon_img.filename}"}
    ]))

    session.commit()

    return {"status": 200}


@coupon_router.put("/coupon/{no}")
async def put_coupon(no: str):
    session.execute(update(Coupon).where(Coupon.no == no).values(use="Y"))
    session.commit()

    return {"status": 200}


@coupon_router.get("/coupon")
async def get_coupon(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {
        "request": request,
        "coupon_list": coupon_list

    })


@coupon_router.get("/images/{filename}")
async def get_image(filename: str):
    return FileResponse(f"{IMG_DIR}/{filename}")
