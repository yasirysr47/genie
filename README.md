# genie

Generate intelligent and efficacious data from any URL's

-------------
Genie is here to generate data by crawling through public websites and make a textual output
or NLP processed Corpus for any specific use.

-------

Genie has a class named **Genie** which takes the URL as the parameter.
Eg:
``` 
object = genie(url)
object.show_summary()
```

Patterns are there to clean data with certain patterns
```
pattern 1 : any string to be replaced can be added after a pipe (|)
pattern 2 : any regex inside parenthesis
```

modes are to say what kind of cleaning to be done.
```
modes available are:
"p" : means take pattern 1 and do simple substring substitution
"r" : means take pattern 2 and do regex substring substitution
```

The features are as follows:

* **get_data**:
  >returns entire data from the article/url provided

    
* **show_summary**:
  >returns the summary of the article in the url


* **get_keywords**:
  >returns the top keywords present in the article


* **get_video_links**:
  >returns all the video links in the article

    
* **get_authors**:
  >returns the authors name in the article


* **get_title**:
  >returns title of the article


* **get_publish_date**:
  >returns publish date of the article


* **get_top_images**:
  >returns top images in the article


* **get_images**:
  >returns all the images in the article


* **get_trending_topics**:
  >returns global trending topics


* **get_trending_urls**:
  >returns global trending news urls irrespective of the url provided
