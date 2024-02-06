import newspaper

def process_article(url):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article
    except:
        return None