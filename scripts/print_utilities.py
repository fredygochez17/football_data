import time

from scripts.constants import DATA_FILE_NAMES
from scripts.constants import RAW_DATA_PATH


# output for "help" input from user
def print_valid_inputs():
    
    print()
    time.sleep(0.25)
    
    print('list of valid inputs (mind syntax):')
    time.sleep(0.05)
    print('\t-list data files')
    time.sleep(0.05)
    print('\t[data_file] -list stats')
    time.sleep(0.05)
    print('\t[data_file] -list players')
    time.sleep(0.05)
    print('\t[data_file]|[stat]|[player_name]')
    time.sleep(0.05)
    print('\t[data_file]|[stat]|-list top [integer]')
    time.sleep(0.05)
    print('\t[data_file]|[stat]|[player_name_1], [palyer_name_2] -compare stats')
    time.sleep(0.05)
    
    print()

 
def print_input_error_message():
    
    print('One or more bad inputs (check syntax)')
    print("Try 'help' for a list of valid inputs or 'quit' to exit program")
    print()
    
    
# output for "-list data files" input from user
def print_data_files():
    
    print()
    time.sleep(0.25)
    print('Available data files:')
    time.sleep(0.25)
    
    for data_file_name in DATA_FILE_NAMES:
        
        # format data file name
        data_file_name = data_file_name.split('_')
        data_file_name = data_file_name[:data_file_name.index('2024-2025')]
        
        # print formatted file name
        time.sleep(0.05)
        print('\t', " ".join(data_file_name))

# print list of stats in data file selected by user
def print_stat_list(data):
    print()
    time.sleep(.25)
    
    for player in data:
        for stat in data[player]:
            print(stat)
            time.sleep(0.05)
        
        print()
        break
    
# print list of players in data file selected by user
def print_player_list(data):
    print()
    time.sleep(.25)
    
    for player in data:
        print(player)
        time.sleep(0.05) 