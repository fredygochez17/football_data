
from scripts.load_data          import load_data_file









######################## CONSTANTS ########################
FILE_INPUT_ARG_INDEX    = 0     # file name         - 1st argument in user input
STAT_INPUT_ARG_INDEX    = 1     # stat selection    - 2nd argument in user input
PLAYER_INPUT_ARG_INDEX  = 2     # player selection  - 3rd argument in user input

PLAYER_ARG_INT_INDEX    = 2     # index to find the integer in player argument after string splitting

##################### END OF CONSTANTS ####################











################################### HELPER FUNCTIONS #######################################
def strip_list_whitespace(list_input_arg):
    
    # strip the left and right whitespace from each item in a list of strings and return the modified list. 
    
    count = 0
    for item in list_input_arg:
        list_input_arg[count] = item.strip()
        count += 1
        
    return list_input_arg

################################ END OF HELPER FUNCTIONS ################################### 











##################################### MAIN SCRIPT #################################################
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
    print()
    print(" | ".join(player_arg_list))
    print()
    
    # print stats for each player
    for stat in stat_arg_list : 
        print(stat, ": ", sep="", end="")
        stat_list = list()
        for player in player_arg_list :
            stat_list.append(data[player][stat])
        print(" | ".join(stat_list))
        
################################## END MAIN SCRIPT ################################################