import newspaper

def process_article(url):
    #try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()
        article.entities = extract_entities(article.text)
        article.suggestions = get_suggestions(article.text)
        return article
    #except:
    #    print("Exception")
    #    return None
    
def extract_entities(text):
    return None

def get_suggestions(text):
    return None