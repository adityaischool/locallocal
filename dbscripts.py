import sqlite3
from flask import g
"""
def get_db():
    db = getattr(g, '/tmp/flaskr.db', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def getBuds(myname):
	db = getattr(g, '/tmp/flaskr.db', None)
	query='sele#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	ct id, friendname,data from friends where id=\''+myname+'\''+'order by id desc')
	cur = g.db.execute(query)
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
drop table if exists friends;
create table friends (
  id text not null,
  friendname text not null,
   data text not null
);
    """
def queryAllByUser(username):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	query='select * from hearstmain where username=' + 'Amy'
	c.execute(query)
	results = [dict(username=row[0], obj=row[1]) for row in c.fetchall()]
	conn.close()
	return results
def addTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table users (userid not null, name not null, password not null, address not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()


def addBusTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()

	querytoExec="create table business (busid not null, name not null, password not null, address not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def addBusData():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	objtoadd= [('pappy','Pappy Beer','password','1627 University 94703'),('cocoman','Cup Cake Sams','password','214 University 94703'),('rooty','Root Hamburgers','password','212 Shattuck Berkeley California USA')]
	query='insert into business values (?,?,?,?)'
	c.executemany('insert into users values (?,?,?,?)',objtoadd)
def addCharTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()

	querytoExec="create table charity (charid not null, name not null, password not null, address not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def addCharData():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	objtoadd= [('alameda','Alameda County Beautify','password','1627 Alameda County , Oakland , USA'),('berkeleykids','Berkeley Less Able Kids Support','password','67, Shattuck and Telegraph, Berkeley California USA')]
	query='insert into charity values (?,?,?,?)'
	c.executemany('insert into charity values (?,?,?,?)',objtoadd)
def addDealTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()

	querytoExec="create table deals (busid not null, charid not null, dealid not null, dealtext not null, dealdate not null);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()
def getdealdata(dealid):
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	query='select b.name,d.dealid,d.dealtext,b.address,d.dealdate from deals d,business b where d.busid=b.busid and d.dealid=\''+dealid+'\''
	#query='select d.dealid,d.dealdate,d.dealdate,d.dealdate,d.dealdate from deals d where d.dealid=\''+dealid+'\''
	c.execute(query)
	print query
	results = [dict(busname=row[0], dealid=row[1] , dealtext=row[2], busaddress=row[3], dealdate=row[4]) for row in c.fetchall()]
	conn.close()
	print results
	return results
def getdeals():
	#conn = sqlite3.connect(app['DATABASE'])
	conn = sqlite3.connect('app/dbase/localmain.db')
	c = conn.cursor()
	#query='select b.name,d.dealid,d.dealtext,b.address,d.dealdate from deals d,business b where d.busid=b.busid and d.dealid=\''+dealid+'\''
	query='select * from deals'
	c.execute(query)
	print query
	results = [dict(busname=row[0], dealid=row[1] , dealtext=row[2], busaddress=row[3], dealdate=row[4]) for row in c.fetchall()]
	conn.close()
	print results
	return results
def addDealData():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	objtoadd= [('pappy','berkeleykids','deal1','Get 10$ worth free beer - Give 10 $ to Berkeley Kids','2014-10-2'),('pappy','alameda','deal2','Get 10$ worth free beer - Give 10 $ to Alameda County','2014-10-2')]
	query='insert into deals values (?,?,?,?)'
	c.executemany('insert into deals values (?,?,?,?,?)',objtoadd)
	conn.commit()
	conn.close()
def addMappingTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table usermap (uname text not null,role text not null, classname text, mappedteacher text);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def createClassLoginTable(myname):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table loginclass (classname text not null,role not null, login text not null, passw text, mappedteacher text);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()


	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]

def addUser(username,artifact_id):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#objtoadd= [('John','Teacher','class','null'),('Amy','Student','class','John'),('Alice','Student','class','John'),('Mark','Student','class','John'), ('Ben','Student','class','John'),
	#			('Warren','Student','class','John'), ('Tim','Student','class','John'), ('Penny','Student','class','John'), ('Emily','Student','class','John'), ('Judith','Student','class','John'),
	#			('Diana','Student','class','John')]
	#entries=( teachername, studname, objid,'1','2')
	objtoadd =[(username,artifact_id)]

	query='insert into usermap values (?,?)'
	c.execute('insert into usermap values (?,?)',objtoadd)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()

