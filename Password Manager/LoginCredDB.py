import sqlite3
connection = sqlite3.connect('container.db')
cursor = connection.cursor()

command = f"""CREATE TABLE IF NOT EXISTS login_credentials (username VARCHAR(255), password VARCHAR(255));"""
cursor.execute(command)
connection.commit()