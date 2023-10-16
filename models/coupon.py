from pydantic import BaseModel


class Coupon(BaseModel):
    id: int
    month: str
    coupon_no: str

