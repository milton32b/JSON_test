import json

team = {}

team['tux'] = {'health': 23, 'level': 4}
team['beastie'] = {'health': 13,'level': 6}
team['konqi'] = {'health': 18, 'level': 7}

print(team)

with open('mydata.json', 'w') as f:
    json.dump(team,f)







































