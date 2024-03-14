from utils import get_data_directory
from gensim import corpora, models, similarities
from typing import List, Tuple
import spacy

nlp = spacy.load("en_core_web_sm")

def pre_process(documents : List[str]):
    doc_term_matrix, dictionary = prepare_corpus(documents)
    model = build_model(doc_term_matrix, dictionary)
    build_similarity_matrix(model, doc_term_matrix)

def build_model(doc_term_matrix : List[Tuple[int,int]], dictionary : corpora.Dictionary,number_topics = 200) -> models.LsiModel:
    model = models.LsiModel(doc_term_matrix, num_topics=number_topics, id2word=dictionary)
    model.save(get_data_directory() + "model")
    return model

def prepare_corpus(documents : List[str]) -> Tuple[List[Tuple[int,int]], corpora.Dictionary]:
    documents = [clean_document(doc) for doc in documents]
    dictionary = corpora.Dictionary(documents)
    dictionary.save(get_data_directory() + "dictionary")
    doc_term_matrix = [dictionary.doc2bow(doc) for doc in documents]
    return doc_term_matrix, dictionary

def clean_document(document : str) -> List[List[str]]:
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    document = nlp(document)
    return [token.lemma_ for token in document if 
                ((token.is_alpha) and (token.text not in stopwords))]

def build_similarity_matrix(model : models.LsiModel, doc_term_matrix : List[Tuple[int,int]]) -> similarities.MatrixSimilarity:
    sim_matrix = similarities.MatrixSimilarity(model[doc_term_matrix])
    sim_matrix.save(get_data_directory() + "sim_matrix")
    return sim_matrix