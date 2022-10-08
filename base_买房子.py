class Item:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]:占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, form, area):
        self.form = form
        self.area = area
        self.free_area = area
        self.item = []

    def __str__(self):
        return "房型：【%s】,\n总面积:【%.2f】,\n" \
               "剩余面积:【%.2f】,\n家具列表【%s】" % \
               (self.form, self.area,
                self.free_area, self.item)

    def additem(self, item):
        if self.free_area < item.area:
            return "抱歉，没有剩余空间了"
        self.free_area -= item.area
        self.item.append(item.name)
        print("[%s]添加成功" % item.name)


bed = Item("席梦思", 4)
chest = Item("衣柜", 2)
table = Item("餐桌", 1.5)
print(bed)
print(chest)
print(table)
house = House("两房一厅", 70)
house.additem(bed)
house.additem(chest)
house.additem(table)
print(house)

