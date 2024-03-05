import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
import numpy as np
from flask import Flask, request, render_template
import pickle

ufos = pd.read_csv('./Regression/webap/ufos.csv')
# gets all the correct data.
ufos.head()




#sets the data to different values
ufos = pd.DataFrame({'Seconds': ufos['duration (seconds)'], 'Country': ufos['country'],'Latitude': ufos['latitude'],'Longitude': ufos['longitude']})

#basically gets all the unique values in the string.
ufos.Country.unique()


#to remove rows that contain missing values in a row.
ufos.dropna(inplace=True)


ufos = ufos[(ufos['Seconds'] >= 1) & (ufos['Seconds'] <= 60)]

ufos.info()
#converts  countries to a number
ufos['Country'] = LabelEncoder().fit_transform(ufos['Country'])

ufos.head()

selected_features = ['Seconds', 'Latitude', 'Longitude']

x = ufos[selected_features]
y = ufos['Country']
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)



#gets the classification report
print(classification_report(y_test, predictions))


print('Predicted labels: ', predictions)
#gets the accuracy of the (test scores (vs) the ones predicted)
print('Accuracy: ', accuracy_score(y_test,        predictions))


name_of_file = 'ufo-model.pkl'
#
pickle.dump(model, open(name_of_file,'wb'))

model = pickle.load(open('ufo-model.pkl','rb'))
print(model.predict([[50,44,-12]]))

app = Flask(__name__)

model = pickle.load(open("./ufo-model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]

    countries = ["Australia", "Canada", "Germany", "UK", "US"]

    return render_template(
        "index.html", prediction_text="Likely country: {}".format(countries[output])
    )


if __name__ == "__main__":
    app.run(debug=True)