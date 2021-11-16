

#this is my function used to start the game
def start():
    print("You awake in a forest at dawn. You do no know how you got here.")
    print("You think you can hear a river flowing to your left, but there is a cave off in the distance. Which way do you go?")
    #take user input and convert to lowercase (that way they can use whatever case they want in their input)
    answer = input("Cave or River:").lower()
    if "river" in answer:
        #send the user to the river function/section of the game
        river()
    elif "cave" in answer:
        #send the user to the cave entrance function/part of the game
        cave_entrance()
    else:
        #handle a mistype, and restart the game
        print("I didn't understand that. Try again.")
        print()
        start()

#this is the function I call when the game ends/the player dies. The 'reason' argument is substitued with a different phrase depending on when the player dies.
def game_over(reason):
    #print the reason for the game ending
    print(reason)
    again = input("Play Again (y or n)?").lower()
    if "y" in again:
        start()
    else:
        # if the user does not type Y or y, I end the game
        print("Either you typed n/N or you mistyped. You can run the script again if you want to play more!")
        exit()
#This function is called when the player chooses to head toward the cave
def cave_entrance():
    print()
    print("You cautiously head towards the cave, taking in your surroundings.")
    print("You arrive at the cave entrance, but the cave is dark and cold. You hear some deep animal like growls.")
    print("You begin to get second thoughts.")
    decision = input("Do you still want to enter the cave? (y or n)").lower()
    if "y" in decision:
        inner_cave()

    elif "n" in decision:
        print("You changed you mind and you head towards the river instead")
        river()
    else:
        print("You may have mistyped, try again.")
        print()
        cave_entrance()

def inner_cave():
    print("You enter the cave, but it is very dark and you cannot see very well.")
    print("Suddenly you hear an animal of some kind charging toward you. What will you do?")
    fight = input("Will you stand your ground or will you try to run? (stay or run):")
    if "stay" in fight:
        print("You stand your ground. The animal charges right into you and knocks you over.")
        print("The animal stands over you. Up close, you realize it is a bear with sharp teeth and claws. It lunges at you before everything goes black")
        game_over("The bear killed you. Better luck next time.")
    elif "run" in fight:
        print("You run for your life. You stumble over small rocks as you make your way to the cave entrance.")
        print(" You make it out of the cave, but the bear follows. The bear cuts you down and drags your corpse back into its den.")
        game_over("You died, game over.")
    else:
        print("You may have mistyped, try again.")
        print()
        inner_cave()

def river():
    print("The river dlc is not ready yet")
    exit()

start()
