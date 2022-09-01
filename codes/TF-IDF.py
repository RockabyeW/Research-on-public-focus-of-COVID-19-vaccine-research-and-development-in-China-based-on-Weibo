import jieba.analyse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

if __name__ == '__main__':
    with open('分词结果.csv', 'r', encoding='utf-8') as fp:
        vectorizer = CountVectorizer(max_features=10)
        # 该类会统计每个词语的tf-idf权值
        tf_idf_transformer = TfidfTransformer()
        # 将文本转为词频矩阵并计算tf-idf
        tf_idf = tf_idf_transformer.fit_transform(vectorizer.fit_transform(fp.readlines()))
        # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
        x_train_weight = tf_idf.toarray()

        # 对测试集进行tf-idf权重计算
        tf_idf = tf_idf_transformer.transform(vectorizer.transform(str(fp.readlines())))
        x_test_weight = tf_idf.toarray()  # 测试集TF-IDF权重矩阵

        print('输出x_train文本向量：')
        print(x_train_weight)
        print('输出x_test文本向量：')
        print(x_test_weight)