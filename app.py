from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		name=request.form['name']
		email = request.form['email']					#GET FORM FIELDS
		subject= request.form['subject']
		message = request.form['message']
	return name,email,subject,message

if __name__=='__main__':
	app.secret_key='secret123' #for flash messaging
	app.run(threaded=True) #Debugger is set to 1 for testing and overriding the default port to http port
