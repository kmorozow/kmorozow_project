from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy

from service import authorizationService
from service import changeTimetableService
from service import registrationService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(DEBUG=True, SECRET_KEY='secretkey',
                  USERNAME='admin', PASSWORD='admin')
db = SQLAlchemy(app)


app.register_blueprint(registrationService.mod)
app.register_blueprint(authorizationService.mod

app.register_blueprint(changeTimetableService.mod)


@app.route('/')
def main():
    #session.clear()
    return render_template('hello.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000, debug=True)
