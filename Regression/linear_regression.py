import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#function to split the testing data in half
from sklearn.model_selection import train_test_split


#outliers in data causes data to  
#x
time_studied = np.array ([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1,1)
#y
scores = np.array ([56, 83, 47, 93, 47, 82, 45, 23, 55, 67, 57, 4, 89]).reshape(-1,1)

'''
model = LinearRegression()
model.fit(time_studied, scores)

#predicts the x which is time studied in minutes
print(model.predict(np.array([500]).reshape(-1, 1)))

#displays individual points as markers
plt.scatter(time_studied, scores)
#time studied
x = np.linspace(0, 70, 100).reshape(-1, 1)
y = model.predict(x)

plt.plot(x, y, "r")
plt.xlabel("time studied")
plt.ylabel("score")
plt.title("Graph for time studied and scored")

#sets the limit for yaxis
plt.ylim(0, 100)
#visualise
plt.show()

'''


'''
time_train, time_test, score_train, score_test = train_test_split(time_studied, scores, test_size=0.2)

model = LinearRegression()
model.fit(time_train, score_train)
print(model.score(time_test, score_test))

plt.scatter(time_train, score_train)
x = np.linspace(0,70,100).reshape(-1,1)
y =model.predict(x)
plt.plot(x,y, "r")
plt.plot()
plt.show()'''




# Load the CSV file using np.genfromtxt()
data = np.genfromtxt('./Regression/bike.csv', delimiter=',')


min_value= 0
max_value =20
# Access specific columns by indexing the array
temp = np.array(data[(data[:, 9] >= min_value) & (data[:, 9] <= max_value), 9])
rentals = np.array(data[(data[:, 9] >= min_value) & (data[:, 9] <= max_value), 13])

# Reshape the columns into 2D arrays
temp = temp.reshape(-1, 1)
#print(temp)
rentals = rentals.reshape(-1, 1)
print(temp)
time_train, time_test, score_train, score_test = train_test_split(temp, rentals, test_size=0.2)

model = LinearRegression()
model.fit(time_train, score_train)
#print(model.score(time_test, score_test))
print(model.predict(np.array([500]).reshape(-1, 1)))
plt.scatter(time_train, score_train)
plt.ylim(0,3500)
plt.xlim(0,1)
x = np.linspace(0,70,100).reshape(-1,1)
y =model.predict(x)
plt.plot(x,y, "r")

plt.plot()
plt.show()