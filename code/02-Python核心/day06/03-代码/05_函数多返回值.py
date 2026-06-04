# 版本一
def funtuple():
    return (1, 2)


#版本二
def funtuple2():
    return 1, 2

# 版本三
def funtuple3():
    return 1,

def funtuple4():
    return 1

print(funtuple())
print(funtuple2())
print(type(funtuple3()))
print(type(funtuple4()))
