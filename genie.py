import random
import string
import warnings
import re
import numpy as np
import newspaper as paper
from newspaper import Article
from newspaper import news_pool
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings('ignore')


'''
pattern 1 : any string to be replaced can be added after a pipe (|)
pattern 2 : any regex inside ()
'''
clean_data_pattern = {
    1 : '(click here|xxxx|yyy)',
    2: '(\[\s*[\s\w]+\s*\])'
}

'''
modes available are:
"p" : means take pattern 1 and do simple substring substitution
"r" : means take pattern 2 and do regex substring substitution
'''

class Genie():
    def __init__(self, url, pattern=None, mode=None):
        self.init_article(url)
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

        self.corpus = self.article.text
        self.summary = self.article.summary

    def init_article_mt(self, url_list):
        # multi threaded article extraction
        #TODO
        pass
    
    def clean_data(self, data, pattern, mode):
        if mode == 'r':
            data =  re.sub(pattern, '', data)
        elif mode == 'p':
            data = data.replace(pattern, '')

        return data

    def get_data(self):
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
    url = 'https://en.wikipedia.org/wiki/Chicken_soup'
    genie = Genie(url, pattern=clean_data_pattern[2], mode='r')
    data = genie.get_data()
    genie.save_data(data, "soup.txt")
    print(genie.show_summary())





    



