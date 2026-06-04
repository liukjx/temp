
def func_b():
    print("func_b开始执行了")
    print("func_b开始执行函数代码体")
    print("func_b结束运行了")
def func_a():
    print("func_a开始执行了")
    func_b()   # 在一个函数中嵌套另一个函数
    print("func_a结束运行了")

# func_a()