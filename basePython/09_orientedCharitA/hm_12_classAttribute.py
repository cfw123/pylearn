class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2. 输出工具对象的总数
print(Tool.count)
