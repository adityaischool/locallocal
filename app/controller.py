from flask import render_template,request,session,redirect,jsonify
from flask import url_for
import sqlite3
#from app import app


def getDeals(busid):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')

	c = conn.cursor()
	query='select busid,charid,dealid,dealtext from deals where busid=\''+busid+'\''
	c.execute(query)
	results = [dict(busid=row[0], charid=row[1] , dealid=row[2], dealtext=row[3]) for row in c.fetchall()]
	conn.close()
	print results
	return results

if __name__ == '__main__':
	getDeals('pappy')
