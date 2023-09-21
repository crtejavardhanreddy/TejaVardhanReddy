from flask import Flask, redirect, url_for

# WSGI Applitaion
app=Flask(__name__)

# Build the URL dynamically
@app.route('/eligible/<int:age>')
def eligible(age):
    return 'Eligible' if age>20 else 'Not Eligible'

@app.route('/age/<int:age>')
def Age(age):
    criteria = 'eligible'
    return redirect(url_for(criteria,age=age))


if __name__=='__main__':
    app.run(port=8080,debug=True, load_dotenv=False)

    # Debug=True , it is used to restart the server automatically