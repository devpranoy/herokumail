from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
import smtplib
import time
from email.Header import Header
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		name=request.form['name']
		email = request.form['email']					#GET FORM FIELDS
		subject= request.form['subject']
		message = request.form['message']
		me = 'sunil@alamrigroup.org' # change to your email
		p_reader = open('password.txt', 'rb') # edit for your password
		cipher = p_reader.read()
		recipients = ['sunil@alamrigroup.org','devpranoy@gmail.com'] # enter recipients here
		msg = message
		msg['Subject'] = Header('Message from alamrigroup.org website', 'utf-8')
		msg['From'] = me
		msg['To'] = ', '.join(recipients)
		s = smtplib.SMTP(host='smtp.gmail.com', port=587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(me, cipher)
		s.sendmail(me, recipients, msg.as_string())
		s.quit()
		return"200 Success"
	return "200"

@app.route('/', methods=['GET','POST'])
def index():
	return "200"


if __name__=='__main__':
	app.secret_key='secret123' #for flash messaging
	app.run(threaded=True) #Debugger is set to 1 for testing and overriding the default port to http port
