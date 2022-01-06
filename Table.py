from Wheel import Wheel

class Table:

    def __init__(self, num):
        self.tableNum = num
        self.table_wheel = Wheel(self.tableNum)

    def play(self):
        return self.table_wheel.spin()


