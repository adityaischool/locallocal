from flask import render_template,request,session,redirect,jsonify
from flask import url_for
from app import app
import controller



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