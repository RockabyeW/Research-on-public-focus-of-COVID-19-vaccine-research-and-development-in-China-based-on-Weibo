import tensorflow_hub as hub

BERT_URL = "https://tfhub.dev/tensorflow/bert_zh_L-12_H-768_A-12/1"
bert_layer = hub.KerasLayer(BERT_URL, trainable=True, name='bert_layer')
