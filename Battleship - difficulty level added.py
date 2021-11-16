#Definition of the first variable, that stores enemy ships positions and matches them with user input
def missile_launch(a, b):
    if a == 1:
        if b == 1:
            c = b + 24
        elif b == 2:
            c = b + 25
        elif b == 3:
            c = b + 26
        elif b == 4:
            c = b + 27
        elif b == 5:
            c = b + 28
        elif b == 6:
            c = b + 29
        elif b == 7:
            c = b + 30
        elif b == 8:
            c = b + 31
        elif b == 9:
            c = b + 32
    elif a == 2:
        if b == 1:
            c = b + 47
        elif b == 2:
            c = b + 48
        elif b == 3:
            c = b + 49
        elif b == 4:
            c = b + 50
        elif b == 5:
            c = b + 51
        elif b == 6:
            c = b + 52
        elif b == 7:
            c = b + 53
        elif b == 8:
            c = b + 54
        elif b == 9:
            c = b + 55
    elif a == 3:
        if b == 1:
            c = b + 70
        elif b == 2:
            c = b + 71
        elif b == 3:
            c = b + 72
        elif b == 4:
            c = b + 73
        elif b == 5:
            c = b + 74
        elif b == 6:
            c = b + 75
        elif b == 7:
            c = b + 76
        elif b == 8:
            c = b + 77
        elif b == 9:
            c = b + 78
    elif a == 4:
        if b == 1:
            c = b + 93
        elif b == 2:
            c = b + 94
        elif b == 3:
            c = b + 95
        elif b == 4:
            c = b + 96
        elif b == 5:
            c = b + 97
        elif b == 6:
            c = b + 98
        elif b == 7:
            c = b + 99
        elif b == 8:
            c = b + 100
        elif b == 9:
            c = b + 101
    elif a == 5:
        if b == 1:
            c = b + 116
        elif b == 2:
            c = b + 117
        elif b == 3:
            c = b + 118
        elif b == 4:
            c = b + 119
        elif b == 5:
            c = b + 120
        elif b == 6:
            c = b + 121
        elif b == 7:
            c = b + 122
        elif b == 8:
            c = b + 123
        elif b == 9:
            c = b + 124
    elif a == 6:
        if b == 1:
            c = b + 139
        elif b == 2:
            c = b + 140
        elif b == 3:
            c = b + 141
        elif b == 4:
            c = b + 142
        elif b == 5:
            c = b + 143
        elif b == 6:
            c = b + 144
        elif b == 7:
            c = b + 145
        elif b == 8:
            c = b + 146
        elif b == 9:
            c = b + 147
    elif a == 7:
        if b == 1:
            c = b + 162
        elif b == 2:
            c = b + 163
        elif b == 3:
            c = b + 164
        elif b == 4:
            c = b + 165
        elif b == 5:
            c = b + 166
        elif b == 6:
            c = b + 167
        elif b == 7:
            c = b + 168
        elif b == 8:
            c = b + 169
        elif b == 9:
            c = b + 170
    elif a == 8:
        if b == 1:
            c = b + 185
        elif b == 2:
            c = b + 186
        elif b == 3:
            c = b + 187
        elif b == 4:
            c = b + 188
        elif b == 5:
            c = b + 189
        elif b == 6:
            c = b + 190
        elif b == 7:
            c = b + 191
        elif b == 8:
            c = b + 192
        elif b == 9:
            c = b + 193
    elif a == 9:
        if b == 1:
            c = b + 208
        elif b == 2:
            c = b + 209
        elif b == 3:
            c = b + 210
        elif b == 4:
            c = b + 211
        elif b == 5:
            c = b + 212
        elif b == 6:
            c = b + 213
        elif b == 7:
            c = b + 214
        elif b == 8:
            c = b + 215
        elif b == 9:
            c = b + 216
    else:
        c = 'Invalid input'
    return c

