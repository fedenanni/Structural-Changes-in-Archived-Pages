"""
Super simple - make it better doing something smarter

"""


import urllib, difflib
from bs4 import BeautifulSoup


def get_tree(url):
    
    urls_to_try = [url]
    
    for url in urls_to_try:
    
        html = urllib.urlopen(url).read().decode("utf-8")

        soup= BeautifulSoup(html)
        
        if "Got an HTTP 302 response at crawl time" in soup.text:            
            for a in soup.findAll('a'):
                if 'Impatient' in a.text:
                    urls_to_try.append("https://web.archive.org" + a['href'])
        else:
            pretty_soup = BeautifulSoup(html).prettify().split("\n")

            DOM_Tree = []

            for element in pretty_soup:
                if "<" in element and ">" in element:
                    DOM_Tree.append(element)

            return url, DOM_Tree
            break

previous = ""
for year in range(1997, 2016):
    
    url = "https://web.archive.org/web/"+ str(year)+ "0901014004/http://www.nytimes.com/"

    final_url, DOM = get_tree(url)
    
    sm=difflib.SequenceMatcher(None,DOM,previous)
    print year, sm.ratio(), final_url
    previous = DOM
    
    
print "done."