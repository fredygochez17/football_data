# Main Script of football data processing




#########################################################################################
############################ FUNCTIONS ##################################################
#########################################################################################






def load_data():
    # path to raw data from main.py directory (maybe make this a Global Constant later on?)
    RAW_DATA_PATH = "data/raw/fc_barcelona_24_25_champions_league_raw_csv_data/"

    data_set_file_names = \
    [
        "Advanced_Goalkeeping_2024-2025_Barcelona__Champions_League.csv"    ,   # Option 1
        "Defensive_Actions_2024-2025_Barcelona__Champions_League.csv"       ,          
        "Goal_and_Shot_Creation_2024-2025_Barcelona__Champions_League.csv"  ,
        "Goalkeeping_2024-2025_Barcelona__Champions_League.csv"             ,
        "League_phase_Champions_League.csv"                                 ,   # Option 5
        "Miscellaneous_Stats_2024-2025_Barcelona__Champions_League.csv"     ,
        "Pass_Types_2024-2025_Barcelona__Champions_League.csv"              ,
        "Passing_2024-2025_Barcelona__Champions_League.csv"                 ,
        "Playing_Time_2024-2025_Barcelona__Champions_League.csv"            ,
        "Possession_2024-2025_Barcelona__Champions_League.csv"              ,   # Option 10
        "Scores_and_Fixtures_2024-2025_Barcelona__Champions_League.csv"     ,
        "Shooting_2024-2025_Barcelona__Champions_League.csv"                ,
        "Standard_Stats_2024-2025_Barcelona__Champions_League.csv"              # Option 13
    ]

    print("Which data set would you like to access?")
    index = 1

    # print options for data set access
    for file_name in data_set_file_names:
        print("Option", index, ":", file_name)
        index = index + 1
    print("\n")

    # ask user to input the data set option they would like to access
    data_set_option = input("Please input the number of the option you want: ")
    #convert user input to an integer
    data_set_option = int(data_set_option)
    csv_file_path = RAW_DATA_PATH + data_set_file_names[data_set_option - 1]

    file_handle = open(csv_file_path)
    return file_handle





#######################################################################################
################################ END OF FUNCTIONS #####################################
#######################################################################################




































###############################################################################
############################ MAIN SCRIPT ######################################
###############################################################################


# Load Data
file_handle = load_data()
























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

