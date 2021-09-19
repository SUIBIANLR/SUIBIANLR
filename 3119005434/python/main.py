import re
import jieba
import sys
from process import process
from output import output


# 将a，b两个列表合并去重成新的列表
def get_tototal_list(alist, blist):
    answerlist = sorted(list(set(alist + blist)))
    return answerlist


# 传入3个参数，具体操作根据个人情况
def main(argv):
    try:
        orig = argv[1]
        orig_dis = argv[2]
        answer_where_to_output = argv[3]
        awords = input(orig)  # 将原始文档进行预处理，得到分词后的列表
        bwords = input(orig_dis)  # 将抄袭文档进行预处理，得到分词后的列表
        repetition = process(awords, bwords)  # 将两个分词后的列表输入，得到查重率
        output(repetition, answer_where_to_output)  # 将查重率写入answer_where_to_output指向的目录下
    except IndexError:
        pass


def input(file):  # 对文件进行预处理从而得到一个分词后的列表
    filetxt = open(file, "r", encoding='utf-8').read()  # 读取orig.txt
    # filetxt = filetxt.replace('\n', '')
    # filetxt = filetxt.replace(' ', '')
    # filetxt = filetxt.replace('，', '')
    # filetxt = filetxt.replace('。', '')
    filetxt=replace_all_blank(filetxt)
    filewords = jieba.lcut(filetxt)  # 对orig.txt进行分词
    return filewords


def replace_all_blank(value):
    result = re.sub('\W+', '', value).replace("_", '')
    print(result)
    return result


awords = []
bwords = []
if __name__ == "__main__":
    main(sys.argv)
