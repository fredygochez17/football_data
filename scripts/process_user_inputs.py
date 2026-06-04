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
import csv



######################## CONSTANTS ########################

# data
from scripts.constants import DATA_FILE_NAMES
from scripts.constants import RAW_DATA_PATH


##################### END OF CONSTANTS ####################










################################### HELPER FUNCTIONS ###################################
def print_valid_inputs():
    
    print()
    time.sleep(0.5)
    
    print('list of valid inputs (mind syntax):')
    print('\t-list data files')
    print('\t[data_file] -list stats')
    print('\t[data_file] -list players')
    print('\t[data_file]|[stat]|[player_name]')
    print('\t[data_file]|[stat]| -list top [integer]')
    print('\t[data_file]|[stat]|[player_name_1], [palyer_name_2] -compare')
    
    print()
    


def print_data_files():
    
    print()
    time.sleep(0.5)
    print('Available data files:')
    time.sleep(0.25)
    
    for data_file_name in DATA_FILE_NAMES:
        
        # format data file name
        data_file_name = data_file_name.split('_')
        data_file_name = data_file_name[:data_file_name.index('2024-2025')]
        
        # print formatted file name
        time.sleep(0.05)
        print('\t', " ".join(data_file_name))
        

def load_data_file(file_name): 
    
    file_name = file_name.replace(' ', '_')
    
    # find DATA_FILE_NAMES index for which file_name exists
    for name in DATA_FILE_NAMES:
        if file_name in name:
            file_name = name
            break
    
    # open file
    file_path   = RAW_DATA_PATH + file_name
    file_handle = open(file_path)
    
    # create csv dictionary reader
    csv_dict_reader = csv.DictReader(file_handle)
    
    
    # build nested dictionary: data[player name as row][stat label as column]
    data = {}
    for row in csv_dict_reader:
        
        # player name becomes the main key
        player_name = row['Player']
        data[player_name] = row
    
    
    return data


def print_stat_list(data):
    print()
    for player in data:
        for stat in data[player]:
            print(stat)
        
        print()
        break
    
def print_player_list(data):
    print()
    for player in data:
        print(player)
        

def print_input_error_message():
    
    print('One or more bad inputs (check syntax)')
    print("Try 'help' for a list of valid inputs or 'quit' to exit program")
    print()

################################### HELPER FUNCTIONS ####################################













##################################### MAIN SCRIPT #######################################
def process_user_inputs(input):
    
    if 'help' in input:
        print_valid_inputs()
    elif '-list' in input and '|' not in input:
        if '-list data files' in input:
            print_data_files()
        elif '-list stats' in input or '-list players' in input:
            # process file_name from user input
            input = input.split('-')
            file_name = input[0].strip()
            
            # load data
            data = load_data_file(file_name)
            
            if 'list stats' in input:
                # print stat list
                print_stat_list(data)
            else: # print player list
                print_player_list(data)
            
        else: print_input_error_message()
    else:
        print_input_error_message()
    
    
        


##################################### MAIN SCRIPT #######################################