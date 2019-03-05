import pandas as pd
import csv, sqlite3

def getDataFromcsv(csv_file_path): 
	data = pd.read_csv(csv_file_path)
	return data

def saveToDB(db_out_path, csv_file_path, table_name):
	con = sqlite3.connect(db_out_path)
	df = getDataFromcsv(csv_file_path)
	df.to_sql(table_name, con, if_exists='append', index=False)
	con.commit()
	con.close()
	return db_out_path
	
def getDataToDisplay(db_file_path, table_name):
	con = sqlite3.connect(db_file_path)
	cur = con.cursor()
	cur.execute("SELECT * FROM " + table_name)
	data = cur.fetchall()
	con.close()
	return data