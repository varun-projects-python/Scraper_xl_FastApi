from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import re
import os

# FK_base_url = 'https://www.flipkart.com/product/p/itme?pid='
key = os.environ.get('abstractapi_key')
FK_base_url = 'https://scrape.abstractapi.com/v1/?api_key=key&url=https://www.flipkart.com/product/p/itme?pid='
FK_tags = {
    'price_class' : '_30jeq3 _16Jk6d', #div
    'fassured_class' : 'b7864- _2Z07dN', #span
    'min_order_qty' : '_1REMSq _1B0GOL _6aiF2j',#div
    'rating' :'_3LWZlK' , #div
    'count_rating' : '', #span
    'count_review' : '', #span
    'mrp' : '_3I9_wc _2p6lqe', #div
}
soup = None
def initialise(url):
  global soup
  uclient = uReq(url)
  page = uclient.read()
  uclient.close()
  soup = BeautifulSoup(page, 'html.parser')

# def FK_name(FSN):
#   try:
#     url = f'{FK_base_url}{FSN}'
#     initialise(url)
#     global res
#     for i in soup.find_all('span', {'class': 'B_NuCI'}):
#         txt = i.get_text()
#         res = "".join(re.split("[^a-zA-Z]*", txt))
#     product_name = res
#     return product_name
#   except Exception as e:
#     return {'Exception' : f'{str(e)}',}


def FK_name(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    name_tag = soup.find('span', {'class': 'B_NuCI'})
    product_name = name_tag.get_text()
    return product_name
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_seller_name(soup):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    global res
    for i in soup.find_all('div', {'id': 'sellerName'}):
        txt = i.get_text()
        res = "".join(re.split("[^a-zA-Z]*", txt))
    seller_name = res
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_price(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    price_tag = soup.find('div', {'class': FK_tags['price_class']})
    price = price_tag.get_text() if price_tag else "Price not found"
    return price
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_mrp(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    mrp_tag = soup.find('div', class_=FK_tags.get('mrp'))
    mrp = mrp_tag.get_text().strip() if mrp_tag else "MRP not Found"
    return mrp
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_rating(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    rating_tag = soup.find('div', class_=FK_tags.get('rating'))
    rating = rating_tag.get_text().strip() if rating_tag else "Rating Not Found"
    return rating
  except Exception as e:
    return {'Exception' : f'{str(e)}',}

def FK_count_rating(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    rating_span = soup.find('span', class_='_2_R_DZ')
    rating_count =  rating_span.get_text().strip().split('&')[0].strip() if rating_span else "Ratings not found"
    return rating_count
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_count_review(FSN):
  try:
    global review_count
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    review_span = soup.find('span', class_='_2_R_DZ')
    if review_span:
              reviews_text = review_span.get_text().strip()
              reviews_list = reviews_text.split('&')
              review_count = reviews_list[1].strip() if len(reviews_list) > 1 else "No reviews available"
    return review_count
  except Exception as e:
    return {'Exception' : f'{str(e)}',}


def FK_min_odr_qty(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    min_order_qty_tag = soup.find('div', {'class': FK_tags['min_order_qty']})
    min_order_qty = min_order_qty_tag.get_text().strip().replace("Minimum Order Quantity:", '') if min_order_qty_tag else False
    return min_order_qty
  except Exception as e:
    return {'Exception' : f'{str(e)}',}



def FK_is_fassured(FSN):
  try:
    url = f'{FK_base_url}{FSN}'
    initialise(url)
    fassured_tag = soup.find('span', {'class': 'b7864- _2Z07dN'})
    is_fassured = True if fassured_tag else False
    return is_fassured
  except Exception as e:
    return {'Exception' : f'{str(e)}',}

