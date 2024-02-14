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



app = FastAPI()


@app.get("/")
def read_root():
    return {
        "api_name": "flipkart-product-tracket(pricebefore)",
        "repository": "https://github.com/dvishal485/flipkart-product-stock",
        "author": "donottell.com",
        "description": "API to scrapes product details from Flipkart",
        "usage": "https://flipkart-product-stock.herokuapp.com/product?link={product_link}",
        "example": "https://flipkart-product-stock.herokuapp.com/product?link=https://dl.flipkart.com/s/WaqrsvNNNN"
    }


@app.get("/")
def login():
    pass

# http://xyz.render.com/flipkart?id=

@app.get("/flipkart/{FSN}")
async def read_item(FSN: str):
    res = FK_result_maker(FSN)
    return json.loads(json.dumps(res))


# http://xyz.render.com/amazon?id=
# @app.get("/amazon/{ASIN}")
# async def read_item(ASIN: str):
#     res = AMZ_result_maker(ASIN)
#     return json.loads(json.dumps(res))
