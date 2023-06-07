import streamlit as st
import pickle
import pandas as pd
import nltk
nltk.download('punkt')
import re,string
import requests

st.title('Romanized Nepali Text Sentiment Analysis')

gnb_model2= pickle.load(open('gnb2_model.pkl','rb'))
gnb_model = pickle.load(open('gnb_model.pkl','rb'))

mnb_model2= pickle.load(open('mnb2_model.pkl','rb'))
mnb_model = pickle.load(open('mnb_model.pkl','rb'))

bnb_model2= pickle.load(open('bnb2_model.pkl','rb'))
bnb_model = pickle.load(open('bnb_model.pkl','rb'))


tfidf = pickle.load(open('tfidf_vectorizer.pkl','rb'))
bow = pickle.load(open('bow_vectorizer.pkl' ,'rb'))
from preprocessing import clean_sent

def run_sentiment_analysis(txt):
    preprocessed_inputs = clean_sent(txt)
    preprocessed_inputs = [preprocessed_inputs]

    bow_features = bow.transform(preprocessed_inputs)
    bow_features1 = bow.transform(preprocessed_inputs).toarray()

    tfidf_features = tfidf.transform(preprocessed_inputs)
    tfidf_features1 = tfidf.transform(preprocessed_inputs).toarray()

    result1t = gnb_model.predict(tfidf_features1)
    result2t = mnb_model.predict(tfidf_features)
    result3t = bnb_model.predict(tfidf_features)


    result1b = gnb_model2.predict(bow_features1)
    result2b = mnb_model2.predict(bow_features)
    result3b = bnb_model2.predict(bow_features)

    total_result = sum([result1t[0],result2t[0],result3t[0],result1b[0],result2b[0],result3b[0]])

    majority = 1 if total_result >= 3 else 0

    return majority
txt = st.text_area('Enter text here...')
if st.button('Predict'):
    result = run_sentiment_analysis(txt)
    if result == 1:
        st.write('Sentiment : ' , 'Positive')
    else:
        st.write('Sentiment : ' ,'Negative')