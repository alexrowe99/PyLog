import json
from display import print_backlog
from total import print_total_ttb

backlog = json.load(open('backlog.json', 'r'))

def main():
    print_backlog(backlog)
    print_total_ttb(backlog)
    with open("backlog.json", "w") as file:
        json.dump(backlog, file, indent=4)

if __name__ == "__main__":
    main()