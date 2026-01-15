import json
from display import print_backlog
from total import print_total_ttb
from update import update_game_field
from simple_term_menu import TerminalMenu

backlog = json.load(open('backlog.json', 'r'))
options = ["Print Backlog", "Show Total Time To Beat", "Update Backlog"]

def main():
    main_menu = TerminalMenu(options)
    while True:
        menu_entry_index = main_menu.show()
        match menu_entry_index:
            case 0:
                print_backlog(backlog)
            case 1:
                print_total_ttb(backlog)
            case 2:
                games = backlog['games']
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
                update_game_field(backlog, games[game_index]['id'], update_key, new_value)
                with open("backlog.json", "w") as file:
                    json.dump(backlog, file, indent=4)
                exit()

if __name__ == "__main__":
    main()