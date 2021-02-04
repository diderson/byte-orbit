import sys
import fileinput
from collections import defaultdict
from operator import itemgetter

def team_point(filename):
    # Read input file and construct game result per line
    games = []
    game_list = fileinput.input(files = filename)
    for line in game_list:
        game = line.rstrip().split(', ')
        games.append(game)

    # initialize dictionary
    results = defaultdict(int)
    for game in games:
        result1 = game[0].rsplit(',', 1)
        team_one = result1[0].rsplit(' ', 1)
        team_one_name = team_one[0]
        team_one_score = team_one[1]

        result2 = game[1].rsplit(',', 1)
        team_two = result2[0].rsplit(' ', 1)
        team_two_name = team_two[0]
        team_two_score = team_two[1]

        if team_one_score > team_two_score:
            team_one_increment = 3
            team_two_increment = 0
        elif team_one_score < team_two_score:
            team_one_increment = 0
            team_two_increment = 3
        elif team_one_score == team_two_score:
            team_one_increment = 1
            team_two_increment = 1

        results[team_one_name] += team_one_increment
        results[team_two_name] += team_two_increment

    #let now sort the teams by point Desc and name
    sort_team = sorted(results.items(), key=itemgetter(0))
    final_table = sorted(sort_team, key=itemgetter(1), reverse=True)

    return final_table


def soccer_ranking_table():
    team_point_list = team_point('soccer_input.txt')
    previous_point = team_point_list[0][1]
    current_team_position = 1
    team_position = 0

    for r in team_point_list:
        team = r[0]
        point = r[1]

        if point == previous_point:
            rank = current_team_position
            team_position += 1
        elif point < previous_point:
            previous_point = point
            current_team_position += team_position
            rank = current_team_position
            team_position = 1

        unit = 'pt'
        if point > 1:
            unit = 'pts'

        output = "%s. %s, %s %s\n" % (rank, team, point, unit)
        sys.stdout.write(output)


def main():
   soccer_ranking_table() 


if __name__ == '__main__':
    main()
