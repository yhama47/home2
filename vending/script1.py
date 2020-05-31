marchandise = {"orange juice": 200, "coffee": 150, "coke": 100 }
print(marchandise)
price1 = 200
price2 = 150
price3 = 100
while True:
    order = input("ご注文をお伺いします！")
    if order == "orange juice" or order == "coffee" or order == "coke":
        print("ご注文を確認しました！")
        break
    print("申し訳ありません。ご注文を確認できませんでした。もう一度正しい商品名でご注文ください！")

if order == "orange juice":
    while True:
        try:
            money = int(input("orange juiceですね！200円になります！投入金額をいれてください！"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if price1 > money:
            print(str(price1 - money) + "円不足しています! もう一度入力してください")
            continue
        elif money > price1:
            print(str(money - price1) + "円のお釣りです！")
            break
        else:
            print("ちょうどいただきました！ありがとうございました！")
            break

elif order == "coffee":
    while True:
        try:
            money = int(input("coffeeですね！150円になります！投入金額をいれてください！"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if price2 > money:
            print(str(price2 - money) + "円不足しています! もう一度入力してください")
            continue
        elif money > price2:
            print(str(money - price2) + "円のお釣りです！")
            break
        else:
            print("ちょうどいただきました！ありがとうございました！")
            break

elif order == "coke":
    while True:
        try:
            money = int(input("cokeですね！100円になります！投入金額をいれてください！"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        if price3 > money:
            print(str(price3 - money) + "円不足しています! もう一度入力してください")
            continue
        elif money > price3:
            print(str(money - price3) + "円のお釣りです！")
            break
        else:
            print("ちょうどいただきました！ありがとうございました！")
            break

repeat = input("ご注文を続けますか？ Yes or No ??")
if repeat == "Yes":
    order = input("ご注文をお伺いします！")
