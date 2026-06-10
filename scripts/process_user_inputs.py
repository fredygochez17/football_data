import time


from scripts.print_utilities    import print_valid_inputs, print_input_error_message, \
                                    print_data_files, print_player_list, print_stat_list

from scripts.load_data          import load_data_file

######################## CONSTANTS ########################



FILE_INPUT_ARG_INDEX    = 0     # file name         - 1st argument in user input
STAT_INPUT_ARG_INDEX    = 1     # stat selection    - 2nd argument in user input
PLAYER_INPUT_ARG_INDEX  = 2     # player selection  - 3rd argument in user input

PLAYER_ARG_INT_INDEX    = 2     # index to find the integer in player argument after string splitting


##################### END OF CONSTANTS ####################










################################### HELPER FUNCTIONS ###################################        
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
        print(player,':\t', player_dict_desc[player], sep="")
        count += 1
        if count >= player_arg_int : break
        
def player_stat_compare(user_input):
    # split user input by vertical bar and strip whitespace of each string item in the list.
    user_input_split_vert_bar = user_input.split('|')
    user_input_split_vert_bar = strip_list_whitespace(user_input_split_vert_bar) 
    
    # retrieve file name from first argument from user input and load data
    file_name = user_input_split_vert_bar[FILE_INPUT_ARG_INDEX].strip()
    data = load_data_file(file_name)
    
    # retrieve list of stats from second argument of user input
    stat_arg_list = user_input_split_vert_bar[STAT_INPUT_ARG_INDEX]
    stat_arg_list = stat_arg_list.split(",")
    stat_arg_list = strip_list_whitespace(stat_arg_list)
    
    # retrieve list of players from third argument of user input
    player_arg_list = user_input_split_vert_bar[PLAYER_ARG_INT_INDEX]
    player_arg_list = player_arg_list.split(",")
    player_arg_list = strip_list_whitespace(player_arg_list)
    print(" | ".join(player_arg_list))
    
    # print stats for each player
    for stat in stat_arg_list : 
        print(stat, ": ", sep="", end="")
        stat_list = list()
        for player in player_arg_list :
            stat_list.append(data[player][stat])
        print(" | ".join(stat_list))

def strip_list_whitespace(list_input_arg):
    
    # strip the left and right whitespace from each item in a list of strings and return the modified list. 
    
    count = 0
    for item in list_input_arg:
        list_input_arg[count] = item.strip()
        count += 1
        
    return list_input_arg
        

################################### HELPER FUNCTIONS ####################################













##################################### MAIN SCRIPT #######################################
def process_user_inputs(input):
    
    if 'help' in input or 'Help' in input or 'HELP' in input :
        print_valid_inputs()
    elif '-list data files' in input : 
        print_data_files()
    elif '-list stats' in input :
        list_stats(input)
    elif '-list players' in input:
        list_players(input)
    elif '|' in input : 
        if '-list top' in input : 
            top_n_stat_list(input)
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
            player_stat_compare(input)
    else : 
        print_input_error_message()
    

    
    
        


##################################### MAIN SCRIPT #######################################