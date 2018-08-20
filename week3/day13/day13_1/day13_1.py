from flask import Flask, render_template, request

mydict = {'name':'고주원','age':24,'school':'한국산업기술대'}
print(mydict)

app = Flask(__name__)

@app.route('/')
def home():
    doc  = {'user':'puppy9207','addr':'서울시 중랑구','phone':'01033819207'}
    return render_template('main.html',doc=doc)
@app.route('/age/<age>')
def score(age):

    return render_template('age.html',age= int(age))

@app.route('/formun')
def formun():
    return render_template('for_main.html')

@app.route('/grade')
def grade():
    return render_template('form_grade.html')

@app.route('/gradeResult', methods=['POST'])
def gradeResult():
    kor = request.form['kor']
    eng = request.form['eng']
    math = request.form['math']
    science = request.form['sci']
    total = int(kor)+int(eng)+int(math)+int(science)
    avg = total/4
    return render_template('grade_result.html',kor=kor,eng=eng,math=math,sci=science,total=total,avg=avg)
if __name__ == '__main__':
    app.run()