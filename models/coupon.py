from typing import Annotated
from pydantic import BaseModel


class Coupon(BaseModel):
    coupon_no: str

