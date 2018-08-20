from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    a='data'
    c=0
    for i in range(1,101):
        c += i
    return render_template('index_main.html', a=a, c=c)

@app.route('/cal')
def cal():
    a = 5
    b = 6
    result = a+b
    return render_template('f_07_cal.html',result = result)
import random

@app.route('/gift/<username>')
def gift(username):
    a = ['꽝','꽝','꽝','꽝','꽝','에어컨','선풍기']
    b = random.choice(a)
    return render_template('gift.html',b = b, username = username)
if __name__ == '__main__':
    app.run()