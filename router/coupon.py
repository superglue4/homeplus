from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

from models.coupon import Coupon
coupon_router = APIRouter()

coupon_list = []

templates = Jinja2Templates(directory="templates/")


@coupon_router.post("/coupon")
async def post_coupon(request: Request, coupon: Coupon) -> _TemplateResponse:
    coupon_list.append(coupon)
    return templates.TemplateResponse("post.html", {
        "request": request,
        "coupon": coupon

    })


@coupon_router.get("/coupon")
async def get_coupon(request:Request) -> _TemplateResponse:
    return templates.TemplateResponse("index.html", {
        "request": request,
        "coupon": coupon_list

    })
