# no checks for bad input just yet, 
# program assumes perfect inputs from user
# possible user inputs: 
#       help
#       data files -list
#       [data_file] -list stats
#       [data_file] -list players
#       [data_file]|[stat]|[player_name]
#       [data_file]|[stat]| -list top [integer]
#       [data_file]|[stat]|[player_name_1], [palyer_name_2] -compare

import time

from scripts.constants import DATA_FILE_NAMES




################################### HELPER FUNCTIONS ###################################
def print_valid_inputs():
    
    print()
    time.sleep(0.5)
    
    print('list of valid inputs (mind syntax):')
    print('\tdata files -list')
    print('\t[data_file] -list stats')
    print('\t[data_file] -list players')
    print('\t[data_file]|[stat]|[player_name]')
    print('\t[data_file]|[stat]| -list top [integer]')
    print('\t[data_file]|[stat]|[player_name_1], [palyer_name_2] -compare')
    
    print()
    


def print_data_files():
    
    print()
    time.sleep(1)
    print('Available data files:')
    time.sleep(0.5)
    
    for data_file_name in DATA_FILE_NAMES:
        
        # process data file name
        data_file_name = data_file_name.split('_')
        data_file_name = data_file_name[:data_file_name.index('2024-2025')]
        
        
        time.sleep(0.15)
        print('\t', " ".join(data_file_name))

################################### HELPER FUNCTIONS ####################################













##################################### MAIN SCRIPT #######################################
def process_user_inputs(input):
    
    input = input.split('|')
    if len(input) == 1:
        if 'data files -list' in input:
            print_data_files()
        elif 'help' in input:
            print_valid_inputs()
        else:
            print('One or more bad inputs (check syntax)')
            print("Try 'help' for a list of valid inputs or 'quit' to exit program")
            print()
    elif len(input) == 2:
        return
        
        


##################################### MAIN SCRIPT #######################################