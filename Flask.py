# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:31:26 2020

@author: Bazif
"""
from redditdownloader import download_helper
from flask import Flask, request, render_template
import time
import os
def initiate_engine(path,speed=100,subreddit="wallpapers"):

    download_helper(i_speed=speed,subreddit=subreddit)



from flask import Flask
import webbrowser
import threading
app = Flask(__name__)


def start_app():
    app.run()

def open_browser():
    webbrowser.open("http://localhost:5000")

@app.route("/")
def main_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    global t_down 
    speed = request.form['speed']
    path = request.form['path']
    subreddit = request.form['subreddit']
    if(not os.path.exists(path)):
        return "Path Invalid"
    t_down = threading.Thread(target=initiate_engine,args=(path,int(speed),subreddit,))
    t_down.start()
    return render_template("pg2.html")

if __name__ == '__main__':
        t_browser=threading.Thread(target=open_browser)
        t_server=threading.Thread(target=start_app)
        t_server.start()
        time.sleep(2)
        t_browser.start()
        t_server.join()
        t_browser.join()
        #initiate_engine(subreddit="wallpapers")
