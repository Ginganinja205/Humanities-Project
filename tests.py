def inputtemplate(message, numberortext, numberofoptions):
    theinput = input(message)
    if numberortext == 0:
        try:
            thenumberinput = int(theinput)
        except:
            print(str('Please type one of the numbers listed.\n'))
            return
        if numberofoptions < thenumberinput or thenumberinput < 1:
            print(str('Please type one of the numbers listed.\n'))
        else:
            return thenumberinput
    else:
        return str(theinput)

def indial(fd, il, rl, lcraft, scraft, me):
    fd, il, rl, lcraft, scraft = miran(fd, il, rl, lcraft, scraft, me)
    return fd, il, rl, lcraft, scraft

def miran(oo, i, ea, eea, aa, ae):
    count = 0
    while True:
        if count == 0:
            messageinmiran = str(f"\nCongratulations, {ae}. You have safely traveled from Lanzhou to Miran. Along the way you visited Wuwei, Anxi, and Loulan. You have only stopped now because you are completely out of food. In order to continue to your next destination, you must stock up. This town has little to offer, but the local tradesmen are eager to see what you have to offer in return for food. If you wish to continue you require 1000 food. Steel will carry a slightly higher value due to this town's need for protection from barbarians. However, there is little need or desire for silk in this quaint town. Go! Trade!\n 1. Market\n 2. Continue Journey\n 3.Exit\n")
        else:
            messageinmiran = str(f"\nYou need 1000 food to continue.\n 1.Market\n 2. Continue Journey\n 3. Exit\n ")
        decisioninmiran = inputtemplate(messageinmiran, 0, 3 )
        if decisioninmiran == 1:
            oo, i, ea, eea, aa = marketinmiran(oo, i, ea, eea, aa, ae)
        elif decisioninmiran == 2:
            if oo >= 1000:
                return oo, i, ea, eea, aa
                break
            else:
                print("\nYou don't have enough food!\n")
        elif decisioninmiran == 3:
            exit()
        count = 1

def marketinmiran(eatables, thread, shiny, sharp, ornament, un):
    while True:
        marketinmiranmessage = str(f"Welcome {un} to the market. You have {eatables} food, {thread} units of silk, {shiny} bags of pearls, {sharp} steel products, {ornament} brass products.\n 1. Sell Silk\n 2. Sell Pearls\n 3. Sell Steel Products\n 4. Sell Brass Products\n 5. Leave Market\n")
        decisioninmarketinmiran = inputtemplate(marketinmiranmessage, 0, 5)
        if decisioninmarketinmiran == 1:
            eatables, thread = transinmarketm(eatables, thread, 'silk', 155)
        elif decisioninmarketinmiran == 2:
            eatables, shiny = transinmarketm(eatables)
        elif decisioninmarketinmiran == 3:
            eatables, sharp = transinmarketm(eatables)
        elif decisioninmarketinmiran == 4:
            eatables, ornament = transinmarketm(eatables)
        elif decisioninmarketinmiran == 5: break
    return eatables, thread, shiny, sharp, ornament

def transinmarketm(eat, product, productname, sellprice):
    while True:
        sellmessage = str(f"How much {productname} would you like to sell? You will get {sellprice} food per unit of silk sold. You currently have {eat}  food, and {product} units of {productname}. You can sell up to 100 units at a time. If you wish to exit, type 101 and 'Enter'.\n")
        productsellnumber = inputtemplate(sellmessage, 0 , 101)
        if productsellnumber == 101:
            return eat, product
            break
        else:
            if productsellnumber > product:
                print("You don't have enough!!\n")
            else:
                product = product - productsellnumber
                eatgained = productsellnumber * sellprice
                eat = eat + eatgained

def main():
    food, sil, pearl, steelcraft, brasscraft = indial(0, 10, 10, 10, 10, 'Henry Lima')
    print("done test")
    print(food, sil, pearl, steelcraft, brasscraft)
if __name__ == '__main__':
    main()
