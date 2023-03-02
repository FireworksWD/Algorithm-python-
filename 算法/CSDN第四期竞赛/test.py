import jieba

txt = open('三国演义.txt', 'r', encoding='utf-8').read()  # 读取本地文件
words = jieba.lcut(txt)  # 使用lcut方法对文本分词
print(words)
counts = dict()  # 定义一个字典用来存放词的出现频率
for word in words:  # 遍历分词列表
    if len(word) == 1:  # 不统计长度为1的分词，这里主要是跳过标点符号，但也跳过了单个字的词
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # get方法返回键所对应的值，不在返回 0，+1统计次数
items = list(counts.items())  # 转为列表
items.sort(key=lambda x: x[1], reverse=True)  # 利用lambda函数对列表的第二个元素进行升序派
for i in range(10):  # 输出前十
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))  # 格式化输出
