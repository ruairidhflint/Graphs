'''
Thoughts:

From the starting point we need to essentially choose a random direction and do a depth traveral
as far as we can. Every room that we enter will mean we need to update the '?' direction from the
previous room as well as it's own.

Any direction that cannot be travered we can mark accordingly.

We could use a BFT to handle some initial issues but I think potentially the whole thing could be done
with just DFT.

We will need to keep track of the previous direction, cardinal value, current room ID etc. 

'''
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"

map_file = "maps/main_maze.txt"
my_file = os.path.join(THIS_FOLDER, map_file)

# Loads the map into a dictionary
room_graph = literal_eval(open(my_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Reverse directions to save logic later
# reverse_directions = {'n': 's', 's': 'n', 'e':'w', 'w':'e'}

# Dictionary for traversal path (could be a set?)
# traversal_path = {}


# Use a stack to begin with, queue later if necessary
# s = Stack()
# Keep track of the last room id
# previous_room = None
# Keep track of the direction we came from
# previous_direction = None


# Whilst the traversal graph is smaller than the room graph itself, we need to keep exploring

    # Get current room the player is in

    # Check if it has been traversed or not
        # If not make a list of the room's exits using getExits()
        # Add room to traversal graph with  the exits the value in a dict
    
    # Check for previous room
        # If there is one, we need to update it's value for the direction we travelled to 
        # current room ID
        # Give the current room's opposite direction value to match
    # Previous room should be updated to the current room

    # Check to see if we can actually go anywhere and if we have tried yet

    # Log which directions we can move
    
    # If we can go nowhere, go back to the previous room and try somewhere else.


traversalPath = []
opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
rooms = {}
visited = set()



















# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
