import random
rannum = random.randint(1,100)
correct = False
def ask():
    global correct
    global rannum
    while correct == False:
        try:
            ansr = input("What number do you want to try: ")
            ansr = int(ansr)
            if ansr == rannum:
                print("You Win!")
                correct = True
            elif ansr > rannum:
                print("Lower!")
                ask()
            elif ansr < rannum:
                print("Higher")
                ask()
        except:
            print("Error Try agin")
            ask()
ask()