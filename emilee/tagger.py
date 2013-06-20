#coding:utf8

import xmlrpclib


def core_postagging(text):
    _RPC = xmlrpclib.Server("")
    try:
        result = _RPC.BuzzniTagger.postagging(text)
        #
    except:
        print "##ERROR : %s" % text
        result = ""
    return result

def core_jossegment(text):
    _RPC = xmlrpclib.Server("")
    try:

        result = _RPC.BuzzniTagger.jossegment(text)
    except:
        print "##ERROR : %s" % text
        result = ""
    return result


import re


def postagging(text):
    tagged = core_postagging(text)
    rows = re.split('[ +]', tagged)
    train = []
    for row in rows:
        train.append(row.split("/"))
    return train


def postagging_grouped(text):
    tagged = core_postagging(text)
    rows = re.split('[ +]', tagged)
    train = []
    for row in rows:
        train.append(row.split("/"))

    filtered = []
    isNN = False
    name = ""
    state = ""
    for row in train:
        if row[0] == "":
            continue
        try:
            if row[1] == "NNP":
                name = name + " " + row[0]
                state = row[1];
            else:
                if name != "":
                    filtered.append([name.strip(), state])
                    name = ""
                    state = ""
                filtered.append(row)
        except:
            print row
    if name != "":
        filtered.append([name.strip(), state])

    return filtered


def jossegment(text):
    tagged = core_jossegment(text)
    rows = re.split('[ +]', tagged)
    train = []
    for row in rows:
        train.append(row.split("/"))

    return train

