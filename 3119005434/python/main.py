import jieba
from process import getsfrequence


# 将a，b两个列表合并去重成新的列表
def get_tototal_list(alist, blist):
    answerlist = sorted(list(set(alist + blist)))
    return answerlist


# 测试
atxt = open("orig.txt", "r", encoding='utf-8').read()  # 读取orig.txt
btxt = open("orig_0.8_dis_10.txt", "r", encoding='utf-8').read()  # 读取orig_0.8_dis_10.txt
awords = jieba.lcut(atxt)  # 对orig.txt进行分词
bwords = jieba.lcut(btxt)  # 对orig_0.8_dis_10.txt进行分词
totalwords = get_tototal_list(awords, bwords)  # 得到两份文档的合并去重文档
print(totalwords)
bcounts = {}  # 通过键值对的形式存储orig_0.8_dis_10.txt中词语及其出现的次数
acounts = {}
getsfrequence(awords, totalwords, acounts)  # 通过键值对的形式存储orig.txt中词语及其出现的次数
getsfrequence(bwords, totalwords, bcounts)

print(acounts)
print(bcounts)
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
#
# for i in range(3):
#     word, count = items[i]
#     print("{0:<5}{1:>5}".format(word, count))
