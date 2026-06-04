"""封装一个函数，参数有两个num1，num2，求两个数的四则运算结果"""


#函数名未明确  自定义
#函数定义
#【形参】在函数定义时的参数就是形式参数
def calculator(num1,num2):
    print(num1+num2)
    print(num1*num2)
    print(num1-num2)
    print(num1/num2)

#函数调用
# TypeError: calculator() missing 2
#解释： 当前的函数是有参函数，我们在调用的过程中必须要给他参数，不然报错
calculator(1.0,3.0)
#【实参】函数调用是的参数就是我们实际参数
calculator(4,6)

