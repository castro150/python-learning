from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from werkzeug import secure_filename
from send_email import send as send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ra102030@localhost/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def receive_data():
    global file
    if request.method == 'POST':
        # email = request.form['email_name']
        # height = request.form['height_name']
        # if db.session.query(Data).filter(Data.email == email).count() == 0:
        #     db.session.add(Data(email, height))
        #     db.session.commit()
        #     average_height = round(db.session.query(func.avg(Data.height)).scalar(), 1)
        #     count = db.session.query(Data.height).count()
        #     send_email(email, height, average_height, count)
        #     return render_template('success.html')
        file = request.files['file_name']
        file.save(secure_filename('uploaded' + file.filename))
        with open('uploaded' + file.filename, 'a') as f:
            f.write('This was added later!')
        return render_template('index.html', btn='download.html')
    return render_template('index.html', text='Seems like we have got something from that email already!')


@app.route('/download')
def download():
    return send_file('uploaded' + file.filename, attachment_filename='your_file.csv', as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    app.run()
