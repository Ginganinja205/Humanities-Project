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

def Instructions(wronginput):
    while True:
        howtoplay = input("By selecting this you are already on the right track. Your goal is to try and make the character you select as profitable as possible, and my goal is to try to teach you about the economies of Ancient Civilizations. Throughout this interactive teaching program you will be asked to make multiple decisions, some small some large, in order to achieve your goal. Along the way, you may encounter things that you are unfamiliar with, or decisions you feel unable to make. If this happens, there should be an option to give you more information. Select this, read through the given information, and try again. Type the number corresponding to your answer then press 'Enter'. If you still feel confused, or if program isn't functioning properly, please call me (Henry Lima) over, but be merciful; I only had about two weeks to put this together. Thank you. (Press the 'SpaceBar' then 'Enter' to continue.)")
        if howtoplay == ' ':
            beginningcode(wronginput)
            break

def Citations():
    print()

#This function is for the multiple times input will have to be vetted. For second argument put 0 for numbers and anythingelse for text.
def inputtemplate(message, numberortext, numberofoptions, wronginputmssg):
    theinput = input(message)
    if numberortext == 0:
        try:
            thenumberinput = int(theinput)
        except:
            print(wronginputmssg)
        if numberofoptions < thenumberinput or thenumberinput < 1:
            print(wronginputmssg)
        else:
            return numberinput
    else:
        return str(theinput)

def civpicker():
    return

def characterchoice():
    return




def main():
    wronginputmessage = str('Please type one of the numbers listed.\n')
    beginningcode(wronginputmessage)
    thecivpicked = civpicker()
    return

if __name__ == '__main__':
    main()
