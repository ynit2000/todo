from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import jinja2
import json


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/todos'
mongo = PyMongo(app)

@app.route('/')
def index():
     user_email = request.args.get('user')
     # print(user_email)
     login = request.args.get('login')
     # print(login)
     users=mongo.db.users.find()
     for user in users:
          if user['email']==user_email:
               name=user['name']
               data_list = [{"title": item["title"], "_id": item["_id"]} for item in user['task']]
               return render_template('index.html',name=name, tasks=data_list,email=user['email'],login=login)
     return render_template('login.html',user_not_exit=1)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginn', methods=['POST'])
def loginn():
     email=request.form.get('email')
     password=request.form.get('pas')
     users=mongo.db.users.find()
     for user in users:
          if user['email']==email and user['password']==password:
               return redirect(url_for('index',user=email,login=1))
     return render_template('login.html',user_not_exist=1)
   
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerr',methods=['POST'])
def registerr():
     name=request.form.get('name')
     email=request.form.get('emaill')
     password=request.form.get('pass')
     cpassword=request.form.get('cpass')
     task=[]
     ale=password==cpassword
     if ale:
          if name and email and password:
               users=mongo.db.users.find()
               for user in users:
                    if user['email']==email:
                         user_exist=email==user['email']
                         return render_template('register.html',user_exist=user_exist)
               mongo.db.users.insert_one({'name':name,'email':email,'password':password,'task':task})
               return redirect(url_for('login'))
     else:
          return render_template('register.html',alr=ale)
        
@app.route('/add_task/<string:email>', methods=['POST'])
def add_task(email):
     title = request.form.get('title')
     users=mongo.db.users
     result = users.update_one({"email": email},{"$push": {"task":{'title': title,'_id':ObjectId()}}})
     return redirect(url_for('index',user=email))

@app.route('/update_task/<string:email>/<string:_id>', methods=['POST'])
def update_task(email,_id):
     title = request.form.get('title')
     if title:
          document_id = ObjectId(_id)
          mongo.db.users.update_one({'email':email,'task._id': document_id}, {'$set': {'task.$.title': title}})
     return redirect(url_for('index',user=email))

@app.route('/delete_task/<string:email>/<string:_id>')
def delete_task(email,_id):
    document_id = ObjectId(_id)
    mongo.db.users.update_one({'email':email},{"$pull": {"task": {"_id": document_id}}})
    return redirect(url_for('index',user=email))

if __name__ == '__main__':
    app.run(debug=True)
