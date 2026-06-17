
# load modules
import time
from scripts.process_user_inputs              import process_user_inputs


def get_user_input() :
    print()
    time.sleep(0.1)
    user_input = input('Input: ')
    print(user_input)
    return user_input

def input_is_quit(user_input) :
    user_input = user_input.lower()
    if user_input == 'quit' or user_input == 'q' : 
        return True
    else : 
        return False

def close_program() :
        print('Closing Program...')
        time.sleep(0.5)
        print()
        time.sleep(0.1)


###############################################################################
############################ MAIN SCRIPT ######################################
###############################################################################


# keep the program going until user quits
user_input = None
while user_input != 'quit' :
    
    user_input = get_user_input()
    
    #if user_input == 'q' or user_input == 'Q' or user_input == 'QUIT' : user_input = 'quit'
    if input_is_quit(user_input) : 
        user_input = 'quit'
        close_program()
        continue
    
    process_user_inputs(user_input)


    
###############################################################################
############################ END OF MAIN SCRIPT ###############################
###############################################################################


