import socket
from mtranslate import translate
from langdetect import detect
from training_data import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

check = True
network = False

# Training data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([x[0] for x in training_data])
y = [x[1] for x in training_data]

clf = MultinomialNB()
clf.fit(X, y)

def check_network():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect(("google.com", 80))
        s.close()
        return True
    except:
        return False

def ask(question):
    global language, check, network
    
    if (question == "check network") and (check == True):
        if check_network() == True:
            check = False
            network = True
            return "Stable network connection, can now use multi-language"
        else:
            check = False
            network = False
            return "No internet connection, only English can be used"
    
    if network == True:
        try:
            language = language
            question = translate(question, "en")
        except:
            language = detect(question)
            if question != translate(question, language):
                language = "en"
            question = translate(question, "en")
        
        if question == "":
            pass
        else:
            X_test = vectorizer.transform([question])
            prediction = clf.predict(X_test)[0]
            return translate(prediction, language)
    else:
        if question == "":
            pass
        else:
            X_test = vectorizer.transform([question])
            prediction = clf.predict(X_test)[0]
            return prediction