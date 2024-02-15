# from typing import Optional
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}



import json
from fastapi import FastAPI
from API.flipkart_sc import FK_result_maker
from API.newfk_sc import *


app = FastAPI()


@app.get("/")
def read_root():
    return {
        '/': 'This is home page'
    }

@app.get("/flipkart/{FSN}")
async def read_item(FSN: str):
    res = FK_result_maker(FSN)
    return json.loads(json.dumps(res))

@app.get("/fk/pname/{FSN}")
async def read_item(FSN: str):
    res = FK_name(FSN)
    return res


@app.get("/fk/sname/{FSN}")
async def read_item(FSN: str):
    res = FK_seller_name(FSN)
    return res


@app.get("/fk/price/{FSN}")
async def read_item(FSN: str):
    res = FK_price(FSN)
    return res


@app.get("/fk/mrp/{FSN}")
async def read_item(FSN: str):
    res = FK_mrp(FSN)
    return res


@app.get("/fk/rating/{FSN}")
async def read_item(FSN: str):
    res = FK_rating(FSN)
    return res


@app.get("/fk/c-rating/{FSN}")
async def FK_count_rating(FSN: str):
    res = FK_count_rating(FSN)
    return res


@app.get("/fk/c-review/{FSN}")
async def FK_count_review(FSN: str):
    res = FK_count_review(FSN)
    return res


@app.get("/fk/pname/{FSN}")
async def read_item(FSN: str):
    res = FK_name(FSN)
    return res


@app.get("/fk/moq/{FSN}")
async def read_item(FSN: str):
    res = FK_min_odr_qty(FSN)
    return res

@app.get("/fk/is-fassured/{FSN}")
async def read_item(FSN: str):
    res = FK_is_fassured(FSN)
    return res
