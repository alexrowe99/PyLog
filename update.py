from simple_term_menu import TerminalMenu

def update_game_field(games, id, key, new_value):
    for game in games:
        if game['id'] == id:
            game[key] = new_value

def update_game(games):
    game_options = map(lambda game : game['name'], games)
    game_menu = TerminalMenu(game_options, title="Choose a game to update")
    game_index = game_menu.show()
    update_options = [f"Name ({games[game_index]['name']})",
                        f"Genre ({games[game_index]['genre']})",
                        f"Playtime ({games[game_index]['playtime']})",
                        f"Time to Beat ({games[game_index]['timetobeat']})",
                        f"Platform ({games[game_index]['platform']})",
                        f"Owned ({'Yes' if games[game_index]['owned'] else 'No'})",
                        f"Completed ({'Yes' if games[game_index]['completed'] else 'No'})"]
    update_menu = TerminalMenu(update_options, title=f"Updating {games[game_index]['name']}")
    field_index = update_menu.show()
    new_value = None
    match (field_index):
        case 0:
            update_key = 'name'
            display = 'Name'
            val_type = str
        case 1:
            update_key = 'genre'
            display = 'Genre'
            val_type = str
        case 2:
            update_key = 'playtime'
            display = 'Playtime'
            val_type = int
        case 3:
            update_key = 'timetobeat'
            display = 'Time to Beat'
            val_type = int
        case 4:
            update_key = 'platform'
            display = 'Platform'
            val_type = str
        case _:
            update_key = 'owned' if field_index == 5 else 'completed'
            boolean_menu = TerminalMenu(["Yes", "No"], title=update_key[0].upper()+update_key[1:]+"?")
            new_value = not bool(boolean_menu.show())
    if type(new_value) is not bool:
        new_value = val_type(input(f"Enter new {display}: "))
    update_game_field(games, games[game_index]['id'], update_key, new_value)
    return games