from flask import Flask,redirect,url_for

app = Flask(__name__)

app = Flask(__name__)
@app.route('/welcome/<int:passs>')
def welcome(passs):
    return "he was pass"+str(passs)
@app.route('/result/<int:marks>')
def result(marks):
    if marks<50:
        return "he was failed in exams"
    else :
       return redirect(url_for('welcome',passs=marks))

if __name__ == '__main__':
    app.run(debug=True)