import jieba
import re
def v(text):
    words = []
    seg_list = lcut(text, cut_all=False)  # 使用jieba下的lcut()方法，返回一个列表
    pat = re.compile(u'[a-zA-Z0-9\u4e00-\u9fa5]').sub(" ","")  # 将正则表达式转换为内部格式，提高执行效率
    for word in seg_list:
        if re.match(pat, word):
            words.append(word)  # 筛选出不含标点符号的结果
        else:
            pass
    return words