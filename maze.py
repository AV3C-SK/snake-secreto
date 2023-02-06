import os
import random
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 15
my_position = [6, 3]
tail_length = 0
tail = []
MAP_OBJECTS = []
end_game = False
died = False

# Draw Map

while not end_game:
    os.system("cls")
    while len(MAP_OBJECTS) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGHT)]

        if new_position not in MAP_OBJECTS and new_position != my_position:
            MAP_OBJECTS.append(new_position)

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None

            for MAP_OBJECT in MAP_OBJECTS:
                if MAP_OBJECT[POS_X] == coordinate_x and MAP_OBJECT[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = MAP_OBJECT

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    MAP_OBJECTS.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    print("Haz muerto!")
                    end_game = True
            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")



    direction = readchar.readchar()

    if direction == "z":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= MAP_HEIGHT
    elif direction == "q":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] -= 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position[POS_X] += 1
        my_position[POS_X] %= MAP_WIDTH
    elif direction == "a":
        end_game = True

    os.system("csl")
