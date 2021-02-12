#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#creates a connection to the MongoDB.
#make sure you have the correct URL.  If the MongoDB and Flask
#are not on the same server, you will need to put an IP address
#instead of localhost
app.config["MONGO_URI"] = "mongodb://localhost:27017/temperature"
mongo = PyMongo(app)

#create the "index" or "root" level of the website.
#this is the "home page"
@app.route('/')        #the root route, for example: 192.168.56.108/
@app.route('/index/')  #the root route, for example: 192.168.56.108/
def index():
    #when a user browses the root of the site, Flask returns a "template"
    #html file name index.html.  This page is a static page.
    #look for it under the "templates" directory
    return render_template('index.html') 

#define another route.  Here Flask will query the MongoDB, grab the most recent
#temperature reading and return it as JSON back to the user.
#this is not intended to be used by a person.  Instead this is an API that another
#system for example would use to query the database.
@app.route("/get_one_temp_api")
def temp1():
    one_temp = mongo.db.temperature.find_one()
    return str(one_temp)

#same as above, just returns the most recent 10 temperatures in the database as 
#JSON objects.
@app.route("/get_ten_temps_api")
def temp10():
    temps = ""
    ten_temps = mongo.db.temperature.find().limit(10)
    for temp in ten_temps:
        temps=temps+str(temp)
        print(temps)
    return temps

#this is the site's one human readable page.
#queries the db and returns a table of 10 temps.
@app.route("/recent_temps")
def recent():
    temps = mongo.db.temperature.find().limit(10)
    
    return render_template('temps.html',temps=temps)

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyonepy