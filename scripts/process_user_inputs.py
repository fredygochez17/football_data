import time
import csv

from scripts.print_utilities import print_valid_inputs, print_input_error_message, \
                                    print_data_files, print_player_list, print_stat_list



######################## CONSTANTS ########################

# data
from scripts.constants import DATA_FILE_NAMES
from scripts.constants import RAW_DATA_PATH

FILE_INPUT_ARG_INDEX    = 0     # file name         - 1st argument in user input
STAT_INPUT_ARG_INDEX    = 1     # stat selection    - 2nd argument in user input
PLAYER_INPUT_ARG_INDEX  = 2     # player selection  - 3rd argument in user input

PLAYER_ARG_INT_INDEX    = 2     # index to find the integer in player argument after string splitting


##################### END OF CONSTANTS ####################










################################### HELPER FUNCTIONS ###################################        

def load_data_file(file_name): 
    
    file_name = file_name.replace(' ', '_')
    
    # find DATA_FILE_NAMES index for which file_name exists
    for name in DATA_FILE_NAMES:
        if file_name in name:
            file_name = name
            break
    
    # open file
    file_path   = RAW_DATA_PATH + file_name
    try:
        file_handle = open(file_path)
    except:
        print('Error: file not found (check syntax)')
        print()
        return
    
    # create csv dictionary reader
    csv_dict_reader = csv.DictReader(file_handle)
    
    
    # build nested dictionary: data[player name as row][stat label as column]
    data = {}
    for row in csv_dict_reader:
        
        # player name becomes the main key
        player_name = row['Player']
        data[player_name] = row
    
    
    return data






################################### HELPER FUNCTIONS ####################################













##################################### MAIN SCRIPT #######################################
def process_user_inputs(input):
    
    if 'help' in input or 'Help' in input or 'HELP' in input :
        print_valid_inputs()
    elif '-list data files' in input : 
        print_data_files()
    elif '-list stats' in input :
        # retrieve file name from user input
        input_split = input.split('-')
        file_name   = input_split[FILE_INPUT_ARG_INDEX].strip()
        
        # load csv data from file
        data = load_data_file(file_name)
        
        # print list of stats in data file
        print_stat_list(data)
    elif '-list players' in input:
        # retrieve file name from user input
        input_split = input.split('-')
        file_name   = input_split[FILE_INPUT_ARG_INDEX].strip()
        
        # load csv data form file
        data = load_data_file(file_name)
        
        # print list of stats in data file
        print_player_list(data)
    elif '|' in input : 
        if '-list top' in input : 
            # split the input by '|'
            input_split = input.split('|')
            
            # split the last argument by spaces
            player_arg = input_split[PLAYER_INPUT_ARG_INDEX].strip().split(' ')
            
            # retreive integer
            try:
                player_arg_int = int(player_arg[PLAYER_ARG_INT_INDEX])
            except:
                player_arg_int = 1
            
            # retreive data structure given filename from user input
            file_name   = input_split[FILE_INPUT_ARG_INDEX].strip()
            data = load_data_file(file_name)
            
            # retrieve stat form user input
            stat_arg = input_split[STAT_INPUT_ARG_INDEX].strip()
            
            # build player dictionary with values based on stat input from user
            player_dict = dict()
            for player in data :
                player_dict[player] = float(data[player][stat_arg])
            
            # sort player dictionary in descending order
            player_dict_desc = dict(sorted(player_dict.items(), key=lambda item: item[1], reverse=True))
            
            # print top [int from user input] of [stat from user input]
            count = 0
            for player in player_dict_desc : 
                time.sleep(0.05)
                print(player,':\t', player_dict_desc[player], sep="")
                count += 1
                if count >= player_arg_int : break
        elif '-compare stats' in input : 
            # load data file
            input_split = input.split('|')
            file_name   = input_split[FILE_INPUT_ARG_INDEX].strip()
            data = load_data_file(file_name)
            
            # get stat from user input
            stat_arg = input_split[STAT_INPUT_ARG_INDEX].strip()
            
            # get player names from player argument
            player_args = input_split[PLAYER_ARG_INT_INDEX].strip().split('-')
            players = player_args[0].split(',')
            player_1 = players[0].strip()
            player_2 = players[1].strip()
            
            # output data
            print(player_1,'|', player_2)
            print(stat_arg,':', data[player_1][stat_arg], '|', data[player_2][stat_arg])
        else: # user input: [data_file]|[stat]|[player_name]
            # retrieve file name from user input
            input_split = input.split('|')
            file_name   = input_split[FILE_INPUT_ARG_INDEX].strip()
            
            # load csv data from file
            data = load_data_file(file_name)
            
            # output stat-player from user input
            stat_column = input_split[STAT_INPUT_ARG_INDEX].strip()
            player_row  = input_split[PLAYER_INPUT_ARG_INDEX].strip()
            print(player_row, ' - ', stat_column, ': ', data[player_row][stat_column], sep="")
    else : 
        print_input_error_message()
    

    
    
        


##################################### MAIN SCRIPT #######################################