def addUserData():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	)
	#objtoadd= [('RobinWollowski','Teacher','null','null'),('MikeAdams','Teacher','null','null'),('JimmyPage','Teacher','null','null'),('LarryKing','Teacher','null','null')]
	#objtoadd= [('Mark','Student','null','RobinWollowski'),('Viny','Student','null','RobinWollowski'), ('Anand','Student','null','JimmyPage'), ('Bruce','Student','null','RobinWollowski'), ('Andy','Student','null','RobinWollowski'), ('Bradley','Student','null','RobinWollowski'), ('Suhen','Student','null','JimmyPage'), ('Katey','Student','null','JimmyPage'), ('Ashwin','Student','null','RobinWollowski'), ('Carlos','Student','null','JimmyPage'), ('Walt','Student','null','RobinWollowski'), ('Noah','Student','null','RobinWollowski'), ('Adams','Student','null','RobinWollowski'), ('Jacques','Student','null','RobinWollowski'), ('Alex','Student','null','MikeAdams'), ('HurtingFoot','Student','null','MikeAdams'), ('Kiddy','Student','null','MikeAdams')]
	#entries=( teachername, studname, objid,'1','2')
	objtoadd= [('cage101','John Mark','password','1627 University 94703'),('markd','Marko Coy','password','214 University 94703'),('billc','Bill Chambers','password','2333 Shattuck')]

	query='insert into users values (?,?,?,?)'
	c.executemany('insert into users values (?,?,?,?)',objtoadd)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.comaddUserDatamit()
	conn.close()

def addClassLogin():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	)
	#objtoadd= [('RobinWollowski','Teacher','null','null'),('MikeAdams','Teacher','null','null'),('JimmyPage','Teacher','null','null'),('LarryKing','Teacher','null','null')]
	#objtoadd= [('Mark','Student','null','RobinWollowski'),('Viny','Student','null','RobinWollowski'), ('Anand','Student','null','JimmyPage'), ('Bruce','Student','null','RobinWollowski'), ('Andy','Student','null','RobinWollowski'), ('Bradley','Student','null','RobinWollowski'), ('Suhen','Student','null','JimmyPage'), ('Katey','Student','null','JimmyPage'), ('Ashwin','Student','null','RobinWollowski'), ('Carlos','Student','null','JimmyPage'), ('Walt','Student','null','RobinWollowski'), ('Noah','Student','null','RobinWollowski'), ('Adams','Student','null','RobinWollowski'), ('Jacques','Student','null','RobinWollowski'), ('Alex','Student','null','MikeAdams'), ('HurtingFoot','Student','null','MikeAdams'), ('Kiddy','Student','null','MikeAdams')]
	#entries=( teachername, studname, objid,'1','2')
	objtoadd = [('class', 'teacher', 'teacher', 'yapikapi', 'John')]
	objtoadd = [('class', 'student', 'student','hearst','John')]
	c.executemany('insert into loginclass values (?,?,?,?,?)',objtoadd)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()

def addToSatchel(tup):
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	teachername,studname,obid=objid
	#entries=('MRs Robin', 'Jinny', objid,'1','2')
	entries=( tup[0], tup[1])

	query='insert into hearstmain values (?,?)'
	c.execute('insert into hearstmain values (?,?)',entries)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()

def qSatchel():
	conn = sqlite3.connect("app/dbase/localmain.db")
	c = conn.cursor()
	#query='select login,passw,mappedteacher from loginclass'
	query2='select mappedteacher from loginclass where login =? and passw = ?'
	c.execute(query2,('student','hearst'))
	results = [dict(login=row[0]) for row in c.fetchall()]
	print results
	conn.close()
#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
#c.execute(query)
#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]

if __name__ == '__main__':
	"""addTable("")
	addMappingTable("")
	createClassLoginTable("")
	addUserData()conn.cursor()"""
	#qSatchel()
	#conn.close()
	#return results
	#getdealdata('deal1')
	#getdealdata()
	#addTable('bi')
	#addUserData()
	#addDealTable('a')
	#addDealData()
	#addMappingTable("not")
	getdeals()
	"""d= getBuds('aditya')
	for e in d:
		print e['fname']"""