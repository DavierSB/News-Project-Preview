import streamlit as st
import article_processer

st.write("Hola!")
st.write("En esta web app, nos das el link de una noticia y te mostraremos todo lo que quieras saber sobre ella")

url = st.text_input('Enter a news url')

article = article_processer.process_article(url)

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
    st.write(article.suggestions)