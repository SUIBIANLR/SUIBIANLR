import numpy as np


def process(awords, bwords):
    acounts = get_a_frequence(awords, bwords)  # 通过a和b的分词列表得到a的词频向量
    bcounts = get_a_frequence(awords, bwords)  # 通过a和b的分词列表得到b的词频向量
    a_value_list = list(acounts.values())  # 转化为列表
    b_value_list = list(bcounts.values())
    a_value_array = np.array(a_value_list)  # 转化为数组
    b_value_array = np.array(b_value_list)
    repetition = calculate_repetition(a_value_array, b_value_array)  # 通过a与b的词频向量得出查重率
    return repetition


def calculate_numerator(arraya, arrayb):
    numerator=np.matmul(arraya,arrayb)
    return numerator


def calculate_denominator(arraya, arrayb):
    ma=np.linalg.norm(arraya)
    mb=np.linalg.norm(arrayb)
    denominator=ma*mb
    return denominator



def calculate_repetition(arraya, arrayb):
    numerator = calculate_numerator(arraya, arrayb)
    denominator=calculate_denominator(arraya,arrayb)
    repetition=numerator/denominator
    return repetition


def get_a_frequence(awords, bwords):
    totalwords = get_tototal_list(awords, bwords)  # 得到两份文档的合并去重文档
    acounts = getsfrequence(awords, totalwords)
    return acounts


def get_b_frequence(awords, bwords):
    totalwords = get_tototal_list(awords, bwords)  # 得到两份文档的合并去重文档
    bcounts = getsfrequence(awords, totalwords)
    return bcounts


# 得到文档中的词频向量
def getsfrequence(words, Totalwords):
    initialvalue = []  # 得到空列表，以便和totalwords合并成为每个键的值都是0的counts词典
    number = 1  # 计数
    while number <= len(Totalwords):  # totalwords中元素有多少个就生成多少个0
        initialvalue.append(0)
        number = number + 1
    counts = dict(zip(Totalwords, initialvalue))  # 合并成为词典

    for word in words:  # 对于每一个在目标文档中的词语进行遍历，若发现它在合并去重文档中出现过，则将它的出现次数加一
        if word in Totalwords:  # 如果该词语出现在Totalwords中
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
    return counts


# 得到合并去重列表
def get_tototal_list(alist, blist):
    answerlist = []
    for word in alist:
        if word in answerlist:
            continue
        else:
            answerlist.append(word)
    # 将alist赋值给合并去重列表
    for bword in blist:  # 对于blist中每一个词语，若它出现在answerlist中，则应跳过，若不出现，则应加入
        if bword in answerlist:
            continue
        else:
            answerlist.append(bword)
    return answerlist