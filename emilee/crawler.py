#coding:utf8

import urllib
import re
import HTMLParser
import psycopg2


from xml.dom import minidom


def html_to_text(text):
    htmlparser = HTMLParser.HTMLParser()
    return htmlparser.unescape(re.sub('<[^<]+?>', '', text))


def html_to_text2(text):
    return re.sub('<[^<]+?>', '', text)


def rec_search(nodes, name, contexts):
    for node in nodes:
        rec_search(node.childNodes, name, contexts)

        if node.nodeValue and node.nodeValue.find(name) != -1:
            contexts.append(node.nodeValue)


def get_context(url, name):
    html_data = urllib.urlopen(url)
    #print html_data
    contexts = []
    dom = minidom.parse(html_data)
    body = dom.getElementsByTagName("body")

    rec_search(body, name, contexts)

    return contexts
    #for child in body.childNodes:


def get_db():
    db = psycopg2.connect(host="", database="", user="", password="")
    return db

def document_counts(text):
    db = None
    try :
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT count FROM word_count where word = \'%s\'" % text)
    except:
        print "[ERROR] %s" % text

    record = cur.fetchone();
    if record:
        count, = record
        db.close()
        return int(count)


    url = "http://openapi.naver.com/search?key=7f2c8fab20ff3e2991eafab9c4e1d1f1&query=%s&target=blog&start=1&display=20" % text
    dom = minidom.parse(urllib.urlopen(url))
    items = dom.getElementsByTagName("total")
    for item in items:
        cnt = int(item.childNodes[0].nodeValue)
        try :
            db = get_db()
            cur.execute("INSERT INTO word_count(word, count) values (\'%s\', %d)" % (text, cnt))
            db.commit()
        except:
            print "[ERROR] %s" % text
        db.close()
        return cnt

def crawling(name, qps):
    import re
    #fd = open("../crawled/crawled3.txt", "a+")
    #fd.write("#q#"+name+"\n")
    texts = []
    #url = "http://newssearch.naver.com/search.naver?where=rss&query=" + name
    url = "http://openapi.naver.com/search?key=7f2c8fab20ff3e2991eafab9c4e1d1f1&query=%s&target=blog&start=1&display=10" % name
    dom = minidom.parse(urllib.urlopen(url))
    items = dom.getElementsByTagName("item")
    for item in items:
        for node in item.childNodes:
            if node.nodeName == "description":
                #print node.childNodes[0].nodeValue
                if node is not None and node.childNodes is not None and len(node.childNodes) > 0:
                    text = html_to_text(node.childNodes[0].nodeValue.replace("...", "")).encode("utf8")

                    for sents in text.split(". "):
                        #if sent.find(name) != -1:
                        #sent = sent.decode("utf8")
                        for sent in sents.split("\n"):
                            isMatched = False
                            for qp in qps:
                                if sent.find(qp.encode("utf8")) != -1:
                                    isMatched = True

                            if isMatched :

                                sent = re.sub(r"[ ]+", r" ", sent)
                                sent = re.sub(r"[ \n]{2,100}", r"\n", sent).strip()
                                #fd.write("#a#"+sent + '\n')
                                texts.append(sent)
    #fd.close()
    return texts
