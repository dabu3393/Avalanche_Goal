import requests
from datetime import datetime


start_date = datetime.now()
today = start_date.strftime("%Y-%m-%d")

avs_score = requests.get("https://statsapi.web.nhl.com/api/v1/schedule?teamId=21&startDate=" + today + "&endDate=" + today)
score = avs_score.json()

print(score['dates'][0]['games'][0]['teams']['home']['team']['name'] + ": " + str(score['dates'][0]['games'][0]['teams']['home']['score']) + "      " + score['dates'][0]['games'][0]['teams']['away']['team']['name'] + ": " + str(score['dates'][0]['games'][0]['teams']['away']['score']))

