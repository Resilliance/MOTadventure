
import time

delay = 0
quit = 0 # Breaks while loop when quit = 1

class player:
    name = ''
    items = ['','','']
    itemCount = 0 # keeps track of how many items player has as an index for the next available slot
    room = 0
    i = 0
    
    # Locates what Room the player is in
    def whereAmI(x):
        print(rooms.room_name[x])
        time.sleep(delay)
    
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
                player.helpMe()
            case "inspectRoom":
                rooms.inspectRoom()
            case "move":
                rooms.movePlayer()
            case "pickUp":
                item.pickUp()
            case "use":
                item.use()
            case "drop":
                item.drop()
            case "whereAmI":
                player.whereAmI(player.room)
                # Figure out why I can't pass player.room into whereAmI()
                # I was using ":" instead of "=" for defining my class variables Oops
            case "quit":
                quit = 1
    
    # Shows player.items[]
    def showInventory():
        for i in range(len(player.items)):
            print(i+1, ")", player.items[i])
    


class item:
    
    # Picks up items from rooms.itemHere[] and transfers to player.items[]
    def pickUp():    
        if rooms.itemHere[player.room] == '':
            print("There is nothing to pick up.")   
            
        elif rooms.itemHere[player.room] != "Lock":
            
            # Add to player's items[]
            player.items[player.itemCount] = rooms.itemHere[player.room]
            print("You have picked up a", rooms.itemHere[player.room])
            player.itemCount += 1
            
            # Remove item from room
            rooms.itemHere[player.room] = ''
            
        else:
            print("You can't pick up the lock")
    
    # Player choose item to use
    def use():
        global quit # Enables change to global quit variable
        
        player.showInventory()
        
        # Redundant code, figure out how to call this dynamically
        itemIndex = input("What item did you want to use?\n") 
        itemIndex = int(itemIndex) 
        
        if player.room == 0 and "Key" == player.items[itemIndex-1]:
            print("You unlocked the door, Congrats!!")
            quit = 1
        else: 
            print("There is nothing to do with the",player.items[itemIndex-1])
        
    
    # Player gets to drop an item in a room
    def drop(): 
        player.showInventory()
        
        # Add back/cancel function
        itemIndex = input("What item did you want to drop?\n") 
        itemIndex = int(itemIndex)
        
        #BUG: if player types in a string instead of 1 , 2 , or 3 for itemIndex program will break
        
        # Update rooms.itemHere wherever player drops it
        rooms.itemHere[player.room] = player.items[itemIndex-1] #BUG: dropping multiple items in one room will overwrite the previously dropped item(s)
        
        if rooms.itemHere[itemIndex-1] != '':
            print("Cannot drop item here, there's already an item here")
            
        else:
            print(player.items[itemIndex-1], "has been dropped.")
            player.items[itemIndex-1] = '' # removes item from player.items
            player.itemCount -= 1 # updates player's total itemCount
        
        
    
    
class rooms:
    room_number = [0,1,2]
    room_name = ['Matrix Exit', 'Corridor', 'Office']
    itemHere = ['Lock', 'Sword', 'Key']
        
    def isDirectionValid(direction):
        
        # Find Optimization to condense this code (if possible)
        
        # room_number = 0 (Cannot move backward)
        if player.room < 1:
            if direction == "backward":
                print("You walk into a cinderblock wall, ouch.")
                return False
            elif direction == "forward":
                print("You walk into a dimly lit room")
                player.room += 1
                return True
        
        # room_number = 1 (Can move forward and backward)
        elif player.room == 1:
            if direction == "backward":
                print("You backtrack into the room with a glistening green light")
                player.room -= 1
                return True
            elif direction == "forward":
                print("You walked into the room with a decayed wooden desk")
                player.room += 1
                return True
            
        # room_number = 2 (Cannot move forward)
        else: # could make this an elif, but we can insinuate that the only other number would be 2
            if direction == "backward":
                print("You walk into a dimly lit room")
                player.room -= 1
                return True
            elif direction == "forward":
                print("You gaze into the alphanumerical green abyss through the room's window.")
                return False
                
    
    def movePlayer():
        # Foreward or Backward
        direction = input("'forward' or 'backward'?\n")
        rooms.isDirectionValid(direction)
        
    
    def inspectRoom():
        # Looks for items in the room
        if rooms.itemHere[player.room] != '':
            print("There is a", rooms.itemHere[player.room],"here.")
        elif rooms.itemHere[player.room] == '':
            print("This room is completely vacant of items.")
    
def intro():
    player.name = input(f'What is your name?\n')
    time.sleep(delay)
    print('We have been waiting for you,',player.name)
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
    

    
intro()
while quit != 1:
    player.makeChoice()
