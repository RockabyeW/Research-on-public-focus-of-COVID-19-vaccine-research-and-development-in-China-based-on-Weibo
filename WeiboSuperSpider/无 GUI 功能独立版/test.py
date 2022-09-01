import gensim
import os
import re
import sys
import multiprocessing
from tokenize import tokenize
from time import time


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for root, dirs, files in os.walk(self.dirname):
            for filename in files:
                file_path = '/topic/' + filename
                for line in open(file_path):
                    try:
                        sline = line.strip()
                        if sline == "":
                            continue
                        ###rline = cleanhtml(sline)
                        tokenized_line = ''.join(sline)
                        ###print(tokenized_line)
                        word_line = [word for word in tokenized_line.split()]
                        yield word_line
                    except Exception:
                        print("catch exception")
                        yield ""


if __name__ == '__main__':
    begin = time()
    sentences = MySentences("分词结果~15.csv")
    print(sentences.f)
    # model = gensim.models.Word2Vec(sentences,  window=15, min_count=10, workers=multiprocessing.cpu_count())
    # model.save("model/word2vec_gensim")
    # model.wv.save_word2vec_format("model/word2vec_org",
    #                               "model/vocabulary",
    #                               binary=False)
    #
    # end = time()
    # print("Total procesing time: %d seconds" % (end - begin))