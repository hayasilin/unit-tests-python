class TennisScore(object):
    def __init__(self):
        self.player_one_score = 0
        self.player_two_score = 0
        self.score_map = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
        }

    def get_score(self):
        if self.player_one_score == self.player_two_score:
            return '%s All' % self.score_map[self.player_one_score]
        else:
            return '%s %s' % (self.score_map[self.player_one_score], self.score_map[self.player_two_score])


    def add_score(self, player, times):
        if player == 1:
            self.player_one_score += times
        elif player == 2:
            self.player_two_score += times
        else:
            raise Exception("only two player")