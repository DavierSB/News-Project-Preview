import newspaper
import nltk
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def process_article(url):
    #try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()
        article.summary_from_sumy = get_summary(article.text)
        article.entities = extract_entities(article.text)
        article.suggestions = get_suggestions(article.text)
        return article
    #except:
    #    print("Exception")
    #    return None

def get_summary(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=5)
    return '. '.join([str(sentence) for sentence in summary])

def extract_entities(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    conjunto = set()
    for entitie in doc.ents:
        if entitie.label_ in ['PERSON', 'NORP', 'ORG', 'GPE', 'LOC']:
            conjunto.add(entitie.text + " : " + entitie.label_)
    return list(conjunto)

def get_suggestions(text):
    return None

#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')