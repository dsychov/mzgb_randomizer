import random as god_desire

participants = ['Nikita', 'Anya', 'Igor', 'Dima', 'Yulia', 'Katya Karpik', 'Ruslan', 'Tania', 'Jenya', 'Andrey', 'Katya']
team_names = ['Naugad', 'Intrigor']
game_day1 = 'Tuesday'
game_day2 = 'Wednesday'
team_day1 = []
team_day2 = []
all_participants = reduce(lambda x,y:x+y,[len(participants),len(team_day1),len(team_day2)])
teams = [team_day1, team_day2]
max_amount_in_one_team = all_participants/2+1 if all_participants%2 else all_participants/2

def sort_players():
    while len(participants):
        group_participants = [x for x in participants if isinstance(x, list)]
        if len(group_participants):
            group = group_participants[0]
            decision = god_desire.randint(0, 1)
            if len(teams[decision]) < (max_amount_in_one_team -1):
                teams[decision].extend(group)
            else:
                teams[decision].extend(group)
            participants.remove(group)
        else:
            participant = participants[0]
            decision = god_desire.randint(0,1)
            if len(teams[decision]) < max_amount_in_one_team:
                teams[decision].append(participant)
            else:
                teams[not decision].append(participant)
            participants.remove(participant)

def set_team_names():
    decision_team_name = god_desire.randint(0, 1)
    team_name1 = team_names[decision_team_name]
    team_name2 = team_names[not decision_team_name]
    return team_name1, team_name2

def show_result(team_name1, team_name2):
    print "{}_{}: {}".format(game_day1, team_name1, team_day1)
    print "{}_{}: {}".format(game_day2, team_name2, team_day2)

sort_players()
team_name1, team_name2 = set_team_names()
show_result(team_name1, team_name2)