#coding:utf8


import sys
import tagger
import rank
import crawler




def get_answer(question):

    question_post = tagger.postagging(question)
    question_part = []
    for q in question_post:
        if q[1] in ("NNP", "NNG", "NNB", "NP") :
            question_part.append(q[0])

    lines = crawler.crawling(question,question_part)

    entity = {}

    for line in lines:
        #print "### " + line
        line = line.replace("["," ").replace("]"," ").replace("“", "\"").replace("”","\"").replace("*", " ").replace("’", "'").replace("‘","'").replace("（","(").replace("：",":").replace("?"," ").replace("•", " ")

        tags = tagger.postagging_grouped(line)
        for tag in tags:
            #if tag[1] in ("NNP", "NNG", "NNB", "NP"):
            try:
                if len(tag) > 1 and (tag[1] in ("NNP", "NNG", "NP")): #) or tag[1] == ""):
                #print "[[%s : %s]]" % (tag[0], tag[1])
                    if entity.has_key(tag[0]):
                        entity[tag[0]] += 1
                    else:
                        entity.update({tag[0]: 1})
            except:
                print tag
                #break;



    max = 0
    ans = []
    for word, count in entity.items():
        if word is not None and count is not None and word not in question_part:
            ans.append((word, count))

    from operator import itemgetter
    ans = sorted(ans, reverse=True, key=itemgetter(1))

    ans = ans[:10]


    base_part = question_part[len(question_part)-1]
    print "base : [%s]" % base_part,
    result = rank.pmi_tuple(base_part, ans)
#
#    for word, count in entity.items():
#        if word in origin:
#            continue
#        if count > max:
#            max = count
#            ans = []
#            ans.append(word)
#        elif count == max:
#            ans.append(word)
    return result


if __name__ == "__main__":
   if len(sys.argv) < 2:
       print " Usage : %s \"Question\"" % sys.argv[0]
       sys.exit(1)

   ans = get_answer("애플의 전 회장은?")

   for answer in ans:
       print answer[0]
       break
