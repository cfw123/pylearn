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

lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_cat2 = lazy_cat
print(lazy_cat)
