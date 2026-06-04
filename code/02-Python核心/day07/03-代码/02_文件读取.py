#
# file =open("datax.txt","r",encoding="utf-8")
# c = file.read(2)  #设置读取长度
# print(c)
# file.close()

file =open("datas.txt","rb")
c = file.read(1024)  #设置读取长度
print(c)
file.close()

file =open("datas.txt","rb")
c = file.readlines(10) #按照行的方式进行读取，返回一个列表
print(c)
file.close()


file = open("datax.txt","r",encoding="utf-8")
c = file.readline() #readline 一次读取一行，读完指针下移
print(c)
file.close()

#遇到问题了！！！目前只打印一行。需求打印整首古诗。解决方案
file = open("datax.txt","r",encoding="utf-8")
#读写文件
while True:
    tf=file.readline()
    if not tf:
        break
    print(tf,end="")
file.close