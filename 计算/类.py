#一个计算类
class calculator:
    #初始化为输入
    def __init__(self):
        self.line = input()
        print(type(self.line))

    #对输入的字符串进行编辑并实现计算
    def calulate(self):
        #遍历字符串，从self.line[1]开始可避免第一个数为负数
        for item in self.line[1:]:
            if(item in '+-*/'):
                self.item1 = float(self.line[0: self.line.index(item)])  # 获取第一个数并float（）
                self.item2 = item
                self.item3 = float(self.line[self.line.index(item) + 1: len(self.line)])  # 获取第二个数并float（）
                # 执行计算
                if (item == '+'):
                    print(self.item1 + self.item3)
                if (item == '-'):
                    print(self.item1 - self.item3)
                if (item == '*'):
                    print(self.item1 * self.item3)
                if (item == '/'):
                    print(self.item1 / self.item3)
                break


if __name__ == '__main__':
    c1 = calculator() #构造一个计算类
    c1.calulate()     #实现计算


