import json
from display import print_backlog
from total import print_total_ttb
from update import update_game
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
                update_game(backlog['games'])
                with open("backlog.json", "w") as file:
                    json.dump(backlog, file, indent=4)
                exit()

if __name__ == "__main__":
    main()