import os.path

from fastapi import FastAPI
from router.coupon import coupon_router
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()


@app.get("/")

async def welcome() -> dict:
    return {
        "message": "환영 합니다.!"
    }

app.include_router(coupon_router)



# if __name__ == '__main__':
#     print_hi('PyCharm')

