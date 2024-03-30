import streamlit as st
import pandas as pd
import article_processer
from searching import search, load_all_dates
from typing import List
from loading_no_processing_news import New,  load_news_from_huggins
from pre_processing import pre_process


try:
    corpus = load_all_dates()
except:
    news_text = load_news_from_huggins()
    pre_process(news_text)
    corpus = load_all_dates()


st.write("Hola!")
st.write("En esta web app, nos das el link de una noticia y te mostraremos todo lo que quieras saber sobre ella")

url = st.text_input('Enter a news url')

article = None
if url:
    article = article_processer.process_article(url, corpus)

def print_suggestion(suggestions : List[New]):
    titles = []
    dates = []
    links = []
    for new in suggestions:
        titles.append(new.title)
        dates.append(new.published_date)
        links.append(new.link)
    dic = {"Title" : titles, "Published Date": dates, "Link": links}
    df = pd.DataFrame(dic)
    st.table(df)

if article:
    st.markdown("<h3>El título es:</h3>", unsafe_allow_html= True)
    st.write(article.title)
    st.markdown("<h3>Los autores son</h3>", unsafe_allow_html= True)
    for author in article.authors:
        st.write(author)
    st.markdown("<h3>Fue publicado el</h3>", unsafe_allow_html= True)
    st.write(article.publish_date)
    st.markdown("<h3>Resumen</h3>", unsafe_allow_html= True)
    st.write(article.summary)
    st.markdown("<h3>Resumen con sumy</h3>", unsafe_allow_html= True)
    st.write(article.summary_from_sumy)
    st.markdown("<h3>Las entidades que aparecen son</h3>", unsafe_allow_html= True)
    for entity in article.entities:
        st.write(entity)
    st.markdown("<h3>Artículos Similares</h3>", unsafe_allow_html= True)
    print_suggestion(article.suggestions)