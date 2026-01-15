def get_remaining_time(game):
    if game['timetobeat'] > game['playtime']:
        return game['timetobeat'] - game['playtime']
    return 0

def get_totals():
    return (
        sum(map(lambda game : game['playtime'], backlog['games'])),
        sum(map(lambda game : game['timetobeat'], backlog['games'])),
        sum(map(get_remaining_time, backlog['games']))
    )

def print_total_ttb():
    playtime, ttb, time_remaining = get_totals()
    print(f"Total Time Played: {playtime}")
    print(f"Total Time to Beat: {ttb}")
    print(f"Time Remaining: {time_remaining}")