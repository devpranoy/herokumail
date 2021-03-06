from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
import sendgrid
import os
from sendgrid.helpers.mail import *


app = Flask(__name__)

@app.route('/send', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		name=request.form['name']
		email = request.form['email']					#GET FORM FIELDS
		subject= request.form['subject']
		message = request.form['message']
		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
		from_email = Email("website@my_website.org")
		to_email = Email("reciever@email.com")
		subject = str(subject)
		content = Content("text/plain", str(message)+"\n\n Message by "+name+"\n\n Email id "+email)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)
		return"200 Success"
	return "200"

@app.route('/', methods=['GET','POST'])
def index():
	return "200"


if __name__=='__main__':
	app.secret_key='secret123' #for flash messaging
	app.run(threaded=True) #Debugger is set to 1 for testing and overriding the default port to http port
