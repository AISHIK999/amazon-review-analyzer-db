import os

from scrape_amazon import get_reviews
from dotenv import load_dotenv

load_dotenv()


def fetch_reviews():
    reviews = get_reviews(domain=os.getenv('DOMAIN'), product_id=os.getenv("PRODUCT_ID"))

    if not os.path.exists('temp'):
        os.makedirs('temp')
    reviews.to_csv('temp/reviews.csv', index=False)
    print(f"Reviews saved to temp/reviews.csv")


if __name__ == "__main__":
    fetch_reviews()
