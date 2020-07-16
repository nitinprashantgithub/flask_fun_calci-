from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS, cross_origin
import requests
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # To render Homepage
@cross_origin()
def home_page():
    return render_template('index.html')
@app.route('/math', methods=['POST'])  # This will be called from UI
@cross_origin()
def math_operation():
    if (request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 / num2
            result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html',result=result)
port = os.getenv("PORT")
if __name__ == '__main__':
	if port is None:
		app.run(host='0.0.0.0', port=5000, debug=True)
	else:
		app.run(host='0.0.0.0', port=int(port), debug=True)