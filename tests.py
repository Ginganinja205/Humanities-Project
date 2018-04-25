#This function is for the multiple times input will have to be vetted. For second argument put 0 for numbers and anythingelse for text.
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
    ice = 0
    fd, il, rl, lcraft, scraft, ice = purushapura(fd, il, rl, lcraft, scraft, ice, me)
    return fd, il, rl, lcraft, scraft, ice

def miran(oo, i, ea, eea, aa, ae):
    count = 0
    while True:
        if count == 0:
            messageinmiran = str(f"\nCongratulations, {ae}. You have safely traveled from Lanzhou to Miran. Along the way you visited Wuwei, Anxi, and Loulan. You have only stopped now because you are completely out of food. In order to continue to your next destination, you must stock up. This town has little to offer, but the local tradesmen are eager to see what you have to offer in return for food. If you wish to continue you require 1000 food. Steel will carry a slightly higher value due to this town's need for protection from barbarians. However, there is little need or desire for silk in this quaint town. Go! Trade!\n 1. Market\n 2. Continue Journey\n 3. Exit\n")
        else:
            messageinmiran = str(f"\nYou need 1000 food to continue.\n 1. Market\n 2. Continue Journey\n 3. Exit\n ")
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
        marketinmiranmessage = str(f"Welcome, {un}, to the market! You have {eatables} food, {thread} units of silk, {shiny} bags of pearls, {sharp} steel products, {ornament} brass products.\n 1. Sell Silk\n 2. Sell Pearls\n 3. Sell Steel Products\n 4. Sell Brass Products\n 5. Leave Market\n 6. Advice From Amil Yrneh\n")
        decisioninmarketinmiran = inputtemplate(marketinmiranmessage, 0, 6)
        if decisioninmarketinmiran == 1:
            eatables, thread = transinmarketm(eatables, thread, 'units of silk', 160)
        elif decisioninmarketinmiran == 2:
            eatables, shiny = transinmarketm(eatables, shiny, 'bags of pearls', 105)
        elif decisioninmarketinmiran == 3:
            eatables, sharp = transinmarketm(eatables, sharp, 'steel products', 135)
        elif decisioninmarketinmiran == 4:
            eatables, ornament = transinmarketm(eatables, ornament, 'brass products', 65)
        elif decisioninmarketinmiran == 5: break
        elif decisioninmarketinmiran == 6:
            print("\nThe value of silk and pearl will continue to increase as you travel, so I would wait to sell those. I think you should sell some steel, as it is more valuable here than in peaceful towns. I would also sell some brass, as its price won't differ from location to location.\n")
    return eatables, thread, shiny, sharp, ornament

def transinmarketm(eat, product, productname, sellprice):
    while True:
        sellmessage = str(f"How many {productname} would you like to sell? You will get {sellprice} food per unit of silk sold. You currently have {eat} food, and {product} {productname}. You can sell up to 100 units at a time. If you wish to exit, type 101 and 'Enter'.\n")
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

def purushapura(foo, sils, pea, stc, brc, spc, moi):
    count = 0
    while True:
        if count == 0:
            messageinpurushapura = str(f"\nCongratulations, {moi}. You have safely traveled from Miran to Purushapura. Along the way you visited Niya, Khotan, and Srinagar. You have only stopped now because you are completely out of food. In order to continue to your next destination, you must stock up. The local tradesmen are eager to see what you have to offer in return for food. During this period, India's economy is mostly based off of agriculture (like most civilizations) and craftspeople. If you wish to continue you require 1500 food. You are in Northern India which is currently ruled by Chandragupta Maurya. Maurya has put into place a tax system and made safe, well-constructed roads. In fact, there is even a government coin, further solidifying the economy. While here, you can buy spices to sell in foreign nations. People are willing to pay highly for silk; silk textiles are one of the main exports. Go! Trade!\n 1. Market\n 2. Continue Journey\n 3. Exit\n")
        else:
            messageinpurushapura = str(f"\nYou need 1500 food to continue.\n 1. Market\n 2. Continue Journey\n 3. Exit\n ")
        decisioninpurushapura = inputtemplate(messageinpurushapura, 0, 3 )
        if decisioninpurushapura == 1:
            foo, sils, pea, stc, brc, spc = marketinpurushapura(foo, sils, pea, stc, brc, spc, moi)
        elif decisioninpurushapura == 2:
            if foo >= 1500:
                return foo, sils, pea, stc, brc, spc
                break
            else:
                print("\nYou don't have enough food!\n")
        elif decisioninpurushapura == 3:
            exit()
        count = 1

