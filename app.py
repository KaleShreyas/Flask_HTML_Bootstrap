from flask import Flask, render_template, request
app = Flask(__name__)

#from model import DataManager

@app.route("/")
def GoToIndex():
	return render_template('Index.html')

@app.route("/home")
def GoToHome():
	return render_template('Home.html')

@app.route("/datacollection")
def GoToDataCollector():
	return render_template('DataCollector.html')

@app.route("/datamanagement")
def GoToDataManager():
	return render_template('DataManager.html')

@app.route("/datatraining")
def GoToDataTrainer():
	return render_template('DataTrainer.html')

@app.route("/logsummary")
def GoToLogger():
	return render_template('Logger.html')

@app.route("/displaydata")
def ViewData():
	df = DataManager.getDataToDisplay()
	df_html = df.to_html()
	return render_template('dataviewer.html', table_html=df_html)

if __name__ == "__main__":
  app.run()