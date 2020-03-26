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
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"

# map_file = "maps/main_maze.txt"
my_file = os.path.join(THIS_FOLDER, map_file)

# Loads the map into a dictionary
room_graph = literal_eval(open(my_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Traversal path as list not DICT
traversalPath = []
opposite_directions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# DICT of rooms instead of Traversal path
rooms = {}
# As in guided lecture, a visited set
visited = set()

# Create a depth first search - takes in current room, the direction we came from and the previous room's ID
def depth_first_r(current_room, prev_dir=None, prev_room_id=None):
    # add current room's id tov visited set
    visited.add(current_room.id)
    # set the temp room dict with all the cardinal values set to ?
    room = {'n': '?', 'e': '?', 's': '?', 'w': '?'}
    # Loop through the get_exits() functionality and check if any exist
    exits = current_room.get_exits()

# if the current room id is not in the room dict

# set the current room's id to the room dict

# if there is a previous direction

# set the oppsoite direction and current direction to match between rooms
# Loop through the rooms that are abilable and try to travel to any with a ?


# Breadth first search on a current room
def breath_first_search(current_rooms_id):
    pass
# Create quite
# Add list with current room is
# Make temp set
# whilst queue is larger than zero
# dequeue to temp var
# current id is the last value
# if that is is not in visited
# make a new list of the room's values
# If any of the values are ? or the length's or the room graph match the visited set
# return that path
# add to the rooms visited the current room id
# loop through the the rooms held in the values list
# go through the motions of adding a new list that is a copy and enqueueing

# FUnction to bring it all together
def traverse_rooms():
    pass
# whilst the length of the room graph is not equal to the length of the visited,
# DO a depth first search starting at the current room.
# The path is the same except a breadth first search
# Loop through every single room in the path, adding the relevant valyes to the traversal path


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
