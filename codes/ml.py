import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

nltk.download('stopwords')


data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv", sep="\t", header=None)
data.columns = ['label', 'text']

# Conversão para binário
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Função de limpeza
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # remove pontuações e números
    words = text.split()
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    cleaned = [stemmer.stem(word) for word in words if word not in stop_words]
    return ' '.join(cleaned)

data['clean_text'] = data['text'].apply(clean_text)

# Separação de treino/teste
X_train, X_test, y_train, y_test = train_test_split(
    data['clean_text'], data['label'], test_size=0.2, random_state=42
)

# Pipeline: TF-IDF + RandomForest
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=1000)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Avaliação
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Ham', 'Spam'],
            yticklabels=['Ham', 'Spam'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

# Importância das features
model = pipeline.named_steps['rf']
tfidf = pipeline.named_steps['tfidf']
feature_names = tfidf.get_feature_names_out()
importances = model.feature_importances_
indices = np.argsort(importances)[-20:]  # top 20 palavras

plt.figure(figsize=(10, 6))
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.title('🔍 Principais palavras que influenciam o modelo')
plt.xlabel('Importância')
plt.show()
