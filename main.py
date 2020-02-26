from random import randint

import uvicorn
from fastapi import FastAPI

app = FastAPI()

from aux import A
from utils import process_func, op_stop_process


@process_func("A")
def fun1(num):
    a = A(num)
    a.run()


@app.get("/test", tags=["test"])
async def test():
    return randint(1, 10)


@app.post("/test/{e}", tags=["test"])
def test(e: int):
    fun1(e)


@app.delete("/test/{e}", tags=["test"])
def test(e: int):
    op_stop_process(e, "A")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8020)
