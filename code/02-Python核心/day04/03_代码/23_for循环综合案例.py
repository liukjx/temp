# 案例：用for循环实现用户登录
# ① 输入用户名和密码
# ② 判断用户名和密码是否正确（username='admin'，password='admin888'）
# ③ 登录仅有三次机会，超过3次会报错

username='admin'
password='admin888'
#输入出错计数器
tryCount=0
for i in range(3):
    tryCount=tryCount+1
    if tryCount<=3:
        # ① 输入用户名和密码
        uName=input("请输入用户名")
        pWord=input("请输入密码")
        # ②判断用户名和密码是否正确（username='admin'，password='admin888'）
        if (uName==username and pWord==password):
            print("登录成功")
            break
        else:
            print("登录失败")
            print(f"您还有{3 - tryCount}次输入的机会")

username='admin'
password='admin888'
#输入出错计数器
tryCount=0
for i in range(3):
    tryCount=tryCount+1
    if tryCount<=3:
        # ① 输入用户名和密码
        uName=input("请输入用户名")
        pWord=input("请输入密码")
        # ②判断用户名和密码是否正确（username='admin'，password='admin888'）
        if (uName==username and pWord==password):
            print("登录成功")
            break
        else:
            print("登录失败")
            if 3-tryCount==0:
                print("您没有机会了")
            else:
                print(f"您还有{3 - tryCount}次输入的机会")