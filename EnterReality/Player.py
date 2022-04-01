from operator import index
import Room


class player:
    name = ''
    __items = []
    itemCount = 0 # keeps track of how many items player has as an index for the next available slot
    __room = 0
    i = 0
    
    # Locates what Room the player is in
    def whereAmI(x):
        print(Room.rooms.room_name[x])
        
    
    # Shows player.items[]
    def showInventory():
        if not player.__items:
            print("I don't have anything.")
        else:
            for i in range(len(player.__items)):
                print(i+1, ")", player.__items[i])

    def playerInventory():
        inventory = player.__items
        return inventory
    
    def appendPlayerInventory(item):
        player.__items.append(item)
        #print(player.__items)
        pass

    def popPlayerInventory(index):
        player.__items.pop(index)
        #print(player.__items)
        pass

    def playerRoom():
        room = player.__room
        return room

    def mathPlayerRoom(num):
        player.__room = player.__room + num