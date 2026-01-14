import json

backlog = json.load(open('backlog.json', 'r'))
NAME_DISPLAY_LENGTH=16
GENRE_DISPLAY_LENGTH=10
NUM_DISPLAY_LENGTH=8

def truncate_number(num):
    num_str = str(num)
    return num_str+" "*(NUM_DISPLAY_LENGTH-len(num_str))

def truncate_string(string, display_len):
    if len(string) <= display_len:
        return string+" "*(display_len-len(string))
    return string[:display_len-3]+"..."

def print_backlog():
    print("Game            |Genre     |Playtime|Platform|Owned?|Completed?")
    for game in backlog['games']:
        print(f"{truncate_string(game['name'], NAME_DISPLAY_LENGTH)}|{truncate_string(game['genre'], GENRE_DISPLAY_LENGTH)}|{truncate_number(game['playtime'])}|{truncate_number(game['platform'])}|{"Yes   " if game['owned'] else "No    "}|{"Yes       " if game['completed'] else "No        "}")

def main():
    print_backlog()


if __name__ == "__main__":
    main()