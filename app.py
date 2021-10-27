from os import name
from flask import Flask, render_template, request, redirect 
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page_load(page_name):
    return render_template(page_name)

def write_to_file(data):
    #open that file in append mode name as database
    with open('database.txt', mode='a') as database:
        #extract the data from the dict/object
        email =data["email"]
        subject=data["subject"]
        message=data["message"]
        #wrote to file
        file=database.write(f'\nemail: {email}, subject: {subject}, message: {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email =data["email"]
        subject=data["subject"]
        message=data["message"]
        #csv write config 
        csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message]) #writerow as a list



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
        #html form method == post if its the case
    if request.method == 'POST':
        try:
            
         #grap the form_data and trs into dictionary
         data=request.form.to_dict()
         #call the write function passing the data 
         write_to_csv(data)
         # redirect thank you page
         return redirect('/thankyou.html')
        except:
            return 'data did not seved'
    else:
        return 'something went wrong!'

if __name__ == '__main__':
 app.run(debug=True)
