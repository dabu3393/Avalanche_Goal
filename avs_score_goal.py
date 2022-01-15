import requests
from datetime import datetime
import time
import os

starting_score = 0

while True:


    # This gets the date and schedule for today
    start_date = datetime.now()
    today = start_date.strftime("%Y-%m-%d")

    avs_score = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId=21&startDate=" + today + "&endDate=" + today)
    score = avs_score.json()


    # This gets the player id's and checks for goal scoring
    avs_players_info = requests.get("https://statsapi.web.nhl.com/api/v1/teams/21?expand=team.roster")
    player_info = avs_players_info.json()
    game_id = score['dates'][0]['games'][0]['gamePk']
    avs_stats = requests.get("https://statsapi.web.nhl.com/api/v1/game/" + str(game_id) + "/boxscore") # 2021020591 (<<<Blackhawks vs Avs Game ID, use to see stats from past game) 2021020606 (<<<Winnipeg Jets Game ID)
    stats = avs_stats.json()

    def home_away():
        if stats['teams']['home']['team']['name'] == "Colorado Avalanche":
            return "home"
        else:
            return "away"

    id_list = []

    for x in range(0, len(player_info['teams'][0]['roster']['roster'])):
        player_id = player_info['teams'][0]['roster']['roster'][x]['person']['id']
        id_string = "ID" + str(player_id)
        id_list.append(id_string)

    def player_loop(id):
        for y in id:
            if y in stats['teams'][home_away()]['players']:
                if stats['teams'][home_away()]['players'][y]['stats'] != {}:
                    player_name = stats['teams'][home_away()]['players'][y]['person']['fullName']
                    if player_name == "Pavel Francouz" or player_name == "Darcy Kuemper":
                        pass
                    else:
                        player_goal = stats['teams'][home_away()]['players'][y]['stats']['skaterStats']['goals']
                        if player_goal != 0 and player_goal != 1 and player_goal != 2:
                            print("SCORING HIS " + str(player_goal) + "RD GOAL OF THE NIGHT, " + player_name.upper() + "!")
                        elif player_goal != 0 and player_goal != 1:
                            print("SCORING HIS " + str(player_goal) + "ND GOAL OF THE NIGHT, " + player_name.upper() + "!")
                        elif player_goal != 0:
                            print("SCORING HIS " + str(player_goal) + "ST GOAL OF THE NIGHT, " + player_name.upper() + "!")
                        else:
                            pass

    player_loop(id_list)



    # This determines when we score and runs a program
    home_team_name = score['dates'][0]['games'][0]['teams']['home']['team']['name']
    away_team_name = score['dates'][0]['games'][0]['teams']['away']['team']['name']
    home_team_score = score['dates'][0]['games'][0]['teams']['home']['score']
    away_team_score = score['dates'][0]['games'][0]['teams']['away']['score']


    if home_team_name == "Colorado Avalanche" and home_team_score != starting_score:
        os.system("afplay avs_goal_horn.wav&")
        print("AVS GOAL!!!")
        time.sleep(2)
        player_loop(id_list) # Should print who scored, but will also print past scoring so need to fix that
        time.sleep(2)
        print("New Score!!\nColorado Avalanche: " + str(home_team_score) + "\n" + away_team_name + ": " + str(away_team_score))
        starting_score = home_team_score
    elif away_team_name == "Colorado Avalanche" and away_team_score != starting_score:
        os.system("afplay avs_goal_horn.wav&")
        print("AVS GOAL!!!")
        time.sleep(2)
        player_loop(id_list)  # Should print who scored, but will also print past scoring so need to fix that
        time.sleep(2)
        print("New Score!!\nColorado Avalanche: " + str(away_team_score) + "\n" + home_team_name + ": " + str(home_team_score))
        starting_score = away_team_score


    time.sleep(20)


# Issues that need fixed
#     . (CONSULT) Figure out how to print the current goal scorer and not all the goal scorers since it'll run through the whole loop picking up each player that has already scored
#     . Since using two different API's to see who scored and what the score of the game is, make sure that the API's update their stats similtaneously so the player_loop() has data to present when scored
#     . Create a GUI








# if the avs score changes
#     Say "AVS GOAL" --done
#     Say who scored the goal --Need Help
#     Play Music --done
#     Show the new score --done
