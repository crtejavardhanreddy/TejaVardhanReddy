from flask import Flask, redirect, url_for

# WSGI Applitaion
app=Flask(__name__)

# Build the URL dynamically
@app.route('/eligible/<int:Age>')
def eligible(Age):
    return 'The user is eligible with '+ str(Age)

@app.route('/noteligible/<int:Age>')
def noteligible(Age):
    return 'The user is not eligible with '+ str(Age)

@app.route('/age/<int:age>')
def Age(age):
    criteria = ''
    if age > 20:
        criteria = 'eligible'
    else:
        criteria = 'noteligible'
    return redirect(url_for(criteria,Age=age))


if __name__=='__main__':
    app.run(port=8080,debug=True, load_dotenv=False)

    # Debug=True , it is used to restart the server automatically