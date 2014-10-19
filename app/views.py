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


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


"""
@app.route('', methods=['GET', 'POST'])
def index():
	return render_template('index.html')"""

@app.route('/busdash', methods=['GET', 'POST'])
def busdash():
	listdeals=controller.getDeals('pappy')
	return render_template('businessdashboard.html',dealList=listdeals)

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
		return render_template('viewdeal.html',dealid='a',dataFordeal='a')

def formatDeal(deal):
	datalist =deal.split('---')
