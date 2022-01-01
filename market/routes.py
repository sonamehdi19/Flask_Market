from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm
from market import db 
#db located in init file, thereofre direct import 
@app.route("/")
@app.route("/home")
def home_page():
	return render_template('home.html')

@app.route('/market')
def market_page():
	items = Item.query.all()     #querying all the items in the database 
	return render_template('market.html', items=items)

@app.route("/about/<username>")     #dynamic routing 
def about_page(username):
	return f'<h1>This is the about page of {username} </h1>'

@app.route('/register', methods=['GET', 'POST'])
def register_page():
	form=RegisterForm()
	if form.validate_on_submit():  #if the user clicked the submit button 
		user_to_create=User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)
		db.session.add(user_to_create)
		db.session.commit()
		#if the account is created, redirect to market page 
		return redirect(url_for('market_page'))
	if form.errors !={}:   #if no errors from the validations 
		for err in form_errors.values():
			flash(f'There was error with creating an user account: {err}')
			
	return render_template('register.html', form=form)