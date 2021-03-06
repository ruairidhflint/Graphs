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

    if 'n' not in exits:
        room['n'] = None
    if 'e' not in exits:
        room['e'] = None
    if 's' not in exits:
        room['s'] = None
    if 'w' not in exits:
        room['w'] = None

# if the current room id is not in the room dict
    if not current_room.id in rooms.keys():
        # set the current room's id to the room dict
        rooms[current_room.id] = room
    # if there is a previous direction
    if prev_dir:
        # set the oppsoite direction and current direction to match between rooms
        rooms[current_room.id][
            opposite_directions[prev_dir]] = prev_room_id
    # Loop through the rooms that are abilable and try to travel to any with a ?
    for next_room in rooms[current_room.id]:
        if rooms[current_room.id][next_room] == '?':
            # move through the room if it is yet unexplored
            player.travel(next_room)
            # Update the id
            rooms[current_room.id][next_room] = player.current_room.id
            # Add to the traversal path
            traversalPath.append(next_room)
            # Recursively run the function again on the new room
            depth_first_r(player.current_room, next_room, current_room.id)

            return

# Breadth first search on a current room


def breath_first_search(current_rooms_id):
    # Create queue
    q = Queue()
    # Add list with current room is
    q.enqueue([current_rooms_id])
    # Make temp set
    visited_2 = set()
    # whilst queue is larger than zero
    while q.size() > 0:
        # dequeue to temp var
        temp_var_path = q.dequeue()
        # current id is the last value
        last_value = temp_var_path[-1]
        # if that is is not in visited
        if last_value not in visited_2:
            # make a new list of the room's values
            values = list(rooms[last_value].values())
            # If any of the values are ? or the length's or the room graph match the visited set
            if '?' in values or len(room_graph) == len(visited):
                # return that path
                return temp_var_path
            # a dd to the rooms visited the current room id
            visited_2.add(last_value)
            # loop through the the rooms held in the values list
            for next_room in values:
                # go through the motions of adding a new list that is a copy and enqueueing
                if (next_room == 0
                        or next_room) and next_room not in visited_2:
                    new_path = list(temp_var_path)
                    new_path.append(next_room)
                    q.enqueue(new_path)

# FUnction to bring it all together


def traverse_rooms():
    # whilst the length of the room graph is not equal to the length of the visited
    while len(room_graph) != len(visited):
        # DO a depth first search starting at the current room.
        depth_first_r(player.current_room)
        # The path is the same except a breadth first search
        path = breath_first_search(player.current_room.id)
        # Loop through every single room in the path, adding the relevant valyes to the traversal path
        for index in range(0, len(path) - 1):
            # Loop through every single room in the path, adding the relevant valyes to the traversal path
            currentroom_ID = path[index]
            next_room_id = path[index + 1]
            current_room = rooms[currentroom_ID]
            keys = list(current_room.keys())
            values = list(current_room.values())
            cardinal = keys[values.index(next_room_id)]
            player.travel(cardinal)
            traversalPath.append(cardinal)

traverse_rooms()


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