#definition of the second function, that explains the rule of the game
def game_rules():
    print('-' * 20)
    print('It is a version of classic game called "Battleship".')
    print('Your task is to find and sink all enemy ships, located somewhere on the map.')
    print('The map consists of 9 rows and 9 columns of "+" signs. Each "+" is a place where a part of enemy ship can be located.')
    print('You need to choose a position of a specific "+" and type its row (horizontal) and column (vertical).')
    print('If you miss, you will get a "Miss!" message, and the position you aimed for will turn from "+" to "x".')
    print('If you hit the target, you will get "Hit!" message, and the part of the ship you hit will turn from "+" to "O".')
    print('There are 3 ships: 2 destroyer-class ships each of 3 signs long (O O O), and 1 cruiser-class ship of 4 symbols long (O O O O).')
    print('You need to hit all parts of the ship to sink it. When there are no more ships on the map, you will get a winning notification.')
    print('You have limited amount of shots to destroy all the enemy ships. There are 4 difficulty levels for this game - easy, medium, hard and crazy.')
    print('If you choose "easy", you get 50 shots. It is 30 shots for "medium", 20 shots for "hard" and 10 shots for "crazy".')
    print('"Crazy" difficulty is special. If you hit any part of any ship, you will  get 2 additional shots for that')
    print("If you couldn't destroy all the ships with given number of shots, you lose.")
    print('If you want to read the rules once more, just type 0 in both row and column input field again.')
    print('Good luck, captain!')
    print('-' * 20)

#developing a map for the game
map = '   1 2 3 4 5 6 7 8 9 \n 1|+ + + + + + + + +| \n 2|+ + + + + + + + +| \n 3|+ + + + + + + + +| \n 4|+ + + + + + + + +| \n 5|+ + + + + + + + +| \n 6|+ + + + + + + + +| \n 7|+ + + + + + + + +| \n 8|+ + + + + + + + +| \n 9|+ + + + + + + + +|'

#randomizing the ship locations on the map
import random
ship_locations = [25, 27, 29, 31, 33, 35, 48, 50, 52, 54, 56, 58, 71, 73, 75, 77, 79, 81, 94, 96, 98, 100, 102, 104, 117, 119, 121, 123, 125, 127, 140, 142, 144, 146, 148, 150, 163, 165, 167, 169, 171, 173, 186, 188, 190, 192, 194, 196, 209, 211, 213, 215, 217, 219]
s_1 = random.choice(ship_locations)
ship_1 = s_1, s_1 + 2, s_1 + 4
s_2 = random.choice(ship_locations)
ship_2 = s_2, s_2 + 2, s_2 + 4, s_2 +6 
s_3 = random.choice(ship_locations)
ship_3 = s_3, s_3 + 2, s_3 + 4
while ship_1[0] == ship_2[0] or ship_1[0] == ship_2[1] or ship_1[0] == ship_2[2] or ship_1[0] == ship_2[3] or ship_1[0] == ship_3[0] or ship_1[0] == ship_3[1] or ship_1[0] == ship_3[2] or ship_2[0] == ship_3[0] or ship_2[0] == ship_3[1] or ship_2[0] == ship_3[2] or ship_1[1] == ship_2[0] or ship_1[1] == ship_2[1] or ship_1[1] == ship_2[2] or ship_1[1] == ship_2[3] or ship_1[1] == ship_3[0] or ship_1[1] == ship_3[1] or ship_1[1] == ship_3[2] or ship_2[1] == ship_3[0] or ship_2[1] == ship_3[1] or ship_2[1] == ship_3[2] or ship_1[2] == ship_2[0] or ship_1[2] == ship_2[1] or ship_1[2] == ship_2[2] or ship_1[2] == ship_2[3] or ship_1[2] == ship_3[0] or ship_1[2] == ship_3[1] or ship_1[2] == ship_3[2] or ship_2[2] == ship_3[0] or ship_2[2] == ship_3[1] or ship_2[2] == ship_3[2]: 
    s_1 = random.choice(ship_locations)
    ship_1 = s_1, s_1 + 2, s_1 + 4
    s_2 = random.choice(ship_locations)
    ship_2 = s_2, s_2 +2, s_2 + 4, s_2 + 6
    
