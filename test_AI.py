from training_data import *
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = CountVectorizer()
X = vectorizer.fit_transform([x[0] for x in training_data])
y = [x[1] for x in training_data]

clf = MultinomialNB()
clf.fit(X, y)

len_training_data = len(training_data)
list_error = []

for i in range(0, len_training_data):
	os.system("clear")
	print(f"Scan data: {i+1}/{len_training_data}")
	X_test = vectorizer.transform([training_data[i][0]])
	prediction = clf.predict(X_test)[0]
	if prediction != training_data[i][1]:
		list_error.append(i)
		
if list_error == []:
	print("Accuracy: 100%")
else:
	print(f"Accuracy: {round((1 - len(list_error)/len_training_data) * 100, 2)}%")
	print(f"Error in: {list_error}")
	print(training_data[list_error[0]])