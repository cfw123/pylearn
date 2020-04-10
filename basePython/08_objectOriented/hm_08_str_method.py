class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s come" % self.name)

    def __del__(self):
        print("%s go" % self.name)

    def __str__(self):
        return "I am cat[%s] " % self.name


tom = Cat("Tom")
print(tom)