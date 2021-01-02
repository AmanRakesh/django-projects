import requests
from bs4 import BeautifulSoup
import random
from .constants import *

#logic
def getImagesAndDownloadLinks(htmlLink):

    dataToBeSent = None
    headersList = getHeaders(htmlLink)
    htmlLink = PEXELS_SEARCH_URL.format(htmlLink)
    print(htmlLink)
    response = requests.get(htmlLink, headers=headersList)
    htmlPage = response.text
    print(htmlPage)
    soup = BeautifulSoup(htmlPage, "html.parser")
    resultsList = soup.find_all('a', {"class": PEXELS_RESULTS_CLASS})
    if resultsList!=None:
        for eachResult in resultsList:
            print(eachResult)

    return resultsList

def getHeaders(searchTerm):
    header={}
    header["authority"] = "www.pexels.com"
    header["method"] = "GET"
    header["path"] = "/search/{}/".format(searchTerm)
    header["scheme"] = "https"
    header["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9," \
    #                    "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    # header["accept-encoding"] = "gzip, deflate, br"
    # header["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
    header["referer"] = getReferrer()
    # header["sec-fetch-dest"] = "document"
    # header["sec-fetch-mode"] = "navigate"
    # header["sec-fetch-site"] = "cross-site"
    # header["sec-fetch-user"] = "?1"
    # header["upgrade-insecure-requests"] = "1"
    header["user-agent"] = getUserAgent()
    return header

def getUserAgent():
    userAgent=[
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN)",
        "Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    ]
    return userAgent[random.randint(0, len(userAgent)-1)]

def getReferrer():
    referrers=[
        "https://search.aol.com/",
        "https://duckduckgo.com/",
        "https://www.google.com/",
        "https://results.excite.com/",
        "https://www.adobe.com/",
        "https://in.search.yahoo.com/",
        "https://www.google.com/",
        "https://www.facebook.com",
        "https://yandex.com",
    ]
    return referrers[random.randint(0, len(referrers)-1)]