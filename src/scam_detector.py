import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import mean_absolute_error


# Imported, changed column names, and changed labels to 1s and 0s
df = pd.read_csv("email-scam-detector\data\spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'text'] # "spam_ham_dataset.csv" already has columns labeled correctly
df['label'] = df['label'].map({'ham' : 0, 'spam' : 1})


# Using NLTK to tokenize and clean out common words
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(df['text'])
y = df['label']


# Training the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
model = RandomForestClassifier(n_estimators=100, random_state=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print(mean_absolute_error(y_test, y_pred))


# Function to classify new email texts
def classify_email(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return "Scam" if prediction == 1 else "Safe"