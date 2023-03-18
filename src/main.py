from typing import List

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import csv
import numpy as np

PLAYER = "Stephen Curry"


def load_csv():
    response = []
    with open("./datasets/games_details_date.csv", encoding='latin1') as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            if "PLAYER_NAME" in row and row["PLAYER_NAME"] == PLAYER and row["PTS"]:
                response.append(row)
    return response


def get_avg_previous_50_games(games: List, idx: int):
    games_to_average = games[idx - 50:idx]
    avg = sum([float(game["PTS"]) for game in games_to_average]) / 50
    return avg


full_csv = load_csv()
full_csv_sorted = sorted(full_csv, key=lambda x: x["GAME_DATE_EST"])
full_csv_filtered = [x for x in full_csv_sorted if x["GAME_DATE_EST"]]

total_points = sum([float(x["PTS"]) for x in full_csv])
average_points = total_points / float(len(full_csv))

starting_index = 51

x = []
y = []
while True:
    guessing_index = starting_index+1
    if guessing_index > len(full_csv_filtered)-1:
        break
    rolling_average = get_avg_previous_50_games(full_csv_filtered, starting_index)
    x.append([rolling_average])
    result = 1 if float(full_csv_filtered[guessing_index]["PTS"]) < rolling_average else 0
    y.append(result)
    starting_index += 1

x = np.asarray(x)
y = np.asarray(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)

gnb = GaussianNB()

y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != y_pred).sum()))
print("Number of Correctly labeled points out of a total %d points : %d" % (X_test.shape[0], (y_test == y_pred).sum()))
