 #coding=utf-8

from flask import render_template, flash, redirect,url_for
from app import app
from SQLite import SQLiteOp
from flask import request,session

db = SQLiteOp("LabDB.db")
app.secret_key = '\xe0\xae?\xd8\x18\x9c\xb3\xf5\x9e/3@h1\xbf2\xbb\x1e\xafBOF\xbf\xb4'

@app.before_request
def before_action():        # url的预处理
    print(request.path)
    if request.path.find('.ico') == -1:
        if not request.path == '/login':
            if (not 'id' in session) or (session['id'] == None):
                session['newurl'] = request.path
                return redirect(url_for('login'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

def fetch_password_from_id(id):
    '''在数据库中搜索学号及其对应的密码'''
    fetch_sql = 'SELECT password FROM users WHERE student_number = ? '
    return db.fetch_one_data(fetch_sql,id) 

def fetch_name_from_id(id):
    '''在数据库中搜索学号对应的姓名'''
    fetch_sql = 'SELECT name FROM users WHERE student_number = ? '
    return db.fetch_one_data(fetch_sql,id) 

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    print("===================")
    if request.method == 'POST':
        if request.form['id'] == '':                # 空用户名
            error = u'用户名或密码错误，请重新输入！'
            return render_template('login.html', error=error)
        r_password = fetch_password_from_id(request.form['id'])   # 获取学号对应的密码
        if request.form['password']==r_password:    # 若输入密码与获取的密码对应
            session['id'] = request.form['id']      # 用session传递用户名参数
            session['name'] = fetch_name_from_id(request.form['id'])
            print(session['name'])
            if 'newurl' in session:                 # 判断是否由本网站的其它域名转来
                newurl = session['newurl']
                session.pop('newurl',None)
                return redirect(newurl)
            else:
                return redirect('/home')            # 缺省链接到home
        else:
            error = u'用户名或密码错误，请重新输入！'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html', name=session['name'])