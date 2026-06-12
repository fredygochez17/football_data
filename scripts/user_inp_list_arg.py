# function calls
from scripts.load_data          import load_data_file
from scripts.print_utilities    import print_stat_list, print_player_list


# constants
FILE_INPUT_ARG_INDEX    = 0     # file name         - 1st argument in user input
STAT_INPUT_ARG_INDEX    = 1     # stat selection    - 2nd argument in user input
PLAYER_INPUT_ARG_INDEX  = 2     # player selection  - 3rd argument in user input



def list_stats(user_input):
    # retrieve file name from user input
    input_split_dash = user_input.split('-')
    file_name   = input_split_dash[FILE_INPUT_ARG_INDEX].strip()
    
    # load csv data from file
    data = load_data_file(file_name)
    
    # print list of stats in data file
    print_stat_list(data)
    
    
def list_players(user_input):
    # retrieve file name from user input
    input_split_dash = user_input.split('-')
    file_name   = input_split_dash[FILE_INPUT_ARG_INDEX].strip()

    # load csv data form file
    data = load_data_file(file_name)

    # print list of stats in data file
    print_player_list(data)