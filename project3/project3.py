

#this is my function used to start the game
def start():
    print("You awake in a forest at dawn. You do no know how you got here.")
    print("You think you can hear a river flowing to your left, but there is a cave off in the distance. Which way do you go?")
    #take user input and convert to lowercase (that way they can use whatever case they want in their input)
    answer = input("Cave or River: ").lower()
    # if the word "river" is equal to the users answer, it sends them on to the "river" function. The sting comparison == is used throughout my script.
    if "river" == answer:
        #sends the user to the river function/section of the game
        river()
    elif "cave" == answer:
        #sends the user to the cave entrance function/part of the game
        cave_entrance()
    else:
        #handle a mistype, and restart the game
        print("I didn't understand that. Try again.")
        print()
        start()

#this is the function I call when the game ends/the player dies. The 'reason' argument is substituted with a different phrase depending on when the player dies.
def game_over(reason):
    #print the reason for the game ending
    print(reason)
    print()
    # notice the .lower() method that changes the answer to lowercase. I use this for all user input
    again = input("Play Again (yes or no)? ").lower()
    if "yes" == again:
        # if they want to play again it starts the game over
        start()
    else:
        # if the user does not type yes, I end the game
        print("Either you typed no or you mistyped. You can run the script again if you want to play more! Exiting...")
        exit()

# this function is called when the player picks the path in my game that results in a win
def win():
    print("You win! You found the path in my game that lets you live. Thanks for playing!")
    game_over("The game is over")

#This function is called when the player chooses to head toward the cave
def cave_entrance():
    print()
    print("You cautiously head towards the cave, taking in your surroundings.")
    print("You arrive at the cave entrance, but the cave is dark and cold. You hear some deep animal like growls.")
    print("You begin to get second thoughts.")
    decision = input("Do you still want to enter the cave? (yes or no): ").lower()
    if "yes" == decision:
        inner_cave()

    elif "no" == decision:
        print("You changed you mind and you head towards the river instead")
        river()
    else:
        print("You may have mistyped, try again.")
        print()
        cave_entrance()

# this function is called when the player decides to enter the cave
def inner_cave():
    print()
    print("You enter the cave, but it is very dark and you cannot see very well.")
    print("Suddenly you hear an animal of some kind charging toward you. What will you do?")
    fight = input("Will you stand your ground or will you try to run? (stay or run): ").lower()
    if "stay" == fight:
        print()
        print("You stand your ground. The animal charges right into you and knocks you over.")
        print("The animal stands over you. Up close, you realize it is a bear with sharp teeth and claws. It lunges at you before everything goes black")
        game_over("The bear killed you. Better luck next time.")
    elif "run" == fight:
        print()
        print("You run for your life. You stumble over small rocks as you make your way to the cave entrance.")
        print("You make it out of the cave, but the bear follows. The bear cuts you down and drags your corpse back into its den.")
        game_over("You died, game over.")
    else:
        print("You may have mistyped, try again.")
        print()
        inner_cave()
# this function is called when the player heads toward the river
def river():
    print()
    print("As you head towards the river, the sounds of flowing water grow increasingly louder.")
    print("When you arrive at the river, you spot a few sickly looking animals drinking the water. Your presence scares them away.")
    drink = input("You find that you are thirsty and could use some water. Do you take a drink from the river? (yes or no): ").lower()

    if "yes" == drink:
        print()
        print("You take a few drinks of water from the river. The water tastes awful.")
        poison()
    elif "no" == drink:
        print()
        print("You don't drink any water and you begin to walk down the shore of the river.")
        river_attack()
    else:
        print("You may have mistyped, try again.")
        river()
# thic function is called when the player drinks the 'bad' water 
def poison():
    print()
    print("You begin to feel unwell. You begin to realize that the water was not safe to drink.")
    print("You start feeling lightheaded and you blackout")
    game_over("You died from drinking dirty water")
# this function is called when the player doesn't drink the water and continues down the river
def river_attack():
    print("As you make your way down the shore of the river, you are ambushed by a monster.")
    print("The monster has huge claws and fangs. You fear for your life.")
    monster_fight = input("Do you stand and fight or do you flee for your life? (fight or flee): ").lower()
    if "fight" == monster_fight:
        print()
        print("You stand your ground and fight the monster. The monster lunges at you and you narrowly dodge the attack.")
        print("The monster trips and falls in the river. It yells out as it melts into the water, dissolving away.")
        print("It appears that you won the fight. You run away from the scene until you find a small village. The people there are kind and shelter you for the night.")
        # players who make it this far win the gme and the win() function is called
        win()
    elif "flee" == monster_fight:
        print()
        print("You run from the monster, but he is faster than you. He begins to catch you, but suddenly two warriors appear and take the monster down.")
        print("You travel with the warriors until you arrive at their village. The people there are kind and shelter you for the night.")
        # players who make it this far win the gme and the win() function is called
        win()
    else:
        print("You may have mistyped, try again.")
        river_attack()
# this starts the game
start()
