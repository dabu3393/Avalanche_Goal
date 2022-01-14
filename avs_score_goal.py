import requests
from datetime import datetime
import time
import os

starting_score = 0

while True:

    start_date = datetime.now()
    today = start_date.strftime("%Y-%m-%d")

    avs_score = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId=21&startDate=" + today + "&endDate=" + today)
    score = avs_score.json()
    game_id = score['dates'][0]['games'][0]['gamePk']
    avs_stats = requests.get("https://statsapi.web.nhl.com/api/v1/game/" + str(game_id) + "/boxscore")
    stats = avs_stats.json()

    # DONT TOUCH, USING PAST GAME STATS TO FIND PATH FOR GOAL SCORER!!!
    # practice_stats = requests.get("https://statsapi.web.nhl.com/api/v1/game/2021020591/boxscore")
    # pstats = practice_stats.json()

    home_team_name = score['dates'][0]['games'][0]['teams']['home']['team']['name']
    away_team_name = score['dates'][0]['games'][0]['teams']['away']['team']['name']
    home_team_score = score['dates'][0]['games'][0]['teams']['home']['score']
    away_team_score = score['dates'][0]['games'][0]['teams']['away']['score']


    if home_team_name == "Colorado Avalanche" and home_team_score != starting_score:
        print("AVS GOAL!")
        os.system("afplay avs_goal_horn.wav&")
        print("New Score!!\nColorado Avalanche: " + str(home_team_score) + "\n" + away_team_name + ": " + str(away_team_score))
        starting_score = home_team_score
    elif away_team_name == "Colorado Avalanche" and away_team_score != starting_score:
        print("AVS GOAL!")
        os.system("afplay avs_goal_horn.wav&")
        print("New Score!!\nColorado Avalanche: " + str(away_team_score) + "\n" + home_team_name + ": " + str(home_team_score))
        starting_score = away_team_score


    time.sleep(30)





# if the avs score changes
#     Say "AVS GOAL" --done
#     Say who scored the goal --Need Help
#     Play Music --done
#     Show the new score --done
