from scripts.print_utilities        import  print_valid_inputs, print_input_error_message, \
                                            print_data_files

from scripts.list_top_n             import  top_n_stat_list
from scripts.user_inp_list_arg      import  list_stats, list_players
from scripts.player_stat_compare    import  player_stat_compare



######################## CONSTANTS ########################

##################### END OF CONSTANTS ####################



################################### HELPER FUNCTIONS ######################################    

################################# END HELPER FUNCTIONS ####################################


















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
        else: # user input: [data_file]|[stat]|[player_name]
            player_stat_compare(input)
    else : 
        print_input_error_message()
    
##################################### MAIN SCRIPT #######################################