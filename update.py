
def update_game_field(backlog, id, key, new_value):
    for game in backlog['games']:
        if game['id'] == id:
            game[key] = new_value