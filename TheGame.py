#Opening Screen Credits and Stuff Here
def beginningcode(wronginputmssg):
    while True:
        playorexit = input("\nWelcome Participant\n Please type '1' to start, '2' to exit, '3' for How To Play, or '4' for credits. Press 'Enter' when you have selected your choice.\n 1. Start\n 2. Exit\n 3. How To Play\n 4. Credits/Citations\n")
        try:
            choice1 = int(playorexit)
        except:
            print(wronginputmssg)
            continue
        if choice1 == 1:
            break
        elif choice1 == 2:
            exit()
        elif choice1 == 3:
            Instructions(wronginputmssg)
            break
        elif choice1 == 4:
            Citations()
            break
        else:
            print('wronginputmssg')

#Gives User Initial Guidance
def Instructions(wronginput):
    while True:
        howtoplay = input("\nBy selecting this you are already on the right track. Your goal is to try and make the character you select as profitable as possible, and my goal is to try to teach you about the economies of Ancient Civilizations. Throughout this interactive teaching program you will be asked to make multiple decisions, some small some large, in order to achieve your goal. Along the way, you may encounter things that you are unfamiliar with, or decisions you feel unable to make. If this happens, there should be an option to give you more information. Select this, read through the given information, and try again. (DISCLAIMER: Some elements of this game are ficticious and non-factual.) Type the number corresponding to your answer then press 'Enter'. If you want to read something that you previously read, scroll up. If you still have problems, please call me (Henry Lima) over. Thank you. (Press the 'SpaceBar' then 'Enter' to continue.)")
        if howtoplay == ' ':
            beginningcode(wronginput)
            break

def Citations():
    print()

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

#Username, Establishes Base Products Currency, Leads to Market or Cont.s to Journey
def startingpage():
    namemssg = str("\nHello user! You have been raised as a merchant in Luoyang, a town in Ancient China (for the intent of this game Ancient refers to a period from 400 BC to 1 BC). Your father has recently decided that it is time for you to attempt a practical execution of your knowledge. You will journey to Alexandria, Egypt with a small company of guards and servants to look after you and your wealth. Your scholar Amil Yrneh will go with you and act as guide. At the start of your journey, you will take some of your father's money and buy some goods and commodities to trade with along the way. China was one of the first nations to have government minted coinage, and this use of official currency bolstered their economy and created growth in the middle class. Your father gives you your spending money in the form of this coinage. However, before we can continue please type your name:\n")
    theusername = inputtemplate(namemssg, 1, 1)
    Coins = 5000
    silk = 0
    silkworms = 0
    pearls = 0
    steelcrafts = 0
    brasscrafts = 0
    beginjourneymessage = str(f"\nBefore you begin your journey {theusername}, you may wish to stop by the marketplace to stock up on goods and commodities. You may also begin your journey immediately.\n 1. Marketplace\n 2. Begin Journey\n 3. Exit\n")
    marketorstart = inputtemplate(beginjourneymessage, 0, 3)
    return theusername, Coins, silk, silkworms, pearls, steelcrafts, brasscrafts, marketorstart

#Only Buying Things, Lots of Info For Hum. Wonderful Bit of code
def marketplaceChina(C, s, sw, p, stc, bc, username):
    while True:
        cmarketopening = inputtemplate(f"\nWelcome to the market place, {username}! You have {C} coins, {s} units of silk, {sw} units of silkworm, {p} bags of pearl, {stc} steel products, and {bc} brass products. Here you will be able to purchase goods to sell in foreign lands. Keep in mind that some of the goods you can buy in China will not be available elsewhere.\n 1. Silk\n 2. Silkworms\n 3. Pearls\n 4. Steel Products (Armor and Weapons)\n 5. Brass Products (Mainly Ornamentation)\n 6. More Info\n 7. Continue With Journey\n 8. Exit\n ", 0, 8)
        if cmarketopening == 1:
            s, C = markettrans('units of silk', 150, s, C)
        elif cmarketopening == 2:
            sw, C = markettrans('units of silkworm', 500, sw, C)
        elif cmarketopening == 3:
            p, C = markettrans('bags of pearls', 100, p, C)
        elif cmarketopening == 4:
            stc, C = markettrans('steel products', 120, stc, C)
        elif cmarketopening == 5:
            bc, C = markettrans('brass products', 60, bc, C)
        elif cmarketopening == 6:
            print("\nHello, I am Amil Yrneh, your guide.\n 1. Silk and Silkworms - China was the first civilization to discover how to create silk. Silk is created by silkworms when they form a cocoon. The cocoon can then be boiled, pulled of the worm, and spun into silk. However, it takes thousands of worms to make just a pound of silk. Since China is the only one who knows how to make it, it is literally worth its weight in gold in foreign civilizations. The farther away you go the more valuable it gets (due to its increased scarcity). Since no one else knows the secret to silk, the selling of silkworms to foreigners is punishable by death. However, if you managed to do it secretly, you would be the richest man in China!\n 2. Pearls - The Chinese were also the first to farm pearls. Their scarcity in foreign nations make them valuable, but they serve little practical purpose other than decoration. Their value will also go up the farther you are from China, but not as steeply.")
            print(" 3. Steel Products - China was also amongst the first to smelt iron into steel. Steel is much stronger than iron and is ideal for tools of war. Peaceful foreigners will not want to pay such high prices for weaponry, even if its are superior to their current stock. However, cities and towns with a strong military presence will definitely snap them up.\n 4. Brass Products - Brass is an alloy of copper, zinc, and lead, all of which China has large quantities of. It is mostly used for ornamentation, and it is a nice fallback to trade with in foreign nations if you want to save other products for later.\n 5. Food - In China, you will never go hungry. China has no shortage of food, due to their advanced farming techniques. This includes mixed stock rearing (a technique involving raising multiple agricultural lifeforms to increase efficiency), and puddling (tiered pools used to keep rice hydrated). However, in other civilizations you will want to buy food (to survive).\n\n")
        elif cmarketopening == 7:
            return C, s, sw, p, stc, bc
            break
        elif cmarketopening == 8:
            exit()

