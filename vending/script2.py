class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def message(self):
        return self.name + " : $" + str(self.price)

    def asking_order(self):
        while True:
            order = input("ご注文をお伺いします！")
            if order == "orange juice" or order == "coffee" or order == "coke":
                print("ご注文を確認しました！")
                break
            print("申し訳ありません。ご注文を確認できませんでした。もう一度正しい商品名でご注文ください！")

    def change_calc(self):
        while True:
            try:
                money = int(input("投入金額をいれてください！"))
                gotten_money = money
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if self.price > gotten_money:
                print(str(self.price - gotten_money) + "円不足しています! もう一度入力してください")
                continue
            elif gotten_money > self.price:
                print(str(gotten_money - self.price) + "円のお釣りです！")
                break
            else:
                print("ちょうどいただきました！ありがとうございました！")
                break


item1 = Item("orange juice", 250)
item2 = Item("coffee", 100)
item3 = Item("coke", 150)

items = [item1, item2, item3]


for item in items:
    print(item.message())


print(item.asking_order())

print(item.change_calc())

