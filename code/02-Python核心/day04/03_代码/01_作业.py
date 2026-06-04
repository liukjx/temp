# AA制餐厅
# 需求: 假设你是一位很棒的AA制餐厅的服务员，你的任务是计算每位顾客的应付金额。
# 输入顾客人数，并赋值给total_friends变量。
# 输入总账单数值，并赋值配给 total_bill变量。
# 在账单费用上加上20%的税，并计算最终账单总额均摊给顾客金额，然后打印

# 输入顾客人数，并赋值给total_friends变量。
# 输入 input()
# 输入 顾客人数  input() 提示词
# 输入 字符串 类型转换
# 输入 转换为什么类型 ？ eval()


#值给total_friends变量
# 变量赋值   变量名 = 变量值
total_friends = eval(input("请输入顾客人数"))
# 输入总账单数值，并赋值配给 total_bill变量。
total_bill = eval(input("请输入总账单数值"))

# 在账单费用上加上20%的税，并计算最终账单总额均摊给顾客金额，然后打印
total_bill=total_bill*1.2

amunt_per_person=total_bill/total_friends
print(f"每位顾客应付金额是{amunt_per_person}")


# 1.键盘输入身高，体重，求BMI = 体重(kg)/身高(m)的平方
# 求BMI = （体重(kg)/身高(m)）的平方
# 求BMI = 体重(kg)/(身高(m)的平方)
height=eval(input("请输入身高"))
weight=eval(input("请输入体重"))
bmi=weight/(height**2)