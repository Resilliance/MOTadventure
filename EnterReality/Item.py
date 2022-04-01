import Room
import Player

quit = 0

class item:
    # Picks up items from rooms.itemHere[] and transfers to player.items[]
    def pickUp():
        numOfItems = Room.rooms.numberOfRoomItems() 

        if numOfItems > 1:

            # Lists items in the room
            for i in range(len(Room.rooms.accessItemHere()[Player.player.playerRoom()])):
                print(i+1,")",Room.rooms.accessItemHere()[Player.player.playerRoom()][i])

            # Player chooses which item to pick up
            itemChoice = input("Choose item number: ")
            if itemChoice.isdigit() == True:

                
                intItemChoice = int(itemChoice)
                if intItemChoice > 0 and intItemChoice-1 < numOfItems and Room.rooms.accessItemHere()[Player.player.playerRoom()][intItemChoice-1] != 'Lock':
                    # Adds item to inventory
                    Player.player.appendPlayerInventory(Room.rooms.accessItemHere()[Player.player.playerRoom()][intItemChoice-1])
                    Player.player.itemCount += 1
                    print("You picked up the",Room.rooms.accessItemHere()[Player.player.playerRoom()][intItemChoice-1])

                    # Removes item from room inventory
                    Room.rooms.popItemHere(Player.player.playerRoom(), intItemChoice-1)

                # Denies player from picking up the Lock
                elif intItemChoice > 0 and intItemChoice-1 < numOfItems and Room.rooms.accessItemHere()[Player.player.playerRoom()][intItemChoice-1] == 'Lock':
                    print("You cannot pick up the Lock.")
                else:
                    print("Invalid Item")


            # Player chooses an invalid choice
            else:
                print("Not a valid item choice")



        elif numOfItems == 1 and Room.rooms.accessItemHere()[Player.player.playerRoom()][0] != 'Lock':
                # Adds item to inventory
                Player.player.appendPlayerInventory(Room.rooms.accessItemHere()[Player.player.playerRoom()][0])
                Player.player.itemCount += 1
                print("You picked up the",Room.rooms.accessItemHere()[Player.player.playerRoom()][0])

                # Removes item from room inventory
                Room.rooms.popItemHere(Player.player.playerRoom(), 0)

        elif numOfItems == 1 and Room.rooms.accessItemHere()[Player.player.playerRoom()][0] == 'Lock':
            print("You cannot pick up the Lock.")

        else:
            print("There is nothing to pick up in here.")
    
    # Player choose item to use
    def use():
        
        if not Player.player.playerInventory():
            print("I can't use what I don't have.")

        else:
            Player.player.showInventory()
            itemIndex = input("What item did you want to use?\n")
            if itemIndex.isdigit() == True:
                intItemIndex = int(itemIndex)

                if intItemIndex-1 < Player.player.itemCount and intItemIndex > 0 and Player.player.playerRoom() == 0 and "Key" == Player.player.playerInventory()[intItemIndex-1]:
                    print("You unlocked the door, Congrats!!")
                    global quit
                    quit = 1

                elif intItemIndex > 0 and intItemIndex-1 < Player.player.itemCount:
                    print("I can't use the",Player.player.playerInventory()[intItemIndex-1],"here.")
                else: 
                    print("Invalid item choice")
            else:
                print("What is that? I don't have that")
    
    # Player gets to drop an item in a room
    def drop(): 
        roomItems = Room.rooms.numberOfRoomItems()
        
        if not Player.player.playerInventory():
            print("I don't have anything.")

        else: 
            Player.player.showInventory()
            itemIndex = input("What item did you want to drop? (Choose number)\n") 
            if itemIndex.isdigit() == True:
                
                intItemIndex = int(itemIndex)
                # Update Room.rooms.itemHere wherever player drops it
                if intItemIndex > 0 and intItemIndex-1 < Player.player.itemCount:
                    # Drops players item into room
                    Room.rooms.appendItemHere(Player.player.playerRoom(),Player.player.playerInventory()[intItemIndex-1])
                    print("You dropped the",Player.player.playerInventory()[Player.player.itemCount-1])

                    # Remove item from player inventory
                    Player.player.popPlayerInventory(intItemIndex-1)
                    Player.player.itemCount -= 1
                    
                else:
                    print("Invalid item choice.")
        
                
       