from fastapi import FastAPI
from clean_data import clean_text
import pickle
import os


app = FastAPI()
Model = pickle.load(open('clf_pickle.pkl','rb'))
vectorizer=pickle.load(open('vectorizer_pickle.pkl','rb'))


	

@app.get("/predict/{text}")
def predict(text):
	text=clean_text(text)
	vect=vectorizer.transform([text])
	prediction=Model.predict(vect)
	if prediction==0:
		output="non Hate speech"
	elif prediction==1:
		output="Hate Speech"
	return {"prediction":output}#,"class":prediction}