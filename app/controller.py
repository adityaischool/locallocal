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
	print "results--------",results
	return results

def authorise(uname,password):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')

	c = conn.cursor()
	query='select busid from business where busid=\''+uname+'\' and password=\''+password+'\'' 
	c.execute(query)
	results = [dict(busid=row[0]) for row in c.fetchall()]
	conn.close()
	print "results--------",results,"------------------>>",len(results)
	if len(results)<1:
		return False

	if(results[0]['busid']!=''):
		return True
	else:
		return False

def getdealdata(dealid):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	query='select b.name,d.dealid,d.dealtext,b.address,d.dealdate from deals d,business b where d.busid=b.busid and d.dealid=\''+dealid+'\''
	c.execute(query)
	results = [dict(busname=row[0], dealid=row[1] , dealtext=row[2], busaddress=row[3], dealdate=row[4]) for row in c.fetchall()]
	conn.close()
	print results
	return results

def insertDeal(dealdata):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	c.execute('insert into deals values (?,?,?,?,?)',dealdata)
	#results = [dict(busname=row[0], dealid=row[1] , dealtext=row[2], busaddress=row[3], dealdate=row[4]) for row in c.fetchall()]
	conn.commit()
	conn.close()
	print "Entered data"

def getbusdata(busid):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	query='select bus_id,name,address from business where bus_id=\''+busid+'\''
	c.execute(query)
	results = [dict(busid=row[0], charid=row[1] , dealid=row[2], dealtext=row[3], dealdate=row[4]) for row in c.fetchall()]
	conn.close()
	print results
	return results

def getMaxDeal():
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	query='select max(dealid) from deals'
	c.execute(query)
	results = [dict(dealid=row[0]) for row in c.fetchall()]
	print "maaax deal --------",results
	conn.close()
	return results

"""
def getdealdata(dealid):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')

	c = conn.cursor()
	query='select busid,charid,dealid,dealtext from deals where busid=\''+busid+'\''
	c.execute(query)
	results = [dict(busid=row[0], charid=row[1] , dealid=row[2], dealtext=row[3]) for row in c.fetchall()]
	conn.close()
	print results
	return results
"""

if __name__ == '__main__':
	getDeals('pappy')
