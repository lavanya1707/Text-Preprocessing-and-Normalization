import streamlit as st
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK stopwords data (if not already downloaded)
nltk.download('stopwords')

# Function for text normalization
def normalize_text(input_text):
    # Convert text to lowercase
    lower_text = input_text.lower()

    # Remove numbers
    no_numbers_text = re.sub(r'\d+', '', lower_text)

    # Remove punctuation (except spaces)
    no_punctuation_text = re.sub(r'[^\w\s]', '', no_numbers_text)

    # Tokenize text
    tokens = nltk.word_tokenize(no_punctuation_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in tokens if word not in stop_words]

    # Stem words
    stemmer = PorterStemmer()
    stemmed_text = [stemmer.stem(word) for word in filtered_text]

    # Reconstruct normalized text
    normalized_text = ' '.join(stemmed_text)

    return normalized_text

# Streamlit app title
st.title('Text Normalization and Preprocessing')

# Input text area for user input
input_text = st.text_area('Enter or paste your text:', '')

# Button to trigger text normalization
if st.button('Normalize Text'):
    if input_text:
        st.subheader('Normalized Text:')
        normalized_text = normalize_text(input_text)
        st.write(normalized_text)
    else:
        st.warning('Please enter text for normalization.')
