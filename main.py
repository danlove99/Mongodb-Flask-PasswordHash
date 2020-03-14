from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request, redirect, session
from hashPassword import hashPassword
import pymongo

# Create the database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


dblist = myclient.list_database_names()
'''if "UserInfo" in dblist:
	pass
else:'''
mydb = myclient["UserInfo"]
users = mydb["users"]



class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        result = hashPassword(request.form.get('password'))
        tmp_dict = {'username' : request.form.get('username'),
        'password': result}
        entry = users.insert_one(tmp_dict)
        print(users.find_one())
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == "__main__":
	app.run()