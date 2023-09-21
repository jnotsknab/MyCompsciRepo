class BoardGame:
    ### Board game class with variables corresponding to components of boardgames
    def __init__(self, name, year, gibbons_rating, public_rating, min_players, min_playtime):
        self.name = name
        self.year = year
        self.gibbons_rating = gibbons_rating
        self.public_rating = public_rating
        self.min_players = min_players
        self.min_playtime = min_playtime

    def __str__(self):
        return f"{self.name} ({self.year}) [GR-{self.gibbons_rating}, PR-{self.public_rating}, MP-{self.min_players}, MT-{self.min_playtime}]"