class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "My name is %s Weight is %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)

        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1


xm = Person("小明", 75.0)

xm.run()
xm.eat()


xim = Person("小美", 45)

xim.eat()
xim.run()

print(xm)
print(xim)
