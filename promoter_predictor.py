import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os


def load_dataset():
    # Ensure path matches your folder structure
    df = pd.read_csv("promoter_dataset.csv") 
    sequences = df["sequence"].str.upper().tolist()
    labels = df["label"].tolist()
    return sequences, labels

def train_and_save_model():
    sequences, labels = load_dataset()
    
    # 1. Initialize and FIT the vectorizer on the whole dataset
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(6, 6), lowercase=False)
    X = vectorizer.fit_transform(sequences).toarray()
    feature_names = vectorizer.get_feature_names_out()
    
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)
    
    model = LogisticRegression(max_iter=1000, class_weight='balanced')
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    print(f"✅ Model trained | Accuracy: {accuracy_score(y_test, preds):.3f}")
    
    # 2. SAVE the feature names so we know the 'vocabulary' for later
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/promoter_model.pkl")
    joblib.dump(feature_names, "models/feature_names.pkl")
    print("✅ Model & features saved.")

def predict_promoter(sequence):
    # 1. Load model and the EXACT vocabulary used in training
    model = joblib.load("models/promoter_model.pkl")
    feature_names = joblib.load("models/feature_names.pkl")
    
    # 2. Use the saved feature_names to build a 'fixed' vectorizer
    # We use 'vocabulary=' to ensure the number of features matches (2873)
    vectorizer = CountVectorizer(analyzer='char', 
                                 ngram_range=(6, 6), 
                                 vocabulary=feature_names, 
                                 lowercase=False)
    
    # 3. Use .transform() NOT .fit_transform()
    X = vectorizer.transform([sequence.upper()]).toarray()
    
    prob = model.predict_proba(X)[0][1]
    
    # Calculate top contributing k-mers
    importance = np.abs(model.coef_[0])
    # Note: we need to handle cases where X might have different indexing 
    # if vocab was different, but using 'vocabulary=' fixed this.
    top_idx = importance.argsort()[-5:][::-1]
    top_kmers = [(feature_names[i], round(importance[i], 3)) for i in top_idx]
    
    return prob, top_kmers