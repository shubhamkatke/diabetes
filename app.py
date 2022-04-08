from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/check")
def check():
	fs = int(request.args.get("fs"))
	r1 = request.args.get("r1")
	if r1 == "Yes":
		fu = 1
	else:
		fu = 0
	with open("dia.model","rb") as f:
		model = pickle.load(f)
	res = model.predict([[fs,fu]])
	msg = res[0]
	if msg == "YES":
		txt = "Unfortnately you have diabetes :("
	else:
		txt = "You dont have diabetes :)"
	return render_template("home.html", msg = txt)
	


if __name__=="__main__":
	app.run(debug = True,use_reloader = True)