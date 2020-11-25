import random
import string
import warnings
import numpy as np
import newspaper as paper
from newspaper import Article
from newspaper import news_pool
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')


class genie():
    def __init__(self, url):
        self.init_article(url)
        # TODO: include multi thread or url as a list option
        # init_article_mt(url_list)

    def init_article(self, url):
        # single Threaded article extraction
        self.article = paper.Article(url)
        self.article.download()
        self.article.parse()
        self.article.nlp()

        self.corpus = self.article.text
        self.summary = self.article.summary

    def init_article_mt(self, url_list):
        # multi threaded article extraction
        #TODO
        pass
    
    def get_data(self):
        # print entire data from the article
        #TODO: clean data
        return self.corpus
    
    def show_summary(self):
        # show the summary of the article in the url
        #TODO: clean summary
        return self.summary

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


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Chicken_soup'
    data = genie(url)
    print(data.show_summary())





    



