# this program recieves a nested dictionary as an argument 
# and outputs stat data based on user inputs


def player_stat_output(data):
    
    print('\nPlayers in data set:\n')
    for player in data:
        print(player)
        
    print()
    player_name_input = input('Input a player name by copying and pasting from the list above: ')
    print()
    
    # print the list of stats available from the data set
    print('\n\nAvailable Stats: \n')
    for player in data:
        for stat in data[player]:
            print(stat)
            
        break
        
    stat_input = input('\nInput a stat by copying and pasting form the list above: ')
    
    print(player_name_input, '>', stat_input, ':\t', data[player_name_input][stat_input])