#Math For Buying
def markettrans(product, price, amountotal, Cns):
    while True:
        unitsofs = inputtemplate(f"How many {product} would you like to buy? You may purchase up to 100 units of something at a time. If you wish to exit, buy 101 units (this is equivalent to buying 0 units). The price per unit is {price} coins.\n", 0, 101)
        if unitsofs != None:
            if unitsofs == 101:
                amountotal = amountotal + 0
                Cns = Cns - (price * 0)
                return amountotal, Cns
            elif Cns >= price * unitsofs:
                amountotal = amountotal + unitsofs
                Cns = Cns - (price * unitsofs)
                return amountotal, Cns
            else:
                print("You can't afford that!!")

#By land or sea
def beginjourney(uname):
    waterorland = inputtemplate("\nYou can get to Alexandria by land or by sea. Along the way, you will need to buy food in other countries. If you go by sea, you will not need to make as many stops or buy as much food as you would if you went by land. However, some of your merchandise will run the risk of damage.\n 1. Land\n 2. Sea\n", 0, 2)
    return waterorland

#Last stop in China by water
def nanhal(noic, klis, mrowklis, lreap, leets, ssarb, eman):
    count = 0
    while True:
        if count == 0:
            leavechinamessage = str(f"\nYour barge travels swiftly, it isn't long before you have reached Nanhal, you last stop in China. You are halted by officials asking if you have a seal that permits you to trade with foreigners. Luckily, your father supplied you with one. The officials will also check your stock, when you leave, to tax some of your goods. If it is any consolation, some of this money will go towards the building of roads and the creation of farmland. This is your last stop in China. Before you leave China {eman}, you may wish to stop by the marketplace to stock up on goods and commodities. You may also leave China immediately.\n 1. Marketplace\n 2. Leave China\n 3. Exit\n")
        else:
            leavechinamessage = str(f"\n 1. Marketplace\n 2. Leave China\n 3. Exit\n")
        marketorleave = inputtemplate(leavechinamessage, 0, 3)
        if marketorleave == 1:
            noic, klis, mrowklis, lreap, leets, ssarb = marketplaceChina(noic, klis, mrowklis, lreap, leets, ssarb, eman)
        elif marketorleave == 2:
            if mrowklis > 0:
                print("It looks like someone thought that crime pays. Unfortunately (for you), you have been caught in an attempt to smuggle silkworms to foriengers. You were willing to betray your entire country just to make an extra buck. If this is a surpruise to you, you should have checked the extra information in the marketplace. Tough luck, Goodbye.")
                exit()
            else:
                noic, klis, lreap, leets, ssarb = noic, klis, lreap, leets, ssarb * .9
                noic, klis, lreap, leets, ssarb = int(noic), int(klis), int(lreap), int(leets), int(ssarb)
                return noic, klis, lreap, leets, ssarb
                break
        elif marketorleave == 3:
            exit()
        count = 1

def xian(noi, kli, mrowkli, lrea, leet, ssar, ema):
    count = 0
    while True:
        if count == 0:
            contmessage = str(f"\nTravel by land may be a bit tedious, but you rest easy knowing that you and your possesions are safe. The roads are nice and well constructed, thanks to government funding. Before you continue {ema}, you may wish to stop by the marketplace to stock up on goods and commodities. You may also continue to Lanzhou.\n 1. Marketplace\n 2. Continue\n 3. Exit\n")
        else:
            contmessage = str(f"\n 1. Marketplace\n 2. Continue\n 3. Exit\n")
        marketorcont = inputtemplate(contmessage, 0, 3)
        if marketorcont == 1:
            noi, kli, mrowkli, lrea, leet, ssar = marketplaceChina(noi, kli, mrowkli, lrea, leet, ssar, ema)
        elif marketorcont == 2:
            return noi, kli, mrowkli, lrea, leet, ssar
            break
        elif marketorcont == 3:
            exit()
        count = 1

