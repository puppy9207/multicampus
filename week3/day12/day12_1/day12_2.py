from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form_submit.html')

@app.route('/result',methods=['POST'])
def action():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phoneNumber']
    message = request.form['Message']
    result = [name,email,phone,message]
    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run()