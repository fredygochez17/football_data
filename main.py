# Main Script of football data processing



# path to raw data from main.py directory
raw_data_path = "data/raw/fc_barcelona_24_25_champions_league_raw_csv_data/"

# csv file we want to process
csv_data_file_name = "Standard_Stats_2024-2025_Barcelona__Champions_League.csv"
file_handle = open(raw_data_path + csv_data_file_name)

player_names = list() # append player name on each iteration to make a list of player names
first_line = True
for line in file_handle:
    
    if first_line == True:
        column_labels = line.split(',')
        first_line = False
        continue
    
    current_row = line.split(',')
    player_names.append(current_row[0]) #player name is in first column
    
sorted_player_names = player_names
sorted_player_names.sort()
for player_name in sorted_player_names:
    print(player_name)

