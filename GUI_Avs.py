from cv2 import resize
import requests
from tkinter import *
from datetime import datetime
import time


while True:
    start_date = datetime.now()
    today = start_date.strftime("%Y-%m-%d")
    starting_score = str(2)

    avs_score = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId=21&startDate=2022-06-26&endDate=2022-06-26")
    score = avs_score.json()

    game_id = score['dates'][0]['games'][0]['gamePk']
    avs_stats = requests.get("https://statsapi.web.nhl.com/api/v1/game/" + str(game_id) + "/feed/live") # 2021020591 (<<<Blackhawks vs Avs Game ID, use to see stats from past game) 2021020606 (<<<Winnipeg Jets Game ID)
    stats = avs_stats.json()

    window = Tk()
    window.geometry("1430x750")
    window.configure(bg="#236192")
    window.title("Avalanche Gamecast by Davis Burrill")

    current_period = StringVar()
    current_period.set(stats['liveData']['linescore']['currentPeriodOrdinal'])
    period_time = StringVar()
    period_time.set(stats['liveData']['linescore']['currentPeriodTimeRemaining'])
    home_shots = StringVar()
    home_shots.set(str(stats['liveData']['linescore']['teams']['home']['shotsOnGoal']))
    away_shots = StringVar()
    away_shots.set(str(stats['liveData']['linescore']['teams']['away']['shotsOnGoal']))
    home_team_name = StringVar()
    home_team_name.set(score['dates'][0]['games'][0]['teams']['home']['team']['name'])
    away_team_name = StringVar()
    away_team_name.set(score['dates'][0]['games'][0]['teams']['away']['team']['name'])
    home_team_pp = StringVar()
    home_team_pp.set(str(int(stats['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['powerPlayGoals'])) +"/" + str(int(stats['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])))
    away_team_pp = StringVar()
    away_team_pp.set(str(int(stats['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['powerPlayGoals'])) +"/" + str(int(stats['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['powerPlayOpportunities'])))
    home_team_fo = StringVar()
    home_team_fo.set(stats['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])
    away_team_fo = StringVar()
    away_team_fo.set(stats['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['faceOffWinPercentage'])
    home_team_blks = StringVar()
    home_team_blks.set(str(stats['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['blocked']))
    away_team_blks = StringVar()
    away_team_blks.set(str(stats['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['blocked']))
    home_team_hits = StringVar()
    home_team_hits.set(str(stats['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['hits']))
    away_team_hits = StringVar()
    away_team_hits.set(str(stats['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['hits']))
    home_team_score = StringVar()
    home_team_score.set(str(score['dates'][0]['games'][0]['teams']['home']['score']))
    away_team_score = StringVar()
    away_team_score.set(str(score['dates'][0]['games'][0]['teams']['away']['score']))

    home_label = Label(text="HOME", font=("DIN Condensed", 20, "bold"), bg="#236192")
    home_label.grid(row=0,column=0, pady=40)
    away_label = Label(text="AWAY", font=("DIN Condensed", 20, "bold"), bg="#236192")
    away_label.grid(row=0,column=2, pady=40)

    time_frame = Frame(window, bg="#236192")
    time_frame.grid(row=0,column=1)

    period_label = Label(time_frame, textvariable = current_period, font=("DIN Condensed", 30, "bold"), bg="#236192")
    period_label.grid(row=0,column=0, pady=(25,0))
    time_label = Label(time_frame, textvariable = period_time, font=("DIN Condensed", 30, "bold"), bg="#236192")
    time_label.grid(row=1,column=0)

    if score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Colorado Avalanche":
        home_image = PhotoImage(file="Pictures/COL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Carolina Hurricanes":
        home_image = PhotoImage(file="Pictures/CAR.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Columbus Blue Jackets":
        home_image = PhotoImage(file="Pictures/CBJ.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "New Jersey Devils":
        home_image = PhotoImage(file="Pictures/NJD.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "New York Islanders":
        home_image = PhotoImage(file="Pictures/NYI.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "New York Rangers":
        home_image = PhotoImage(file="Pictures/NYR.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Philadelphia Flyers":
        home_image = PhotoImage(file="Pictures/PHI.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Pittsburgh Penguins":
        home_image = PhotoImage(file="Pictures/PIT.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Washington Capitals":
        home_image = PhotoImage(file="Pictures/WAS.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Boston Bruins":
        home_image = PhotoImage(file="Pictures/BOS.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Buffalo Sabres":
        home_image = PhotoImage(file="Pictures/BUF.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Detroit Red Wings":
        home_image = PhotoImage(file="Pictures/DET.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Florida Panthers":
        home_image = PhotoImage(file="Pictures/FLR.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Montréal Canadiens":
        home_image = PhotoImage(file="Pictures/MTL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Ottawa Senators":
        home_image = PhotoImage(file="Pictures/OTT.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Tampa Bay Lightning":
        home_image = PhotoImage(file="Pictures/TBL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Toronto Maple Leafs":
        home_image = PhotoImage(file="Pictures/TOR.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Arizona Coyotes":
        home_image = PhotoImage(file="Pictures/ARI.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Chicago Blackhawks":
        home_image = PhotoImage(file="Pictures/CHI.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Dallas Stars":
        home_image = PhotoImage(file="Pictures/DAL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Minnesota Wild":
        home_image = PhotoImage(file="Pictures/MIN.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Nashville Predators":
        home_image = PhotoImage(file="Pictures/NSH.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "St. Louis Blues":
        home_image = PhotoImage(file="Pictures/STL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Winnipeg Jets":
        home_image = PhotoImage(file="Pictures/WIN.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Anaheim Ducks":
        home_image = PhotoImage(file="Pictures/ANH.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Calgary Flames":
        home_image = PhotoImage(file="Pictures/CAL.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Edmonton Oilers":
        home_image = PhotoImage(file="Pictures/EDM.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Los Angeles Kings":
        home_image = PhotoImage(file="Pictures/LAK.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "San Jose Sharks":
        home_image = PhotoImage(file="Pictures/SJS.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Seattle Kraken":
        home_image = PhotoImage(file="Pictures/SEA.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Vancouver Canucks":
        home_image = PhotoImage(file="Pictures/VAN.png")
    elif score['dates'][0]['games'][0]['teams']['home']['team']['name'] == "Vegas Golden Knights":
        home_image = PhotoImage(file="Pictures/VEG.png")

    home_image_label = Label(image=home_image, bg="#236192")
    home_image_label.grid(row=1,column=0)

    middle_frame = Frame(window, bg="#236192")
    middle_frame.grid(row=3,column=1)

    vs_label = Label(text="VS", font=("DIN Condensed", 55, "bold"), bg="#236192")
    vs_label.grid(row=1,column=1)

    sog_label = Label(middle_frame, text="SOG", font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    sog_label.grid(row=0,column=1)

    pp_label = Label(middle_frame, text="PP", font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    pp_label.grid(row=1,column=1)

    fo_label = Label(middle_frame, text="FO%", font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    fo_label.grid(row=2,column=1)

    blocks_label = Label(middle_frame, text="BLKS", font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    blocks_label.grid(row=3,column=1)

    hits_label = Label(middle_frame, text="HITS", font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    hits_label.grid(row=4,column=1)

    home_shots_label = Label(middle_frame, textvariable = home_shots, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    home_shots_label.grid(row=0,column=0, padx=10)

    away_shots_label = Label(middle_frame, textvariable = away_shots, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    away_shots_label.grid(row=0,column=2, padx=10)

    home_pp_label = Label(middle_frame, textvariable = home_team_pp, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    home_pp_label.grid(row=1,column=0, padx=10)

    away_pp_label = Label(middle_frame, textvariable = away_team_pp, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    away_pp_label.grid(row=1,column=2, padx=10)

    home_fo_label = Label(middle_frame, textvariable = home_team_fo, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    home_fo_label.grid(row=2,column=0, padx=10)

    away_fo_label = Label(middle_frame, textvariable = away_team_fo, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    away_fo_label.grid(row=2,column=2, padx=10)

    home_blks_label = Label(middle_frame, textvariable = home_team_blks, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    home_blks_label.grid(row=3,column=0, padx=10)

    away_blks_label = Label(middle_frame, textvariable = away_team_blks, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    away_blks_label.grid(row=3,column=2, padx=10)

    home_hits_label = Label(middle_frame, textvariable = home_team_hits, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    home_hits_label.grid(row=4,column=0, padx=10)

    away_hits_label = Label(middle_frame, textvariable = away_team_hits, font=("DIN Condensed", 30), fg="dark grey", bg="#236192")
    away_hits_label.grid(row=4,column=2, padx=10)

    if score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Colorado Avalanche":
        away_image = PhotoImage(file="Pictures/COL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Carolina Hurricanes":
        away_image = PhotoImage(file="Pictures/CAR.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Columbus Blue Jackets":
        away_image = PhotoImage(file="Pictures/CBJ.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "New Jersey Devils":
        away_image = PhotoImage(file="Pictures/NJD.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "New York Islanders":
        away_image = PhotoImage(file="Pictures/NYI.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "New York Rangers":
        away_image = PhotoImage(file="Pictures/NYR.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Philadelphia Flyers":
        away_image = PhotoImage(file="Pictures/PHI.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Pittsburgh Penguins":
        away_image = PhotoImage(file="Pictures/PIT.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Washington Capitals":
        away_image = PhotoImage(file="Pictures/WAS.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Boston Bruins":
        away_image = PhotoImage(file="Pictures/BOS.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Buffalo Sabres":
        away_image = PhotoImage(file="Pictures/BUF.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Detroit Red Wings":
        away_image = PhotoImage(file="Pictures/DET.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Florida Panthers":
        away_image = PhotoImage(file="Pictures/FLR.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Montréal Canadiens":
        away_image = PhotoImage(file="Pictures/MTL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Ottawa Senators":
        away_image = PhotoImage(file="Pictures/OTT.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Tampa Bay Lightning":
        away_image = PhotoImage(file="Pictures/TBL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Toronto Maple Leafs":
        away_image = PhotoImage(file="Pictures/TOR.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Arizona Coyotes":
        away_image = PhotoImage(file="Pictures/ARI.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Chicago Blackhawks":
        away_image = PhotoImage(file="Pictures/CHI.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Dallas Stars":
        away_image = PhotoImage(file="Pictures/DAL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Minnesota Wild":
        away_image = PhotoImage(file="Pictures/MIN.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Nashville Predators":
        away_image = PhotoImage(file="Pictures/NSH.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "St. Louis Blues":
        away_image = PhotoImage(file="Pictures/STL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Winnipeg Jets":
        away_image = PhotoImage(file="Pictures/WIN.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Anaheim Ducks":
        away_image = PhotoImage(file="Pictures/ANH.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Calgary Flames":
        away_image = PhotoImage(file="Pictures/CAL.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Edmonton Oilers":
        away_image = PhotoImage(file="Pictures/EDM.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Los Angeles Kings":
        away_image = PhotoImage(file="Pictures/LAK.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "San Jose Sharks":
        away_image = PhotoImage(file="Pictures/SJS.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Seattle Kraken":
        away_image = PhotoImage(file="Pictures/SEA.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Vancouver Canucks":
        away_image = PhotoImage(file="Pictures/VAN.png")
    elif score['dates'][0]['games'][0]['teams']['away']['team']['name'] == "Vegas Golden Knights":
        away_image = PhotoImage(file="Pictures/VEG.png")

    away_image_label = Label(image=away_image, bg="#236192")
    away_image_label.grid(row=1,column=2)

    home_name_label = Label(textvariable = home_team_name, font=("DIN Condensed", 45, "bold"), bg="#236192")
    home_name_label.grid(row=2,column=0, padx=180, pady=25)
    away_name_label = Label(textvariable = away_team_name, font=("DIN Condensed", 45, "bold"), bg="#236192")
    away_name_label.grid(row=2,column=2, padx=180, pady=25)

    home_score_label = Label(textvariable = home_team_score, font=("DIN Condensed", 145, "bold"), bg="#236192")
    home_score_label.grid(row=3,column=0)
    away_score_label = Label(textvariable = away_team_score, font=("DIN Condensed", 145, "bold"), bg="#236192")
    away_score_label.grid(row=3,column=2)

    # def quit():
    #     window.destroy()
    #
    # if home_team_name.get() == "Colorado Avalanche" and home_team_score.get() != starting_score:
    #     quit()
    #     starting_score = home_team_score.get()
    # if away_team_name.get() == "Colorado Avalanche" and away_team_score.get() != starting_score:
    #     quit()
    #     starting_score = away_team_score.get()

    window.mainloop()
