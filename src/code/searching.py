from typing import List
import json
from gensim import corpora, models, similarities
from utils import get_data_directory
from pre_processing import clean_document
from loading_no_processing_news import New
from typing import List, Tuple 

class Corpus:
    def __init__(self,news : List[New], model : models.LsiModel, dictionary : corpora.Dictionary, sim_matrix : List[Tuple[int,int]]):
        self.news = news
        self.model = model
        self.dictionary = dictionary
        self.sim_matrix = sim_matrix
def load_all_dates() -> Corpus :
    sim_matrix = similarities.MatrixSimilarity.load(get_data_directory() + "sim_matrix")
    dictionary = corpora.Dictionary.load(get_data_directory() + "dictionary")
    model = models.LsiModel.load(get_data_directory() + "model")
    news = load_news()
    return Corpus(news, model, dictionary, sim_matrix)

def search(query, corpus : Corpus) -> List[New]:
    query = clean_document(query)
    query_bow = corpus.dictionary.doc2bow(query)
    sims = corpus.sim_matrix[corpus.model[query_bow]]
    searched = []
    for index in sorted(enumerate(sims), key=lambda item: -item[1])[:3]:
        searched.append(corpus.news[index[0]])
    return searched

def load_news() -> List[New]:
    with open(get_data_directory() + 'news.json', 'r') as in_f:
        news_dicts = json.load(in_f)
    return [New(title = new["title"], published_date=new["published_date"], link = new["link"]) for new in news_dicts]




