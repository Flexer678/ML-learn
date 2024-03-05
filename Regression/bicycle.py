import pandas as pd

# load the training dataset
#!wget https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/daily-bike-share.csv
bike_data = pd.read_csv("./Regression/daily-bike-share.csv")
bike_data.head()

bike_data["day"] = pd.DatetimeIndex(bike_data["dteday"]).day
bike_data.head(32)


numeric_features = ["temp", "atemp", "hum", "windspeed"]
bike_data[numeric_features + ["rentals"]].describe()
