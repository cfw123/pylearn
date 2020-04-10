class Cat:
    def __init__(self):
        print("This is init Method")
        self.name = "tom"

    def eat(self):
        print("%s like eat finsh" % self.name)


tom = Cat()



print(tom)
print(tom.name)
