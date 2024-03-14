from utils import get_data_directory
import json
from datasets import load_dataset
from typing import List
class New:
    def __init__(self, title, published_date, link):
        self.title = title
        self.published_date = published_date
        self.link = link

def load_news_from_huggins() -> List[str]:
    dataset = load_dataset("RealTimeData/bbc_news_alltime",'2024-02')
    news = []
    news_content = []
    for new in dataset['train']:
        news.append(New(new['title'],new['published_date'],new['link']))
        news_content.append(new['content'])
    save_news(news)
    return news_content

def save_news(news : List[New]):
    news_dicts = [new.__dict__ for new in news]
    with open(get_data_directory() + 'news.json', 'w') as out_f:
        json.dump(news_dicts, out_f)

load_news_from_huggins()