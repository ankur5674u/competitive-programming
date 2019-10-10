def orangecap(match_dict):
    from collections import OrderedDict
    res = OrderedDict()
    for match, match_score in match_dict.items():
        for player, score in match_score.items():
            if player in res:
                res[player]+=score
            else:
                res[player]=score
    orangecap_player=max(res,key=res.get)
    return orangecap_player,res[orangecap_player]


if __name__ == '__main__':
    orangecap({'match1': {'player1': 57, 'player2': 38}, 'match2': {'player3': 9, 'player1': 42},
               'match3': {'player2': 41, 'player4': 63, 'player3': 91}})

