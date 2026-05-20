
# load modules
from scripts.load_data import load_data







###############################################################################
############################ MAIN SCRIPT ######################################
###############################################################################


# Load Data
data = load_data()
#print(data['Raphinha']['Player'])

print()
for player in data:
    #print(player)
    #print(data[player].keys())
    print("Available Stats:")
    for stat in data[player]:
        print(stat)
    # only need from first player
    break


    
###############################################################################
############################ END OF MAIN SCRIPT ###############################
###############################################################################























# # csv file we want to process
# csv_data_file_name = "Standard_Stats_2024-2025_Barcelona__Champions_League.csv"
# file_handle = open(RAW_DATA_PATH + csv_data_file_name)

# player_names = list() # append player name on each iteration to make a list of player names
# first_line = True
# for line in file_handle:
    
#     if first_line == True:
#         column_labels = line.split(',')
#         first_line = False
#         continue
    
#     current_row = line.split(',')
#     player_names.append(current_row[0]) #player name is in first column
    
# sorted_player_names = player_names
# sorted_player_names.sort()
# for player_name in sorted_player_names:
#     print(player_name)

