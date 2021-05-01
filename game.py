from mod import *
import random
from time import sleep

game = TicTacToe()

game.welcome_message()
sleep(3)

game.reference_key()
sleep(5)

player_name1 = input('Enter player1 name- ')
player_name2 = input('Enter player2 name- ')
print()

character = random.randint(0,1)

if character == 0:
    character_1 = 'X'
    character_2 = 'O'

elif character == 1:
    character_1 = 'O'
    character_2 = 'X'

player_character_key = {character_1 : player_name1, character_2 : player_name2}

player_1 = game.player(player_name1, character_1)
player_2 = game.player(player_name2, character_2)

print(f'{player_1[0]} got {player_1[1]}')
print(f'{player_2[0]} got {player_2[1]}')
print()

_ = input('Press any key to start')
print()

game.game_grid()

first_chance = random.randint(0,1)
turn = 1

for _ in range(9999):
    if game.winner_check()[0] != 1:
        try:
            box = int(input('Enter the box number where you want to mark- '))
            if first_chance == 0:
                if turn == 1:
                    if game.gameplay(box, 'X') == 1:
                        turn *= -1
                    elif game.gameplay(box, 'X') == 0:
                        turn *= 1

                elif turn == -1:
                    if game.gameplay(box, 'O') == 1:
                        turn *= -1
                    elif game.gameplay(box, 'O') == 0:
                        turn *= 1
            
            elif first_chance == 1:
                if turn == 1:
                    if game.gameplay(box, 'O') == 1:
                        turn *= -1
                    elif game.gameplay(box, 'O') == 0:
                        turn *= 1

                elif turn == -1:
                
                    if game.gameplay(box, 'X') == 1:
                        turn *= -1
                    elif game.gameplay(box, 'X') == 0:
                        turn *= 1            
        
        except ValueError: print('Invalid Input')    
    
    else:
        print(f'{player_character_key[game.winner_check()[1]]} has won the game!')
        break