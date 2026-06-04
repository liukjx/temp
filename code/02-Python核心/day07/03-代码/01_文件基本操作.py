"""
文件操作三步走
    ①打开文件
    ②读写文件
    ③关闭文件
 ①打开文件 ：注意  在进行文件操作之前，一定要提前打开文件，否则无法对文件进行操作
            open()方法:主要用来打开一个文件，
            原理：如果打开文件不存在，则自动创建一个新的文件
   格式：open("文件名","操作模式")
        文件名：打开谁，传递谁！   注意路径 绝对路径  相对路径
        操作模式：
            r：read ，代表只读的方式打开文件
            w：write,代表以只写的方式打开文件    原理：首先要清空整个文件的内容，从头开始写入
            a：append 代表以追加的方式开发文件，实现数据写入，原因：不需要清空文件原有内容，在文件基础进行追加操作
            ------以上r、w、a主要是针对文本文件进行操作，如果你要对图形，音频、视频这些非文本进行操作
            rb binary： 以二进制流的方式进行读取文件
#             wb binary： 以二进制流的方式进行写入文件
# """
# #打开一个文件，并且向文件中追加一句话 “社会主义好”
# #1.打开一个文件
# fileName = open("python.txt","a",encoding="utf-8")
# #2.对文件进行写操作
# fileName.write("社会主义好")
# #3.关闭文件
# fileName.close()
#
# #演示write清空
# filename2  = open("python.txt","w",encoding="utf-8")
# filename2.write("坚持和落实“两个毫不动摇”")
# filename2.close()

#演示文件读取
#1：打开文件
fileR = open("python.txt","r",encoding="utf-8")
#2:读取文件
content = fileR.read()
print(content)
#3：关闭资源
fileR.close()
# No such file or directory: 'pytshon.txt'








