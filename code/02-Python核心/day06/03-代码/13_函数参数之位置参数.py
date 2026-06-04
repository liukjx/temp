# 定义函数
def func(name, age, address,gender='男'):
    return ("你的名字是:", name, "你的年龄是:", age, "你的地址是", address,"你的性别是",gender)

# 调用函数 传参之【位置参数】  正确位置
print(func("张三", 20, "北京昌平"))
# 调用函数 传参之【位置参数】  错误位置
print(func(20, "北京昌平", "张三"))

# 形式参数是否可以和实际参数同名？ 可以，因为形式参数是局部比那里，只在函数运行时有效。运行后消失


#调用函数 传参之【关键字参数】  正确   key:value  打破位置参数，位置依赖
print(func(age=20, address="北京昌平", name="张三"))


#调用参数之缺省的-默认值
print(func("zhangsan", 20, "北京海淀"))
print(func("zhangsan", 20, "北京海淀","女"))

#注意事项
    # 1：有位置参数是，位置参数必须在关键字参数前面
# print(func(gender="女","zhangsan", 20, "北京海淀"))
#报错 ： 违反了上面的约定