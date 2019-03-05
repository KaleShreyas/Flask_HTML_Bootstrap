from flask import Flask, render_template, request, redirect
from flask_paginate import Pagination, get_page_args
app = Flask(__name__)

from model import DataManager, DataCollector

# Variables #
csv_file_path = r'C:\\Users\\svksh\\Documents\\GitHub\\Flask_HTML_Bootstrap\\model\\chinook_employee.csv'
db_out_path = r'C:\\Users\\svksh\\Documents\\GitHub\\Flask_HTML_Bootstrap\\chinook_employee.db'
db_file_path = r'C:\\Users\\svksh\\Documents\\GitHub\\Flask_HTML_Bootstrap\\model\\chinook.db'
out_table_name = 'training_data'
in_table_name = 'employees'

# HTML Routing #
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
	return render_template('DataManager.html', file = db_file_path, pagination=Pagination)

@app.route("/datatraining")
def GoToDataTrainer():
	return render_template('DataTrainer.html')

@app.route("/logsummary")
def GoToLogger():
	return render_template('Logger.html')

# Support methods #
ALLOWED_EXTENSIONS = set(['db'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_employees(df, offset=0, per_page=5):
    return df[offset: offset + per_page]
	
# Python function calls #
@app.route("/savedata", methods=['GET', 'POST'])
def GetDataInDatabase():
	out_path = DataCollector.saveToDB(db_out_path, csv_file_path, out_table_name)
	return render_template('DataCollector.html')

@app.route("/readcsv", methods=['GET', 'POST'])
def ViewData():
	out_path = DataCollector.saveToDB(db_out_path, csv_file_path, out_table_name)
	df = DataCollector.getDataToDisplay(db_out_path, out_table_name)
	return render_template('DataCollector.html', data=df)

@app.route("/loaddata", methods=['GET', 'POST'])
def LoadData():
	df = DataManager.getDataToDisplay(db_file_path, in_table_name)
	page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
	pagination_employees = get_employees(df, offset=offset, per_page=per_page)
	total = 512
	pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap3')
	return render_template('DataManager.html', data=pagination_employees, page=page, per_page=per_page, pagination=pagination, count=total)

@app.route("/books", methods=["POST"])
def books():
	bookid = request.form["bookid"]
	print(bookid)
	return 'OK' + bookid
	 
@app.route("/updateAll", methods=["POST"])
def updatealllll():
	DataManager.getUpdatedData(db_file_path, in_table_name) 
	return 'OK'
	
if __name__ == "__main__":
  app.run(debug="True")