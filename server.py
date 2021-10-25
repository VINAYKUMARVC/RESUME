from flask import Flask, render_template, request
import csv
app = Flask(__name__)

@app.route ('/')
def home1 ():
	return render_template ('index.html')

@app.route ('/<string:page_name>')
def html_page (page_name):
	return render_template (page_name)

def write_to_file (data):
	with open('database.txt',mode = 'a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n {email},{subject},{message}')

def write_to_csv (data):
	with open('database.csv', mode = 'a') as database1:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database1, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL) 
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file (data)
		write_to_csv(data)
		return 'form_submitted'
	else:
		return 'Some thing went wrong ... Try again'

    

if __name__ == '__main__':
	app.run (debug = True)