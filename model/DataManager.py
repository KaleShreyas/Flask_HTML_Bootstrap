import sqlite3
import pandas as pd

def getDataToDisplay(db_file_path, table_name):
	con = sqlite3.connect(db_file_path)
	cur = con.cursor()
	cur.execute("SELECT * FROM " + table_name)
	data = cur.fetchall()
	con.close()
	return data
	
def getUpdatedData(db_file_path, table_name):
	con = sqlite3.connect(db_file_path)
	cur = con.cursor()
	cur.execute("UPDATE employees SET Country = CASE Country WHEN 'CANADA' THEN 'USA' ELSE NULL END")
	con.commit()
	con.close()