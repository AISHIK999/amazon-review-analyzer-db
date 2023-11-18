import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def clean_reviews():
    asin = os.getenv('PRODUCT_ID')
    df = pd.read_csv('temp/reviews.csv')
    df = df.drop(['ReviewerURL', 'VerifiedPurchase', 'HelpfulCount'], axis=1)
    df['Title'] = df['Title'].replace(r'^\d\.0 out of 5 stars\n', '', regex=True)
    df.insert(0, 'ASIN', asin)
    df.to_csv('temp/reviews.csv', index=False)


if __name__ == "__main__":
    clean_reviews()
