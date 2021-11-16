

#this is my function used to start the game
def start():
    print("You awake in a forest at dawn. You do no know how you got here")
    print("You think you can hear a river flowing to your left, but there is a cave off in the distance. Which way do you go?")

    answer = input("Cave or River:").lower()

    if "river" in answer:
        river()
    elif "cave" in answer:
        cave()
    else:
        game_over("I didn't understand that. Try again.")


def game_over(reason):
    print(reason)
    again = input("Play Again (y or n)?").lower()
    if "y" in again:
        start()
    else:
        print("Either you typed n/N or you mistyped. You can run the script again if you want to play more!")
        exit()

def cave():
    pass

def river():
    pass

start()
