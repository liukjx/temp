
str1="hello python hello world hello linux"

#方法一
# 要替换的内容, 替换后的内容, 替换的次数-可以省略
print(str1.replace("hello", "HELLO"))
print(str1.replace("hello", "HELLO",1))

#方法二：split
print("没有切得",str1)
print("切之后的",str1.split(" "))

print("切之后的",str1.split("python"))

print("没有title之前",str1)
print(str1.title())

# 字符串.join(数据序列)

list1=['a','b','c']
print(list1)
str2="❤".join(list1)
print(str2)

