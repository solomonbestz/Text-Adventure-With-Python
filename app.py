import time
import os

def set_timer(first_time, second_time):
    time.sleep(first_time)
    os.system('cls')
    time.sleep(second_time)


def select_player(player_names: list) -> str:
    set_timer(5, 1)
    print("Choose Player")
    for n in range(len(player_names)):
        print(f'Player {n+1}: {player_names[n]}')
    # choose_player = int(input('Choose Player'))

def game_instruction():
    print('QUEST OF THE LEGENDARY TREASURE')
    set_timer(3, 1)
    print('You are meant to pass through all obstacles and claim the treasure')



if __name__=='__main__':
    names: list = ['Aria', 'Rojas', 'Mathew', 'Dera']



    # Calling the game functions
    game_instruction() 
    select_player(names)