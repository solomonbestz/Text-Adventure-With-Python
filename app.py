import time
import os

# THIS IS A FUNCTION TO SET TIME TO DISPLAY AND CLEAR SCREEN
def set_timer(first_time: int, second_time: int) -> None:
    time.sleep(first_time)
    os.system('cls')
    time.sleep(second_time)

# THIS IS A FUNCTION TO SELECT PLAYER
def select_player(player_names: list) -> str:
    global player 
    print("Choose Player To Play With")
    for n in range(len(player_names)):
        print(f'''
              Player {n+1}: {player_names[n]}''')
    try:
        choose_player = int(input('Choose Player: '))
        if choose_player in range(1, len(player_names)+1):
            player = player_names[choose_player-1]
        else:
            print('Invalid Choice of Player')
            set_timer(1, 1)
            select_player(names)
    except Exception:
        print('Invalid Choice of Character')
        set_timer(1, 1)
        select_player(names)
        
        

# FUNCTION TO SELECT WEAPONS
def select_weapon(weapons: list) -> str:
    print("Select a weapon")
    print("""
    The more you advance in the game the better your weapon to be selected.
    
    LISTS OF WEAPONS:
    """)
    count_weapon: int = 1
    for weapon in weapons:
        print(f'''    {count_weapon}) {weapon}''')
        count_weapon += 1

    

# FUNCTION TO START GAME
def start_game():
    select_player(names)
    set_timer(2, 1)
    print(f"Welcome To Legendary Treasure {player}")
    select_weapon(basic_weapons)


# FUNCTION TO DISPLAY THE GAME INSTRUCTION
def game_instruction() -> None:
    print('QUEST OF THE LEGENDARY TREASURE')
    set_timer(3, 1)
    print('''
You are meant to pass through all obstacles
and claim the treasure
''')
    set_timer(5, 1)

def game_menu():
    game_instruction()
    start_game()
    



if __name__=='__main__':
    names: list = ['Aria', 'Rojas', 'Mathew', 'Dera']
    basic_weapons: list = ['Knife', 'Spear', 'Pistol', 'Mallet', 'Wooden Shield']
    advance_weapons: list = ['Magic Gloves', 'Magic Armour', 'Magic Sheild', 'Magic']

    # Calling the game functions 
    game_menu()
 