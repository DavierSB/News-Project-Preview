import parse_article

url= 'https://www.nytimes.com/2024/02/05/us/politics/faa-boeing-737-max-9.html'
url= 'https://www.granma.cu/cultura/2024-02-05/la-pelota-en-casa-05-02-2024-19-02-38'
url= 'https://www.nytimes.com/2024/02/03/us/politics/us-strikes-iran-militias-israel.html'
url= 'https://www.washingtonpost.com/business/2024/02/02/school-bus-era-ends/'
url= 'https://www.latimes.com/opinion/newsletter/2024-02-03/opinion-newsletter-rain-in-los-angeles-flood-climate-change-opinion'
article = parse_article.process_article(url)

print("Title")
print(article.title)
print("Authors")
print(article.authors)
print("Keywords")
print(article.keywords)
print("Summary")
print(article.summary)
print("Text")
print(article.text)

with open('article.txt', 'w') as f_out:
    f_out.write(article.text)