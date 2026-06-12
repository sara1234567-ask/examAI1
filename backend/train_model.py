from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

texts = [

# positive
"I love this",
"I like it",
"This is amazing",
"Fantastic",
"Excellent",
"Very good",
"Awesome",
"Great job",
"Wonderful",
"Perfect",
"Best product",
"I am happy",
"I enjoyed it",
"Beautiful",
"Super",

# negative
"I hate this",
"Terrible",
"Awful",
"Very bad",
"Worst experience",
"I am disappointed",
"Bad product",
"Horrible",
"I don't like it",
"This is useless",
"So bad",
"Poor quality",
"Really terrible",
"I am angry",
"Disgusting",

# neutral
"It's okay",
"Average",
"Nothing special",
"Normal",
"So so",
"Not bad",
"It works",
"Acceptable",
"Fine",
"Neither good nor bad"

]

labels = [

# positive
"positive","positive","positive","positive","positive",
"positive","positive","positive","positive","positive",
"positive","positive","positive","positive","positive",

# negative
"negative","negative","negative","negative","negative",
"negative","negative","negative","negative","negative",
"negative","negative","negative","negative","negative",

# neutral
"neutral","neutral","neutral","neutral","neutral",
"neutral","neutral","neutral","neutral","neutral"

]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

model.fit(texts, labels)

with open("sentiment_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully!")