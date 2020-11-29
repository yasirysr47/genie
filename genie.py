import random
import string
import nltk
import warnings
import re, sys, os
import heapq
import urllib.request
import bs4 as bs
import numpy as np
import newspaper as paper
from newspaper import Article
from newspaper import news_pool
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#depended upon scrapy and genie and data_store
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataStore.dir import Dir
import DataStore.src as src

MAX_NUMBER_SUBTITLES = 7
PATH = Dir()
warnings.filterwarnings('ignore')
STOPWORDS = nltk.corpus.stopwords.words('english')


'''
modes available are:
"p" : means take pattern 1 and do simple substring substitution
"r" : means take pattern 2 and do regex substring substitution
'''

class Genie():
    def __init__(self, url='', pattern=None, mode=None):
        #self.init_article(url)
        self.mode = mode
        self.pattern = pattern
        # TODO: include multi thread or url as a list option
        # init_article_mt(url_list)

    def init_article(self, url):
        # single Threaded article extraction
        self.article = paper.Article(url)
        self.article.download()
        self.article.parse()
        self.article.nlp()

        self.corpus = self.article.text.lower()
        self.summary = self.article.summary.lower()
    
    def init_article_mt(self, url_list):
        # multi threaded article extraction
        #TODO
        pass

    def convert_parse_data(self, data):
        parsed_article = data
        [tmp.extract() for tmp in parsed_article.select('.hidden')]
        paragraphs = parsed_article.find_all(src.parse_field)
        article_text = ""
        for para in paragraphs:
            txt = para.text.strip().lower()
            if any(word in txt for word in src.blacklist_words):
                continue
            if para.name == 'h1':
                article_text = "{}\n<h1>{}".format(article_text, txt)
            elif para.name == 'h2':
                article_text = "{}\n<h2>{}".format(article_text, txt)
            elif para.name == 'h3':
                article_text = "{}\n<h3>{}".format(article_text, txt)
            elif para.name == 'li':
                article_text = "{}\n>>>{}".format(article_text, txt)
            elif para.name == 'p':
                article_text = "{}\n<p>{}".format(article_text, txt)
        
        return article_text

    def get_data(self, data=''):
        return self.parsed_article
    
    def clean_data(self, data, pattern='', mode=''):
        if mode == 'r':
            data =  re.sub(pattern, '', data)
        elif mode == 'p':
            data = data.replace(pattern, '')
        elif mode == 's':
            data = re.sub(r'[^a-zA-Z0-9]', ' ', data)
            data = re.sub(r'\s+', ' ', data)
        return data

    def get_article_data(self):
        # print entire data from the article
        data = self.corpus
        if self.mode:
            data = self.clean_data(data, self.pattern, self.mode)
        return data
    
    def show_summary(self):
        # show the summary of the article in the url
        summary = self.summary
        if self.mode:
            summary = self.clean_data(summary, self.pattern, self.mode)
            
        return summary

    def generate_summary(self, paragraph):
        word_freq = {}
        sent_scores = {}
        org_data = nltk.sent_tokenize(paragraph.lower())
        alt_data = self.clean_data(paragraph.lower(), pattern='', mode='s')
        for word in nltk.word_tokenize(alt_data):
            if word in STOPWORDS:
                continue
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

        max_freq = max(word_freq.values())
        for word in word_freq.keys():
            word_freq[word] = float(word_freq[word]/max_freq)
        for sent in org_data:
            for word in nltk.word_tokenize(sent):
                if sent not in sent_scores:
                    sent_scores[sent] = word_freq.get(word, 0)
                else:
                    sent_scores[sent] += word_freq.get(word, 0)
        summary_sent = heapq.nlargest(5, sent_scores, key=sent_scores.get)
        summary = ' '.join(summary_sent)

        return summary

    def get_keywords(self):
        # top keywords present in the article
        #TODO: clean keywords
        return self.article.keywords

    def get_video_links(self):
        # all the video links in the article
        #TODO: clean links
        return self.article.movies
    
    def get_authors(self):
        # get the authors name in the article
        #TODO: clean authors
        return self.article.authors

    def get_title(self):
        # get title of the article
        #TODO: clean title
        return self.article.title

    def get_publish_date(self):
        # get publish date of the article
        return self.article.publish_date

    def get_top_images(self):
        # get top images in the article
        #TODO: clean image urls
        return self.article.top_image

    def get_images(self):
        # get all the images in the article
        #TODO: clean image urls
        return self.article.images

    def get_trending_topics(self):
        # get global trending topics
        # irrespective of the url
        return paper.hot()

    def get_trending_urls(self):
        # get global trending news urls
        # only returns news related urls
        # irrespective of the url
        return paper.popular_urls()

    def save_data(self, data, file):
        with open(file, "w+") as fp:
            fp.write(data)


if __name__ == "__main__":
    url = 'https://www.mayoclinic.org/diseases-conditions/chickenpox/symptoms-causes/syc-20351282'
    #url = 'https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605'
    genie = Genie(url, pattern=src.clean_data_pattern[2], mode='r')
    data = genie.get_data()
    #genie.save_data(data, "common-cold.txt")
    #summ = genie.generate_summary(data)
    print("=======================")
    #print(summ)
    #print(data)
    print("===== my summary ====")
    #db = genie.get_sub_heading_data(data)
    #db = {}
    for k,v in db.items():
        print(k)
        print('---')
        print(v)
        print("=====+++++=====")
    #print(genie.show_summary())
    
    #sent_list = nltk.sent_tokenize(data.lower())
    #print(sent_list)
    titles = ["overview", "symptoms", "when to see a doctor", "causes", "risk factors", "complications", "prevention", "Who's at risk?"]
    # print("==========")
    # for each in sent_list:
    #     new = each.split('\n\n')
    #     #print(new)
    #     for e in new:
    #         if e in titles:
    #             print(e)





    



