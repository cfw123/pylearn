class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s come " % self.name)

    def __del__(self):
        print("%s go" % self.name)


tom = Cat("Tom")
print(tom.name)

del tom

print("-" * 50)
