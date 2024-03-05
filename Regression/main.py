import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection


X, y = datasets.load_diabetes(return_X_y=True)
print(X.shape)
print(X[0])

X = X[:, 4]
#turns it from vertical to horizontal from index 0 to in
X = X.reshape((-1, 1))

X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.33
)

model = linear_model.LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


plt.scatter(X_test, y_test, color="black")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.xlabel("Scaled BMIs")
plt.ylabel("Disease Progression")
plt.title("A Graph Plot Showing Diabetes Progression Against BMI")
plt.show()
