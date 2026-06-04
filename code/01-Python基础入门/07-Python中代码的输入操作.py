'''
在Python代码中，我们可以通过input()函数接收外部设备的输入。
注意：接受到的任何数据都是字符串类型
'''
password = input('请输入您的银行卡密码：')
print(password)
print(type(password))

num1 = int(input('请输入一个整数：'))
print(num1)
print(type(num1))

num2 = float(input('请输入一个浮点数：'))
print(num2)
print(type(num2))