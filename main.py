import fileinput
from collections import defaultdict

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
    return results

def main():
    my_games = team_point('soccer_input.txt')
    print(my_games)


if __name__ == '__main__':
    main()
