# function calls
import time
from scripts.load_data          import load_data_file


# constants
FILE_INPUT_ARG_INDEX    = 0     # file name         - 1st argument in user input
STAT_INPUT_ARG_INDEX    = 1     # stat selection    - 2nd argument in user input
PLAYER_INPUT_ARG_INDEX  = 2     # player selection  - 3rd argument in user input

PLAYER_ARG_INT_INDEX    = 2     # index to find the integer in player argument after string splitting


def top_n_stat_list(user_input):
    # split the input by '|'
    input_split_vert_bar = user_input.split('|')
    
    # split the last argument by spaces
    player_arg = input_split_vert_bar[PLAYER_INPUT_ARG_INDEX].strip().split(' ')
    
    # retreive integer
    try:
        player_arg_int = int(player_arg[PLAYER_ARG_INT_INDEX])
    except:
        player_arg_int = 1
    
    # retreive data structure given filename from user input
    file_name   = input_split_vert_bar[FILE_INPUT_ARG_INDEX].strip()
    data = load_data_file(file_name)
    
    # retrieve stat from user input
    stat_arg = input_split_vert_bar[STAT_INPUT_ARG_INDEX].strip()
    
    # build player dictionary with values based on stat input from user
    player_dict = dict()
    for player in data :
        try:
            player_dict[player] = float(data[player][stat_arg])
        except:
            print('unable to numerically sort stat')
            print()
            break
    
    # sort player dictionary in descending order
    player_dict_desc = dict(sorted(player_dict.items(), key=lambda item: item[1], reverse=True))
    
    # print top [int from user input] of [stat from user input]
    count = 0
    for player in player_dict_desc : 
        time.sleep(0.05)
        print(player,':\t', f"{player_dict_desc[player]:g}", sep="")
        count += 1
        if count >= player_arg_int : break
        