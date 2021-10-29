from gensim.models.ldamodel import LdaModel
import json
import pandas as pd


def print_topics(num_words=10):
    LDA_MODEL_PATH = 'lda.model'
    lda = LdaModel.load(LDA_MODEL_PATH)

    # print topics
    topics = lda.show_topics(num_words=num_words, formatted=False)

    topics_list = list()
    for t in topics:
        topics_list.append({'topic_id': int(t[0]), 'words_probs': dict(t[1])})

    return topics_list
	

if __name__ == "__main__":
    # api to show all topics
    print('python done!')
    print(print_topics(num_words=10))
