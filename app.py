# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:00:37 2020

@author: AA
"""

# import packages
import streamlit as st 
import os
from textblob import TextBlob 
import spacy
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
nltk.download('punkt')


# Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

def main():
    """NLP App with Streamlit"""
    
    from PIL import Image
    logo = Image.open('ArcadisLogo.jpg')
    logo = logo.resize((300,90))
    
    st.sidebar.image(logo)
    st.sidebar.title("Text Summarizer")
    st.sidebar.subheader("Natural Language Processing On the Go..")
    
    # Summarization
    st.subheader("Summarize Your Text")
    message = st.text_area('Input your sentence here:') 
    summary_options = st.selectbox("Choose Summarizer",['summy','gensim'])
    
    if st.button("Summarize"):
        if summary_options == 'summy':
            st.text("Using Sumy Summarizer")
            summary_result = sumy_summarizer(message)
        elif summary_options == 'gensim':
            st.text("Using Gensim Summarizer ..")
            summary_result = summarize(message)
        else:
            st.warning("Using Default Summarizer")
            st.text("Using Gensim Summarizer ..")
            summary_result = summarize(message)
        
        st.success(summary_result)
    
    st.sidebar.subheader(" ")
    st.sidebar.subheader(" ")
    st.sidebar.subheader("About the App")
    #st.sidebar.text("Mini Hackathon Prototype")
    st.sidebar.info("This prototype was build as part of the Mini Hackathon. This is an initiative from Group 02 - Afreen Aman")
    
    #st.sidebar.subheader("By")
    #st.sidebar.text("Afreen Aman")

if __name__ == '__main__':
	main()
