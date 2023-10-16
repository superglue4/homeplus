from fastapi import FastAPI
from router.coupon import coupon_router

app = FastAPI()

@app.get("/")

async def welcome() -> dict:
    return {
        "message" : "강가람 안녕!"
    }

app.include_router(coupon_router)



# if __name__ == '__main__':
#     print_hi('PyCharm')

