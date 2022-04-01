import Item
import Room
import Player
import time

delay = 1.5
quit = 0 # Breaks while loop when quit = 1

class main:


    # Shows player all of the commands
    def helpMe():
        print('--help: Lists all commands')
        print('--inspectRoom: Find what item is inside the room')
        print('--move: Allows you to move forward or backward')
        print('--pickUp: Pick up an item inside the room you are in')
        print('--use: Interact an item in your inventory with the environment')
        print('--drop: Removes item from inventory and drops into the room you are in')
        print('--whereAmI: Find out what room you are in')
        print('--quit: Exit Game')
    
    # Allows player to choose what to do
    def makeChoice():
        global quit
        choice = input("What should I do?\n")
        match choice:
            case "help":
                main.helpMe()
            case "inspectRoom":
                Room.rooms.inspectRoom()
            case "move":
                Room.rooms.movePlayer()
            case "pickUp":
                Item.item.pickUp()
            case "use":
                Item.item.use()
            case "drop":
                Item.item.drop()
            case "whereAmI":
                Player.player.whereAmI(Player.player.playerRoom())
                # Figure out why I can't pass player.room into whereAmI()
                # I was using ":" instead of "=" for defining my class variables Oops
            case "a":
                Room.rooms.accessItemHere()
            case "quit":
                quit = 1
                print("Thanks for playing!!")

    def intro():
        Player.player.name = input(f'What is your name?\n')
        time.sleep(delay)
        print('We have been waiting for you,',Player.player.name)
        time.sleep(delay)
        print(f'You are the chosen one.')
        time.sleep(delay)
        print(f'I know this is sudden, but you NEED to trust me...')
        time.sleep(delay*1.5)
        print(f'You are inside the Matrix right now')
        time.sleep(delay)
        print(f"There's a key inside, one of the rooms.")
        time.sleep(delay)
        print(f"Find your way out, and we can talk more...")
        time.sleep(delay*2)

    def end():
        print('You made it.')
        time.sleep(delay)
        print('Good job on getting here,',Player.player.name)
        time.sleep(delay)
        print("We have to close this window now, but we'll be in contact soon.")
        time.sleep(delay*2)

    def checkQuit():
        global quit
        quit = Item.quit
    

# Game Loop
main.intro()
while quit != 1:
    main.makeChoice()
    main.checkQuit()

main.end()