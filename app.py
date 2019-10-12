# -*- coding: utf-8 -*-
# ===============================================================
# Author: David Pedroza Segoviano
# Email: david.pedroza.segoviano@gmail.com
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by David Pedroza (Bubu), for
# his workshop in Forum Tecnológico con PUPAS at León, Gto.
# Any explicit usage of this script or its
# contents is granted according to the license provided and
# its conditions.
# ===============================================================

#Import libraries.
from flask import Flask, render_template, request
from twilio.rest import Client

app = Flask(__name__, template_folder = "templates")

@app.route('/')  
def index():

	return render_template('index.html')

@app.route('/SMS/', methods = ['GET', 'POST'])
def sms():
	account_sid = ""
	auth_token = ""

	client = Client(account_sid, auth_token)
	number = request.form['From']

	call = client.calls.create(
		url = "http://demo.twilio.com/docs/voice.xml",
		to = number,
		from_ = "+1"
		)

	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)
