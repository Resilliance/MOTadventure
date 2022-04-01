import Item
import Player

class rooms:
    _room_number = [0,1,2]
    room_name = ['Matrix Exit', 'Corridor', 'Office']
    __itemHere = [['Lock'], ['Sword'], ['Key']]
        
    def isDirectionValid(direction):
        # Consider using nested dictionary
        
        # room_number = 0 (Cannot move backward)
        if Player.player.playerRoom() < 1:
            if direction == "backward":
                print("You walk into a cinderblock wall, ouch.")
                return False
            elif direction == "forward":
                print("You walk into a dimly lit room")
                Player.player.mathPlayerRoom(1)
                return True
        
        # room_number = 1 (Can move forward and backward)
        elif Player.player.playerRoom() == 1:
            if direction == "backward":
                print("You backtrack into the room with a glistening green light")
                Player.player.mathPlayerRoom(-1)
                return True
            elif direction == "forward":
                print("You walked into the room with a decayed wooden desk")
                Player.player.mathPlayerRoom(1)
                return True
            
        # room_number = 2 (Cannot move forward)
        else: # could make this an elif, but we can insinuate that the only other number would be 2
            if direction == "backward":
                print("You walk into a dimly lit room")
                Player.player.mathPlayerRoom(-1)
                return True
            elif direction == "forward":
                print("You gaze into the alphanumerical green abyss through the room's window.")
                return False
                
    
    def movePlayer():
        # Foreward or Backward
        direction = input("'forward' or 'backward'?\n")
        rooms.isDirectionValid(direction)
        
    
    def inspectRoom(): 
        itemsInHere = rooms.numberOfRoomItems()

        # Tells player what is in the room
        if itemsInHere == 3:
            print("There is a",rooms.__itemHere[Player.player.playerRoom()][0],rooms.__itemHere[Player.player.playerRoom()][1],"and a",rooms.__itemHere[Player.player.playerRoom()][2])
        elif itemsInHere == 2:
            print("There is a",rooms.__itemHere[Player.player.playerRoom()][0],"and a",rooms.__itemHere[Player.player.playerRoom()][1])
        elif itemsInHere == 1:
            print("There is a",rooms.__itemHere[Player.player.playerRoom()][0],"in this room")
        else:
            print("There's nothing in here.")

    def numberOfRoomItems():
        itemsIn = 0

        if not rooms.__itemHere[Player.player.playerRoom()]:
            return itemsIn

        # Looks for items in the room
        else:
            itemsIn += len(rooms.__itemHere[Player.player.playerRoom()])
            return itemsIn
    
    # Methods to Access and Update "private" itemHere

    def accessItemHere():
        publicItemHere = rooms.__itemHere
        return publicItemHere

    def appendItemHere(room,index):
        rooms.__itemHere[room].append(index)
        #print(rooms.__itemHere)

    def popItemHere(room, index):
        rooms.__itemHere[room].pop(index)
        #print(rooms.__itemHere)