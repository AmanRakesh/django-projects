import requests
from bs4 import BeautifulSoup
import random
from .constants import *
import sys

#logic
def getImagesAndDownloadLinks(htmlLink):
    dataToBeSent=set()
    headersList = getHeaders(htmlLink)
    htmlLink = UNSPLASH_SEARCH_URL.format(htmlLink)
    response = requests.get(htmlLink)
    htmlPage = response.text
    soup = BeautifulSoup(htmlPage, "html.parser")
    resultsList = soup.find_all('a', attrs={"class": UNSPLASH_LINK_CLASS})
    image = soup.find_all("div", attrs={'class': "_1tO5-"})
    print("len for image in whole page: ", len(image))
    for i in image:
        print(image, "\n--------->")

    try:
        count=0
        if resultsList!=None:
            resultsList = set(resultsList)
            for eachResult in resultsList:
                print("for: ", count)
                if eachResult!=None:
                    photoLink = UNSPLASH_BASE_URL + eachResult['href']
                    downloadLink = UNSPLASH_BASE_URL + eachResult['href'] + UNSPLASH_DOWNLOAD_SUFFIX
                    image = eachResult.find("img", attrs={'class': UNSPLASH_IMAGE_CLASS})
                    # print(eachResult)
                    if image!=None:
                        imageLink = image['srcset']
                        if imageLink != None:
                            imageLink = str(imageLink).split(" ")[2]
                            print(imageLink)
                            dataToBeSent.add((imageLink, downloadLink, photoLink))
                print("<------------->")
                count += 1
    except Exception as e:
        print(e, sys.gettrace())
    return dataToBeSent

def getHeaders(searchTerm):
    header={}
    header["authority"] = "unsplash.com"
    header["method"] = "GET"
    header["path"] = "/"
    header["scheme"] = "https"
    header["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    header["accept-encoding"] = "gzip, deflate, br"
    header["accept-language"] = "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7"
    header["cookie"] = "ugid=e678967129333775a7ce853a4151ffd35306834; xp-feedback-loop-v2=control; uuid=f31d9340-420a-11eb-9497-fdb7c65a81c6; xpos=%7B%22visual-search%22%3A%7B%22id%22%3A%22visual-search%22%2C%22variant%22%3A%22control%22%7D%7D; azk=f31d9340-420a-11eb-9497-fdb7c65a81c6; azk-ss=true; _ga=GA1.2.1283568001.1608390038; _gid=GA1.2.1623845230.1609437303; _sp_ses.0295=*; _sp_id.0295=67863e47-10ec-43b4-ac86-8da4608de984.1608390037.6.1609480942.1609439293.607fc6ae-2b8e-40f2-82b3-a8df0a315b24"
    header["referer"] = getReferrer()
    header["if-none-match"] = "W/\"4e1cc-cjFGFKy5J1wM57koJLVXGBuiG2E\""
    header["sec-fetch-dest"] = "document"
    header["sec-fetch-mode"] = "navigate"
    header["sec-fetch-site"] = "cross-site"
    header["sec-fetch-user"] = "?1"
    header["upgrade-insecure-requests"] = "1"
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