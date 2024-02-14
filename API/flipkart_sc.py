

from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import re

FK_base_url = 'https://www.flipkart.com/product/p/itme?pid='
FK_tags = {
    'price_class' : '_30jeq3 _16Jk6d', #div
    'fassured_class' : 'b7864- _2Z07dN', #span
    'min_order_qty' : '_1REMSq _1B0GOL _6aiF2j',#div
    'rating' :'_3LWZlK' , #div
    'count_rating' : '', #span
    'count_review' : '', #span
    'mrp' : '_3I9_wc _2p6lqe', #div
}

def FK_result_maker(FSN):
    global res, soup, review_count
    try :
        url = f'{FK_base_url}{FSN}'
        uclient = uReq(url)
        page = uclient.read()
        uclient.close()
        soup = BeautifulSoup(page, 'html.parser')

        #name
        for i in soup.find_all('span', {'class': 'B_NuCI'}):
            txt = i.get_text()
            res = "".join(re.split("[^a-zA-Z]*", txt))
        product_name = res

        #seller_name
        for i in soup.find_all('div', {'id': 'sellerName'}):
            txt = i.get_text()
            res = "".join(re.split("[^a-zA-Z]*", txt))
        seller_name = res


        #TAGS
        price_tag = soup.find('div', {'class': FK_tags['price_class']})
        fassured_tag = soup.find('span', {'class': 'b7864- _2Z07dN'})
        min_order_qty_tag = soup.find('div', {'class': FK_tags['min_order_qty']})
        rating_span = soup.find('span', class_='_2_R_DZ')
        review_span = soup.find('span', class_='_2_R_DZ')
        mrp_tag = soup.find('div', class_=FK_tags.get('mrp'))
        rating_tag = soup.find('div', class_=FK_tags.get('rating'))


        #VARIABLES
        price = price_tag.get_text() if price_tag else "Price not found"
        mrp = mrp_tag.get_text().strip() if mrp_tag else "MRP not Found"
        is_fassured = True if fassured_tag else False
        min_order_qty = min_order_qty_tag.get_text().strip().replace("Minimum Order Quantity:", '') if min_order_qty_tag else False
        rating = rating_tag.get_text().strip() if rating_tag else "Rating Not Found"
        rating_count =  rating_span.get_text().strip().split('&')[0].strip() if rating_span else "Ratings not found"
        # review_count
        if review_span:
            reviews_text = review_span.get_text().strip()
            reviews_list = reviews_text.split('&')
            review_count = reviews_list[1].strip() if len(reviews_list) > 1 else "No reviews available"

        return {
            'product_name': product_name,
            'price': price,
            'mrp' : mrp,
            'is_fassured' : is_fassured,
            'min_order_qty': min_order_qty,
            'rating' : rating,
            'rating_count': rating_count,
            'review_count' : review_count
        }
    except Exception as e:
        return {'Exception' : f'{str(e)}',}
