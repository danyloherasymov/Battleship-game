# Battleship-game
A final project for Introduction to Programming (MTAT.03.236) course at the University of Tartu


For this project, I intended to create a game program called “Battleship”. It is a simplified version of this game, where user will play vs. computer, but without placing their own ships. User has to find and destroy all the enemy ships (exactly 3 of them) in given amount of attempts to win the game. If after final attempt there are still some enemy ships left, user has lost.

For this program, I created a string variable called “map” which prints out the game field. The field contains of a 9x9 table of ‘+’ signs, divided by spaces, and limited by ‘|’. Each row and column have a respective number outside the field. All these values are stored in the “map”. 

User can input 2 numbers: number of a row, and number of column where they intend to find an enemy ship. Input numbers are part of an infinite loop which tests if there are still enemy ships unmarked on the map. If the user hits the ship, they will get “Hit!” message, and the ‘+’ they were aiming for will be replaced by ‘O’. If the user miss, they will get “Miss!” message, and the ‘+’ they were aiming for will be replaced by ‘x’. In both cases, previously defined variable “shots” will decrease by 1 each time user makes full input (row and column). If user hits all the parts of all the ships, the loop breaks and user receive a winning message. If user run out of the shots before they destroy all the ships, they will lose, and loop will break.

User input is limited by “try-except” piece of code to values from 0 to 9 only. If user inputs any values outside this range, they will be warned about it and loop starts anew. If user prints 0 in both row and column input fields, they will call a pre-defined function called “game_rules”. This function prints out a list of rules for the game and explains the user what to do. This step is realized with “if-else” statement inside the loop in such way, that calling out this function won’t result in “shots -1”.

The other function called “missile_laucnh” converts the user input (2 arguments) into indexes of all positions of all the ‘+’ signs on the map. Inside this function, there are many “if-else” statements that analyze the input of rows and columns, and return a value, which equals to the index of a ‘+’ sign on the map.

There is also a part of the code, which generates random number from the list of ‘+’ signs indexes, add next 2 or 3 following indexes and stores it in a variables called “ship_n”. Neither of values in any of the ship_n variables won’t be the same to avoid ship overlapping.

Inside the loop, there is a piece of code, that compares the result of “missile_launch” function with user input, and any of the indexes of ship_n variables. In case of a match, it represents “Hit!” message and replaces this very ‘+’ sign on the map with ‘O’. Respectively, it does so in case there’s no match, only the message is replaced by “Miss!” and ‘+’ sign is replaced by ‘x’. 

This project was developed with only basic understanding of python. During the course, such topics as nested loops/strings, matrix operations, basics of OOP and other features that could be used to simplify the code, were not covered. Hence, the code of the game is not perfect and built only on the basics of python.