#Building the introduction for the user
print("Hello, Player1! Let's get your name and start playing, shall we?")
user_name = input('How should I call you? ')
print("Welcome to the 'Battleship',", user_name + '!')
print("The game starts now! Print the assumed row and column of the enemy ship, or ask for the rules first!")
dif_level = input("Print desired difficulty level: easy, medium, hard, crazy: ")

#Defining number of attempts and difficulty level
dif_level_case = str(dif_level)
dif_level_case = dif_level_case.lower()
if dif_level_case == 'easy':
    shots = 50
elif dif_level_case == 'medium':
    shots = 30
elif dif_level_case == 'hard':
    shots = 20
elif dif_level_case == 'crazy':
    shots = 10
else:
    print('Please type only one of 4 for the difficulty level: easy, medium, hard, or crazy')
    quit()
print('You have', shots, 'shots left to sink all the ships')
print(map)

#developing the main loop that checks user input with the position of the ships
while map.count('O'[:]) != 10:
    row = input('Enter a row number or type 0 to see the rules: ')
    col = input('Enter a column number or type 0 to see the rules: ')
    if row == '0' and col == '0':
        game_rules()
    else: 
        try:
            row_int = int(row)
            col_int = int(col)
            if row_int > 9 or row_int < 0:
                print('Numbers of rows and columns should be in a range of 1-9 (or type 0 in each field to see the rules)')
            elif col_int > 9 or col_int <0:
                print('Numbers of rows and columns should be in a range of 1-9 (or type 0 in each field to see the rules)')
            else: 
                user_launch = missile_launch(row_int, col_int)
                shots = shots -1                            
                if user_launch == ship_1[0] or user_launch == ship_1[1] or user_launch == ship_1[2]:
                    map = map[:user_launch] + map[user_launch:user_launch + 2].replace("+", "O") + map[user_launch +2:]
                    print('Hit!')
                    print(map)
                    if dif_level_case == 'crazy':
                        shots += 2
                    else:
                        print('')
                    if shots == 0:
                        print("You've lost! Wish you more luck next time!")
                        break
                    else:
                        print('You have', shots, 'shots left')
                elif user_launch == ship_2[0] or user_launch == ship_2[1] or user_launch == ship_2[2] or user_launch == ship_2[3]:
                    map = map[:user_launch] + map[user_launch:user_launch + 2].replace("+", "O") + map[user_launch +2:]
                    print('Hit!')
                    print(map)
                    if dif_level_case == 'crazy':
                        shots += 2
                    else:
                        print('')
                    if shots == 0:
                        print("You've lost! Wish you more luck next time!")
                        break
                    else:
                        print('You have', shots, 'shots left')
                elif user_launch == ship_3[0] or user_launch == ship_3[1] or user_launch == ship_3[2]:
                    map = map[:user_launch] + map[user_launch:user_launch + 2].replace("+", "O") + map[user_launch +2:]
                    print('Hit!')
                    print(map)
                    if dif_level_case == 'crazy':
                        shots += 2
                    else:
                        print('')
                    if shots == 0:
                        print("You've lost! Wish you more luck next time!")
                        break
                    else:
                        print('You have', shots, 'shots left')
                else:
                    map = map[:user_launch] + map[user_launch:user_launch + 2].replace("+", "x") + map[user_launch +2:]
                    print('Miss!')
                    print(map)
                    if shots == 0:
                        print("You've lost! Wish you more luck next time!")
                        break
                    else:
                        print('You have', shots, 'shots left')
        
            
            
        except:
            print('Numbers should only be in values from 1 to 9 (or 0 to see the rules), and row (horizontal) should come first')

#wrapping up the game if user won and loop broke
if map.count("O"[:]) == 10:
    print("Congratulations! You won! Good work, captain!")
else:
    print("")


