## Integrate HTML with Flask

# GET and POST

from flask import Flask, redirect, url_for, render_template, request

# WSGI Applitaion
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Build the URL dynamically
# @app.route('/success/<int:score>')
# def success(score):
#     return 'The user is passed with '+ str(score)
    
@app.route('/fail/<int:score>')
def fail(score):
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',result = res, marks =score)


# @app.route('/results/int:marks>')
# def results(marks):
#     result = ""
#     if marks < 50:
#         result = 'fail'
#     else:
#         result = "success"
#     return redirect(result,score = marks)

# Result checker HTML pscore
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form["maths"])
        datascience = float(request.form["datascience"])
        c = float(request.form["c"])
        total_score = (science + maths + datascience + c)/4
    return redirect(url_for('fail',score = total_score))



if __name__=='__main__':
    app.run(port=8080,debug=True, load_dotenv=False)

    # Debug=True , it is used to restart the server automatically