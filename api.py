from flask import Flask,render_template,request,session,redirect,url_for
from model import check_user,add_user_to_db, add_product_to_db

app= Flask(__name__)
app.secret_key='hello'


@app.route('/')
def home():
	return render_template('home.html',title='home')

@app.route('/about')
def about():
	return render_template('about.html',title='about')

@app.route('/contact')
def contact():
	return render_template('contact.html',title='contact')

@app.route('/addproduct')
def addpro():
	return render_template('addproduct.html',title='addproduc')


@app.route('/add',methods=['GET','POST'])
def add():
	if request.method=='POST':

		product_info = {}

		product_info['pname'] = request.form['pname']
		product_info['pprice'] = request.form['pprice']
		product_info['pdescription'] = request.form['pdescription']
		product_info['sellername'] = request.form['sellername']

		add_product_to_db(product_info)
		return redirect(url_for('home'))

	return redirect(url_for('home'))

@app.route('/signup',methods=['GET','POST'])
def signup():

	if request.method=='POST':

		user_info = {}

		user_info['username'] = request.form['username']
		user_info['fullname'] = request.form['fullname']
		user_info['password'] = request.form['password1']
		rpassword = request.form['password2']
		user_info['email'] = request.form['email']
		user_info['c_type']= request.form['c_type']

		if user_info['password']!=rpassword:
			return "password don't match . Go back and re-enter"

		if bool(check_user(user_info['username'])) is True:
			return "user already exists.Try logging in!"

		if user_info['c_type'] == 'buyer':
			user_info['cart'] = []

		add_user_to_db(user_info)
		return redirect(url_for('home'))

	return redirect(url_for('home'))


@app.route('/login',methods=['GET','POST'])
def login():

	if request.method== 'POST':
		db = {'newuser':'1234','TestUser':'12345','TestUser3':'12345'}

		username =request.form['username']
		password =request.form['password']

		if bool(check_user(username)) and (check_user(username)['password'] == password):
			session['username']=username
			session['c_type'] = check_user(username)['c_type']
			return redirect(url_for('home'))
		return "Username or password incorrect,Try again"
	return redirect(url_for('home'))

@app.route('/logout')
def logout():

	session.clear()
	return redirect(url_for('home'))

app.run(debug=True)