import csv


# data
from scripts.constants import DATA_FILE_NAMES
from scripts.constants import RAW_DATA_PATH


def load_data_file(file_name): 
    
    file_name = file_name.replace(' ', '_')
    
    # find DATA_FILE_NAMES index for which file_name exists
    for name in DATA_FILE_NAMES:
        # normalize file names for comparison
        file_name_lower = file_name.lower()
        name_lower = name.lower()
        
        if file_name_lower in name_lower :
            file_name = name
            break
    
    # open file
    file_path   = RAW_DATA_PATH + file_name
    try:
        file_handle = open(file_path)
    except:
        print('Error: file not found (check syntax)')
        print()
        return
    
    # create csv dictionary reader
    csv_dict_reader = csv.DictReader(file_handle)
    
    
    # build nested dictionary: data[player name as row][stat label as column]
    data = {}
    for row in csv_dict_reader:
        
        # player name becomes the main key
        player_name = row['Player']
        data[player_name] = row
    
    
    return data