# -*-coding:utf-8-*-

class Cat:
    def eat(self):
        print("cat like eat finsh")

    def drink(self):
        print("cat like drink")


tom = Cat()

tom.eat()
tom.drink()

print(tom)

addr = id(tom)
print("%x" % addr)
