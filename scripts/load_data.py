# this module returns data structure for data set selected based on user inputs

import csv

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
        index += 1
    print("\n")

    # ask user to input the data set option they would like to access
    data_set_option = input("Please input the number of the option you want: ")
    #convert user input to an integer
    data_set_option = int(data_set_option) 
    
    # exclude options 5 and 11 for now. We'll handle those later
    if data_set_option == 5 or data_set_option == 11:
        print("Currenlty this program cannot process Options 5 or 11.\nPlease wait for future udpates and try a different option.")
        data_set_option = input("Please input the number of the option you want (not option 5 or 11): ")
        data_set_option = int(data_set_option) 
        
        # quit is option 5 or 11 gets inputed again
        if data_set_option == 5 or data_set_option == 11:
            print("program quit for not listening >:(")
            quit()
        
    
    # open csv file_path    
    csv_file_path = RAW_DATA_PATH + data_set_file_names[data_set_option - 1]
    file_handle = open(csv_file_path)
    
    # create csv dictionary reader
    csv_dict_reader = csv.DictReader(file_handle)
    
    # build nested dictionary: data[player name as row][stat label as column]
    data = {}
    for row in csv_dict_reader:
        
        # player name becomes the main key
        player_name = row['Player']
        data[player_name] = row
        
    
    return data