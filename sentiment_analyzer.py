import pandas as pd
import nltk

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

analyzer = SentimentIntensityAnalyzer()

df = pd.read_csv('temp/reviews.csv')


def preprocess_text(text):
    tokens = word_tokenize(text.lower())

    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = ' '.join(lemmatized_tokens)
    return processed_text


df['Token'] = df['Description'].apply(preprocess_text)
df['Score'] = df['Token'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
df.drop(columns=['Token'], inplace=True)
df.to_csv('temp/reviews.csv', index=False)
