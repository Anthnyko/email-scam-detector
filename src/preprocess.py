import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')

def get_vectorizer():
    stop_words = stopwords.words('english')
    return TfidfVectorizer(stop_words=stop_words)