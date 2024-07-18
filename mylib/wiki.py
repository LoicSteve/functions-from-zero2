import wikipedia as wiki
from yake import KeywordExtractor


# build a fucntion to return the summary of a wikipedia page
def get_wiki_summary(page_name):
    return wiki.summary(page_name)


# build a function search wikipedia pages for a match
def search_wiki(query):
    return wiki.search(query)


# build a fucntion to return the wikipedia page
def get_wiki_page(page_name):
    return wiki.page(page_name)


# return the keywords from a wikipedia page
def get_keywords(page_name):
    kw_extractor = KeywordExtractor()
    keywords = kw_extractor.extract_keywords(get_wiki_summary(page_name))
    # return a dictionnary of the top 10 keywords
    return {keyword: score for keyword, score in keywords[:10]}
