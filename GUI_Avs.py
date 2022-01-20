import requests
from tkinter import *
from datetime import datetime
import time

def scoreboard():
    start_date = datetime.now()
    today = start_date.strftime("%Y-%m-%d")
    starting_score = str(0)

    avs_score = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId=21&startDate=" + today + "&endDate=" + today)
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

    home_image = PhotoImage(file="kings_logo.png")
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

    away_image = PhotoImage(file="avs_logo.png")
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

    def quit():
        window.destroy()



    if home_team_name.get() == "Colorado Avalanche" and home_team_score.get() != starting_score:
        quit()
        starting_score = home_team_score.get()
    elif away_team_name.get() == "Colorado Avalanche" and away_team_score.get() != starting_score:
        quit()
        starting_score = away_team_score.get()

    window.mainloop()

scoreboard()