def lanzhou(no, kl, mrowkl, lre, lee, ssa, em):
    count = 0
    while True:
        if count == 0:
            leavechinalandmessage = str(f"\nYou have reached the edge of China, and will soon journey out through the Great Wall, a morbid reminder of the dangers of the outside world, full of barbarians. Don't worry, you will travel with a platton of loyal guards armed with steel armor, weapons, and repeating crossbows (yes really!!). You are halted by officials asking if you have a seal that permits you to trade with foreigners. Luckily, your father supplied you with one. The officials will also check your stock, when you leave, to tax some of your goods. If it is any consolation, some of this money will go towards the building of roads and the creation of farmland. This is your last stop in China. Before you leave China {em}, you may wish to stop by the marketplace to stock up on goods and commodities. You may also leave China immediately.\n 1. Marketplace\n 2. Leave China\n 3. Exit\n")
        else:
            leavechinalandmessage = str(f"\n 1. Marketplace\n 2. Leave China\n 3. Exit\n")
        marketorleavech = inputtemplate(leavechinalandmessage, 0, 3)
        if marketorleavech == 1:
            no, kl, mrowkl, lre, lee, ssa = marketplaceChina(no, kl, mrowkl, lre, lee, ssa, em)
        elif marketorleavech == 2:
            if mrowkl > 0:
                print("It looks like someone thought that crime pays. Unfortunately (for you), you have been caught in an attempt to smuggle silkworms to foriengers. You were willing to betray your entire country just to make an extra buck. If this is a surpruise to you, you should have checked the extra information in the marketplace. Tough luck, Goodbye.")
                exit()
            else:
                no, kl lre, lee, ssa = no, kl, lre, lee, ssa * .9
                no, kl, mrowkl, lre, lee, ssa = int(no), int(kl), int(lre), int(lee), int(ssa)
                return no, kl, lre, lee, ssa
                break
        elif marketorleavech == 3:
            exit()
        count = 1

def indial(fd, il, rl, lcraft, scraft, me):
    fd, il, rl, lcraft, scraft = miran(fd, il, rl, lcraft, scraft, me)
    ice = 0
    fd, il, rl, lcraft, scraft, ice = purushapura(fd, il, rl, lcraft, scraft, me)
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

def purushapura(foo, sils, pea, stc, brc, moi):
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
def marketinpurushapura( od ,sik, pel, stel, bras, spic, mei):
    while True:
        marketinpurumessage = str(f"Welcome, {mei}, to the market! You have {eatables} food, {thread} units of silk, {shiny} bags of pearls, {sharp} steel products, {ornament} brass products.\n 1. Sell Silk\n 2. Sell Pearls\n 3. Sell Steel Products\n 4. Sell Brass Products\n 5. Buy Spice\n 6. Leave Market\n 7. Advice From Amil Yrneh\n")
        decisioninmarketinpuru = inputtemplate(marketinpurumessage, 0, 6)
        if decisioninmarketinpuru == 1:
            eatables, thread = transinmarketm(eatables, thread, 'units of silk', 175)
        elif decisioninmarketinpuru == 2:
            eatables, shiny = transinmarketm(eatables, shiny, 'bags of pearls', 110)
        elif decisioninmarketinpuru == 3:
            eatables, sharp = transinmarketm(eatables, sharp, 'steel products', 120)
        elif decisioninmarketinpuru == 4:
            eatables, ornament = transinmarketm(eatables, ornament, 'brass products', 65)
        elif decisioninpurushapura == 5:
        elif decisioninmarketinpuru == 6: break
        elif decisioninmarketinpuru == 7:
         print("\nThe value of silk is fairly high here, although it will be highest in Alexandria. I think you shouldn't sell steel, as it is less valuable here thanks to the peace brought by Maurya.\n")
    return eatables, thread, shiny, sharp, ornament

def indias():
    print('indias')

def main():
    wronginputmessage = str('Please type one of the numbers listed.\n')
    beginningcode(wronginputmessage)
    name, coins, sil, silkworm, pearl, steelcraft, brasscraft, answer22ndq = startingpage()
    if answer22ndq == 1:
        coins, sil, silkworm, pearl, steelcraft, brasscraft = marketplaceChina(coins, sil, silkworm, pearl, steelcraft, brasscraft, name)
    elif answer22ndq == 3:
        exit()
    answer23rdq = beginjourney(name)
    if answer23rdq == 1:
        coins, sil, silkworm, pearl, steelcraft, brasscraft = xian(coins, sil, silkworm, pearl, steelcraft, brasscraft, name)
        coins, sil, pearl, steelcraft, brasscraft = lanzhou(coins, sil, silkworm, pearl, steelcraft, brasscraft, name)
        food = 0
        food, sil, pearl, steelcraft, brasscraft, spice = indial(food, sil, pearl, steelcraft, brasscraft, name)
    elif answer23rdq == 2:
        coins, sil, pearl, steelcraft, brasscraft = nanhal(coins, sil, silkworm, pearl, steelcraft, brasscraft, name)
        food = 0

    return

if __name__ == '__main__':
    main()
