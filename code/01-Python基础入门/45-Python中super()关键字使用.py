# 1. 定义一个公共父类
class Car(object):
    # 2. 定义公共属性和公共方法
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def run(self):
        print('i can run!')

# 2. 定义一个燃油车
class GasolineCar(Car):
    def run(self):
        print('i can run with gasoline!')

# 3. 定义一个电动车
class EletricCar(Car):
    def __init__(self, brand, model, color, battery):
        # 强调调用父类中的__init__()魔术方法
        super().__init__(brand, model, color)
        self.battery = battery

    def run(self):
        print(f'i can run with eletric, i have a {self.battery} kWh battery！')

bmw = GasolineCar('宝马', 'X5', '蓝色')
print(bmw.brand)
print(bmw.model)
print(bmw.color)
bmw.run()

tesla = EletricCar('Tesla', 'Model S', '黑色', 82)
print(tesla.brand)
print(tesla.model)
print(tesla.color)
tesla.run()