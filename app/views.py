from flask import render_template,request,session,redirect,jsonify
from flask import url_for
from app import app
import controller
import random



def auth():
	if (session['username']!=""):
		return
	else:
		return redirect(url_for('main'))

@app.route('/index.html', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
	if (session['userid']!=""):
		return render_template('index.html')
	else:
		return render_template('login.html',mesg="")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['userid']=''
	return render_template('login.html',mesg="")



@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		uname= request.form['uname']
		password = request.form['password']
		val=controller.authorise(uname,password)
		if(val==True):
			session['userid']=uname
			return render_template('index.html')
		else:
			return render_template('login.html',mesg="Failed Login !!!")





"""
@app.route('', methods=['GET', 'POST'])
def index():
	return render_template('index.html')"""

@app.route('/busdash', methods=['GET', 'POST'])
def busdash():
	listdeals=controller.getDeals('pappy')
	return render_template('businessdashboard.html',dealList=listdeals)

@app.route('/dashboard.html', methods=['GET', 'POST'])
def dash():
	#listdeals=controller.getDeals('pappy')
	return render_template('dashboard.html')



@app.route('/current.html', methods=['GET', 'POST'])
def current():
	listdeals=controller.getDeals(session['userid'])
	#	results = [dict(busid=row[0], charid=row[1] , dealid=row[2], dealtext=row[3]) for row in c.fetchall()]
	
	return render_template('current.html',dealList=listdeals)



@app.route('/viewdeal/<dealid>')
def viewdeal(dealid):
	dataFordeal=controller.getdealdata(dealid)
	return render_template('viewdeal.html',dealid=dealid,dataFordeal=dataFordeal)


@app.route('/createDeal',methods=['GET', 'POST'])
def createDeal():
	if request.method == 'POST':
		charname= request.form['charity']
		price = request.form['offerCost']
		product = request.form['offerProduct']
		quant = request.form['offerQuant']
		offerdate = request.form['offerDate']
		maxdeal=controller.getMaxDeal()
		dealid=maxdeal[0]['dealid']+str(random.randint(101,200))
		dealstring=charname+"---"+price+"---"+product+"---"+quant+"---"+offerdate
		print dealstring
		session['userid']='pappy'
		dealData=(session['userid'],charname,dealid,dealstring,offerdate)
		controller.insertDeal(dealData)
		return render_template('viewdeal.html',dealid=dealid,dataFordeal=formatDeal(dealstring))

def formatDeal(deal):
	datalist =deal.split('---')
	retval="Donate $ %s to %s ! Get %s %s at %s. All Day %s"%(datalist[1],datalist[0],datalist[3],datalist[2],session['userid'],datalist[4])
	return retval
