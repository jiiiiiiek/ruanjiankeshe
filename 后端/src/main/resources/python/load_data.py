# coding: utf-8
import numpy as np
import jieba
from snownlp import SnowNLP


def load_text(datatext):
    # text
    text_data = []
    for sentence in datatext:
        if len(sentence) > 20:
            s = SnowNLP(sentence)
            summart_text = s.summary(3)
            summary_string = '，'.join(summart_text)
            sentence = summary_string[:20]
        words = list(jieba.cut(sentence))
        text_data.append(words)
    return text_data
