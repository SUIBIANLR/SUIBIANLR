# 得到文档中的词频
def getsfrequence(words, Totalwords):
    initialvalue=[] # 得到空列表，以便和totalwords合并成为每个键的值都是0的counts词典
    number=1 # 计数
    while number<=len(Totalwords):# totalwords中元素有多少个就生成多少个0
        initialvalue.append(0)
        number=number+1
    counts = dict(zip(Totalwords, initialvalue))# 合并成为词典

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


awords = ['我', '明天', '要', '上课', '鞋', '明天']
bwords = ['你', '明天', '不用', '上课', '好吧']
totallist = get_tototal_list(awords, bwords)
print(totallist)
print(awords)
print(bwords)
acounts =getsfrequence(awords, totallist)
bcounts =getsfrequence(bwords, totallist)
print(acounts)
print(bcounts)
# a=['b','c','sdfa','d']
# b=[]
# counts={}
# number=1
# while number <= len(a):
#     b.append(0)
#     number = number + 1
# counts = dict(zip(a, b))
# print(counts)
