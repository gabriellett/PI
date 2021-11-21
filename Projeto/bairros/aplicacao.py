import sqlite3

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c=conn.cursor()

def bo_bairro(bairro):
	c.execute('SELECT COUNT ( DISTINCT (bairro) ) AS "Number of employees" FROM dadosOK  WHERE year=2015')
	for row in c.fetchall():
		print(row)
	return

bo_bairro('PARQUE FERNANDA')
