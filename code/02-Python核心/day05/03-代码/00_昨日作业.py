# #
# # 基础题:
# # 	1.键盘录入3个整数并接收, 将其最大值打印到控制台上.
# # 	 # 思路1: if语句.
#
#
# # 键盘录入3个整数并接收
# #键盘录入  input
# #3个整数   类型转换  int
# #并接收 变量名 = 变量值
# num1=int(input("请输入一个整数"))
# num2=int(input("请输入二个整数"))
# num3=int(input("请输入三个整数"))
#
# # #将其最大值打印到控制台上
# max_value=0
# #if语句  因为if语句可以比较
# if num1>num2 and num1>num3:
#     max_value=num1
# elif num2>num1 and num2>num3:
#     max_value=num2
# else:
#     max_value=num3
# print(max_value)
#
# #方式二   把求最大值这件事交给max()
# max_value = max(num1,num2,num3)
# print(max_value)


# 	2.循环实现计算 1 ~ 100之间的奇数和, 并将结果打印到控制台上.
# 		# 思路1: while循环.
# i = 1
# sum=0
# while i<101:
#     if i%2!=0:
#         sum+=i   #sum=sum+i
#     i+=1
# # 		# 思路2: for循环.
# for i in range(0,101,1):
#     if i % 2 != 0:
#         sum += i  # sum=sum+i
# print(sum)
#
# for i in range(1,101,2):
#         sum += i  # sum=sum+i
# print(sum)


# 	3. 猜数字游戏, 随机生成1个 1 ~ 100之间的数字, 让用户来猜, 并进行对应的提示.

# 	4. 模拟登陆, 只给3次机会, 登录成功则程序结束, 登陆失败则提示剩余登陆次数. 好好练


# 	5. 打印水仙花数, 将所有的水仙花数 及 水仙花数的总个数 打印到控制台上.
# 		水仙花数解释:
# 			1.水仙花数是1个三位数.
# 			2.它的各个位数的立方和相加等于它本身.
# 			 例如: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3  它就是1个水仙花数.
# 		提示:
# 			水仙花数一共有4个
#
# count = 0
# #1.水仙花数是1个三位数.
# for num in range(100,1000):
#     bw=num//100 #百位  bw 百位
#     sw = (num//10)%10  #十位  sw
#     gw =num%10    #个位 gw
#     # 它的各个位数的立方和相加等于它本身.
#     if (bw*bw*bw +sw*sw*sw +gw*gw*gw)  ==num :
#             count+=1
#             print(num)
# print(count)

for num in range(100,1000):
    str_num=str(num)
    bw=str_num[0:1]
    sw = str_num[1:2]
    gw= str_num[2:3]
    if (int(bw)**3 +int(sw)**3+int(gw)**3)==num:
        print(num)

