#crawlorig.oy
#creates a webcrawler that makes a list of links from a url passed to it?

import sys
import re
import urllib.request
import urllib.parse
tocrawl = set([sys.argv[1]])
crawled = set([])
keywordregex = re.compile('<meta\sname=["\']keywords["\']\scontent=["\'](.*?)["\']\s/>')
linkregex = re.compile('<a\s*href=[\'|"](.*?)[\'"].*?>')

while len(crawled)<2:
    try:
        crawling = tocrawl.pop()
        print (crawling)
    except KeyError:
        raise StopIteration
    url = urlparse.urlparse(crawling)
    try:
        response = urllib2.urlopen(crawling)
    except:
        continue
    msg = response.read()
    startPos = msg.find('<title>')
    if startPos != -1:
        endPos = msg.find('</title>', startPos+7)
        if endPos != -1:
            title = msg[startPos+7:endPos]
            print (title)
    keywordlist = keywordregex.findall(msg)
    if len(keywordlist) > 0:
        keywordlist = keywordlist[0]
        keywordlist = keywordlist.split(", ")
        print ("keywordlist=", keywordlist)
    links = linkregex.findall(msg)
    crawled.add(crawling)
    for link in (links.pop(0) for _ in xrange(len(links))):
        if link.startswith('/'):
            link = 'http://' + url[1] + link
        elif link.startswith('#'):
            link = 'http://' + url[1] + url[2] + link
        elif not link.startswith('http'):
            link = 'http://' + url[1] + '/' + link
    if link not in crawled:
        tocrawl.add(link)
