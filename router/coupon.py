from fastapi import APIRouter

coupon_router = APIRouter()

coupon_list = []


@coupon_router.post("/coupon")
async def post_coupon(coupon: dict) -> dict:
    coupon_list.append(coupon)
    return {
        "message": "쿠폰 추가 완료!"
    }


@coupon_router.get("/coupon")
async def get_coupon() -> dict:
    return {
        "message": coupon_list
    }
