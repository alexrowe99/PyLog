def get_remaining_time(game):
    if game['timetobeat'] > game['playtime']:
        return game['timetobeat'] - game['playtime']
    return 0

def get_totals(backlog):
    return (
        sum(map(lambda game : game['playtime'], backlog['games'])),
        sum(map(lambda game : game['timetobeat'], backlog['games'])),
        sum(map(get_remaining_time, backlog['games']))
    )

def print_total_ttb(backlog):
    playtime, ttb, time_remaining = get_totals(backlog)
    print(f"Total Time Played: {playtime}")
    print(f"Total Time to Beat: {ttb}")
    print(f"Time Remaining: {time_remaining}")