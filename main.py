
# load modules
import time
from scripts.process_user_inputs              import process_user_inputs





###############################################################################
############################ MAIN SCRIPT ######################################
###############################################################################


# keep the program going until user quits
last_user_input = None
while last_user_input != 'quit' :
    
    print()
    time.sleep(0.1)
    last_user_input = input('Your Input: ')
    print()
    
    if last_user_input == 'q' : last_user_input = 'quit'
    if last_user_input == 'quit': 
        print('Closing Program...')
        time.sleep(0.5)
        print()
        time.sleep(0.1)
        continue
    
    process_user_inputs(last_user_input)


    
###############################################################################
############################ END OF MAIN SCRIPT ###############################
###############################################################################


