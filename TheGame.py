#Opening Screen Credits and Stuff Here
def beginningcode(wronginputmssg):
    while True:
        playorexit = input("Welcome Participant\n Please type '1' to start, '2' to exit, '3' for How To Play, or '4' for credits. Press 'Enter' when you have selected your choice.\n 1. Start\n 2. Exit\n 3. How To Play\n 4. Credits/Citations\n")
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
        howtoplay = input("\nBy selecting this you are already on the right track. Your goal is to try and make the character you select as profitable as possible, and my goal is to try to teach you about the economies of Ancient Civilizations. Throughout this interactive teaching program you will be asked to make multiple decisions, some small some large, in order to achieve your goal. Along the way, you may encounter things that you are unfamiliar with, or decisions you feel unable to make. If this happens, there should be an option to give you more information. Select this, read through the given information, and try again. (DISCLAIMER: Some elements of this game are ficticious and non-factual. Most inconsistencies will be concerning chronology) Type the number corresponding to your answer then press 'Enter'. If you still have problems, please call me (Henry Lima) over. Thank you. (Press the 'SpaceBar' then 'Enter' to continue.)")
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
        if numberofoptions < thenumberinput or thenumberinput < 1:
            print(str('Please type one of the numbers listed.\n'))
        else:
            return thenumberinput
    else:
        return str(theinput)

#Username, Establishes Base Products Currency, Leads to Market or Cont.s to Journey
def startingpage():
    namemssg = str("\nHello user! You have been raised as a merchant in Luoyang, a town in Ancient China (for the intent of this game Ancient refers to a period from 400 BC to 1 BC). Your father has recently decided that it is time for you to attempt a practical execution of your knowledge. You will journey to Alexandria, Egypt with a small company of guards and servants to look after you and your wealth. Your scholar Amil Yrneh will go with you and act as guide. At the start of your journey, you will take some of your father's money and buy some goods and commodities to trade with along the way. China was one of the first nations to have government minted coinage, and this use of official currency bolstered their economy and created growth in the middle class. Your father gives you your spending money in the form of this coinage. However, before we can continue please type your name:  \n")
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
            print(" 3. Steel Products - China was also amongst the first to smelt iron into steel. Steel is much stronger than iron and is ideal for tools of war. Peaceful foreigners will not want to pay such high prices for weaponry even if its are superior to their current stock. However, cities and towns with a strong military presence will definitely snap them up.\n 4. Brass Products - Brass is an alloy of copper, zinc, and lead, all of which China has large quantities of. It is mostly used for ornamentation, and it is a nice fallback to trade with in foreign nations if you want to save other products for later.\n 5. Food - In China, you will never go hungry. China has no shortage of food, due to their advanced farming techniques. This includes mixed stock rearing (a technique involving raising multiple agricultural lifeforms to increase efficiency), and puddling (tiered pools used to keep rice hydrated). However, in other civilizations you will want to buy food (to survive).\n\n")
        elif cmarketopening == 7: break
        elif cmarketopening == 8:
            exit()

#Math For Buying
def markettrans(product, price, amountotal, Cns):
    while True:
        unitsofs = inputtemplate(f"How many {product} would you like to buy? You may purchase up to 100 units of something at a time. If you wish to exit, buy 101 units (this is equivalent to buying 0 units). The price per unit is {price} coins.\n", 0, 101)
        if unitsofs == 101: break
        elif Cns >= price * unitsofs:
                amountotal = amountotal + unitsofs
                Cns = Cns - (price * unitsofs)
                return amountotal, Cns
        else:
            print("You can't afford that!!")

def beginjourney(uname):
    inputtemplate()

def main():
    wronginputmessage = str('Please type one of the numbers listed.\n')
    beginningcode(wronginputmessage)
    name, coins, sil, silkworm, pearl, steelcraft, brasscraft, answer22ndq = startingpage()
    if answer22ndq == 1:
        coins, sil, silkworm, pearl, steelcraft, brasscraft = marketplaceChina(coins, sil, silkworm, pearl, steelcraft, brasscraft, name)
    elif answer22ndq == 3:
        exit()
    answer23rdq = beginjourney(name)
    return

if __name__ == '__main__':
    main()
