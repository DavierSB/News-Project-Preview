import streamlit as st
import pandas as pd
import article_processer
from searching import search, load_all_dates
from typing import List
from loading_no_processing_news import New,  load_news_from_huggins
from pre_processing import pre_process

news_text = load_news_from_huggins()
pre_process(news_text)
corpus = load_all_dates()

st.write("Hola!")
st.write("En esta web app, nos das el link de una noticia y te mostraremos todo lo que quieras saber sobre ella")

url = st.text_input('Enter a news url')

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
    st.write("El titulo es:")
    st.write(article.title)
    st.write("Los autores son:")
    st.write(article.authors)
    st.write("Fue publicado el:")
    st.write(article.publish_date)
    st.write("Resumen:")
    st.write(article.summary)
    st.write("sumy:")
    st.write(article.summary_from_sumy)
    st.write("Entidades presentes:")
    st.write(article.entities)
    st.write("Noticias similares:")
    print_suggestion(article.suggestions)