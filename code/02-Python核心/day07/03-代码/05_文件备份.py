"""
%s
分析：
    ①：用户输入要备份的文件名称
        字符串：a.txt  ->a[备份].txt
    ②：根据用户输入的文件名称进行获取文件名、文件后缀、组成的文件名称，文件名
        分析旧文件名  切       a   .    txt
        分析新文件名  a       [备份]   .txt
""" % TXT_A__TXT_
TXT_A__TXT_ = """需求分析：拷贝文件并改名.
        例如: 把 a.txt文件 拷贝到 a[备份].txt 文件中"""

#第一步：接受文件名
filename = input("请输入您要备份的文件名")

#第二步：拆   rfind
index = filename.rfind(".")
# print(index)   1 是.出现索引位置   a.txt    0   1   2  3  4
if index>0:
    #用户输入的文件名
    old_name = filename[:index] # print(old_name)
    #用户输入后缀
    old_suffix = filename[index:]
    #拼接新文件的名字
    new_name = old_name+"[备份]"+old_suffix

    #读写文件
    old_f = open(filename,"r",encoding="utf-8")
    new_f = open(new_name, "w", encoding="utf-8")
    while True:
        c = old_f.read()
        if len(c)==0:
            break
        new_f.write(c)
    old_f.close()
    new_f.close()
else:
    print("请正确输入文件名如：python.txt")


