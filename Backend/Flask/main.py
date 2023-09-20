from flask import Flask

# WSGI Applitaion
app=Flask(__name__)

@app.route('/')
def Welcome():
    return "Hi My name is Teja Hell"

@app.route('/info')
def Info():
    return "I am working at InfobellIT solutions"


if __name__=='__main__':
    app.run(port=8080,debug=True, load_dotenv=False)

    # Debug=True , it is used to restart the server automatically