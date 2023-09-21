from Boardgame import BoardGame  # Imports the BoardGame class from the boardgame.py

def parse_board_games(filename, encoding="utf-8"):
    ### parses the data from the file and skips over the header line
    games = []
    with open(filename, "r", encoding=encoding) as f:
        lines = f.readlines()
        for line in lines[1:]: 
            parts = line.strip().split('\t')
            if len(parts) == 6:
                name, year_str, gibbons_rating, public_rating, min_players, min_playtime = parts
                try:
                    year = int(float(year_str))
                    gibbons_rating = float(gibbons_rating)
                    public_rating = float(public_rating)
                    min_players = float(min_players)
                    min_playtime = int(min_playtime)
                    games.append(BoardGame(name, year, gibbons_rating, public_rating, min_players, min_playtime))
                except ValueError:
                    print(f"Skipped invalid entry: {line}")
    return games

def print_all_games(games):
    ###prints games
    for game in games:
        print(game)

def print_games_from_year(games, year):
    ###prints games from a specific year
    found = False
    for game in games:
        if game.year == year:
            print(game)
            found = True
    if not found:
        print("No games found")

def print_ranking_range(games, start, end):
    ### prints the ranking range of the games based on a start and end point for reference
    for game in games:
        if start <= game.gibbons_rating <= end:
            print(game)

def print_rating_diff(games, diff):
    ### prints the rating difference between games based on a given value
    for game in games:
        if abs(game.gibbons_rating - game.public_rating) >= diff:
            print(game)

def print_by_playtime(games, max_playtime):
    ### prints the games with the same or less playtime than the max given.
    for game in games:
        if game.min_playtime <= max_playtime:
            print(game)