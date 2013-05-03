
import math
import crawler

def pmi_tuple(base_entity, entities):
    total_documents = 5000000.0
    base_count = crawler.document_counts(base_entity.encode("utf8"))

    px = base_count / total_documents

    if len(entities) > 1 :
        msc = entities[0]
        lsc = entities[len(entities) - 1]

        max = msc[1]
        min = lsc[1]



    pmis=[]
    for entity in entities:
        word, cnt = entity
        entity_count = crawler.document_counts(word.encode("utf8"))
        py = entity_count / total_documents

        if py == 0:
            continue

        xy = "%s %s" % ( base_entity, word)
        base_entity_count = crawler.document_counts(xy.encode("utf8"))
        pxy = base_entity_count / total_documents

        pmi = 0
        if pxy != 0 and px != 0 and py != 0 :
            pmi = math.log( pxy / (px*py))

        rate = (entity[1] - min) / float(max - min)
        entity = entity + (pmi, (rate * 0.9) +  ( pmi * 0.1))
        pmis.append(entity)


    #print entitya
    from operator import itemgetter
    pmis = sorted(pmis, reverse = True, key=itemgetter(3))

    #print pmis

    #pmi_value, word = pmis[0].popitem()

    return pmis


def pmi(base_entity, entities):
    total_documents = 5000000000.0
    base_count = crawler.document_counts(base_entity.encode("utf8"))

    px = base_count / total_documents

    pmis=[]
    for entity in entities:
        entity_count = crawler.document_counts(entity.encode("utf8"))
        py = entity_count / total_documents

        if py == 0:
            continue

        xy = "%s %s" % ( base_entity, entity)
        base_entity_count = crawler.document_counts(xy.encode("utf8"))
        pxy = base_entity_count / total_documents

        pmi = pxy / (px * py)

        pmis.append({pmi: entity})

    pmis = sorted(pmis, reverse = True)
    print pmis

    pmi_value, word = pmis[0].popitem()

    return [word]