#CHANGE VARIABLE NAMES ADD SPICE CODE  eatables etc.
def marketinpurushapura( od, sik, pel, stel, bras, spic, mei):
    while True:
        marketinpurumessage = str(f"Welcome, {mei}, to the market! You have {od} food, {sik} units of silk, {pel} bags of pearls, {stel} steel products, {bras} brass products.\n 1. Sell Silk\n 2. Sell Pearls\n 3. Sell Steel Products\n 4. Sell Brass Products\n 5. Buy Spice\n 6. Leave Market\n 7. Advice From Amil Yrneh\n")
        decisioninmarketinpuru = inputtemplate(marketinpurumessage, 0, 6)
        if decisioninmarketinpuru == 1:
            od, sik = transinmarketm(od, sik, 'units of silk', 175)
        elif decisioninmarketinpuru == 2:
            od, pel = transinmarketm(od, pel, 'bags of pearls', 110)
        elif decisioninmarketinpuru == 3:
            od, stel = transinmarketm(od, stel, 'steel products', 120)
        elif decisioninmarketinpuru == 4:
            od, bras = transinmarketm(od, bras, 'brass products', 65)
        elif decisioninmarketinpuru == 5:
            sik, pel, stel, bras, spic = buyspice(sik, pel, stel, bras, spic)
        elif decisioninmarketinpuru == 6: break
        elif decisioninmarketinpuru == 7:
         print("\nThe value of silk is fairly high here, although it will be highest in Alexandria. I think you shouldn't sell steel, as it is less valuable here thanks to the peace brought by Maurya.\n")
    return od, sik, pel, stel, bras, spic

def buyspice(dea, yni, pra, tne, cip):
    while True:
        spicebuymessage = str(f"\nPlease type what you wish to good you wish to exchange for spice. Spice will be valuable. You have {dea} units of silk, {yni} bags of pearls, {pra} steel products, {tne} brass products, and {cip} units of spice.\n 1. Exchange Spice\n 2. Exchange Pearls\n 3. Exchange Steel Products\n 4. Exchange Brass Products\n 5. Return To Main Market\n")
        exchangetype = inputtemplate(spicebuymessage, 0, 5)
        if exchangetype == 1:
            amountexchange = inputtemplate("How much would you like to exchange? The rate is 4 spice per silk. Enter 101 to exit.\n", 0, 101)
            if amountexchange != 101:
                dea = dea - amountexchange
                cipadded = amountexchange * 4
                cip = cip + cipadded
        elif exchangetype == 2:
            amountexchange = inputtemplate("How much would you like to exchange? The rate is 2 spice per bag of pearls. Enter 101 to exit.\n", 0, 101)
            if amountexchange != 101:
                yni = yni - amountexchange
                cipadded = amountexchange * 2
                cip = cip + cipadded
        elif exchangetype == 3:
            amountexchange = inputtemplate("How much would you like to exchange? The rate is 1 spice for 1 steel product. Enter 101 to exit.\n", 0, 101)
            if amountexchange != 101:
                pra = pra - amountexchange
                cip = cip + amountexchange
        elif exchangetype == 4:
            amountexchange = inputtemplate("How much would you like to exchange? The rate is 1 spice for 1 brass product. Enter 101 to exit.\n", 0, 101)
            if amountexchange != 101:
                tne = tne - amountexchange
                cip = cip + amountexchange
        elif exchangetype == 5:
            return dea, yni, pra, tne, cip
            break


def main():
    food, sil, pearl, steelcraft, brasscraft, spice = indial(0, 10, 10, 10, 10, 'Henry Lima')
    print("done test")
    print(food, sil, pearl, steelcraft, brasscraft, spice)
if __name__ == '__main__':
    main()
