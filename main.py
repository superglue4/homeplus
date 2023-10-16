from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def welcome() -> dict:
    return {
        "message" : "안녕 !"
    }





# if __name__ == '__main__':
#     print_hi('PyCharm')

