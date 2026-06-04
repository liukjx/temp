"""
查找：
    find()： 用查找子串在字符串中出现位置，找到返回索引下标，找不到返回-1
    index(): 用查找子串在字符串中出现位置，找到返回索引下标，找不到报错

"""
str1="hello python hello world hello linux"
#子串hello
print(str1.find("python"))

print(str1.index("hallo"))
