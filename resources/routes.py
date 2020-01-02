from flask import render_template, flash, redirect, url_for
from main import app
from resources.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Martynas'}
    cars = [
        {
            'owner': {'username': 'dude'},
            'make': 'mercedes',
            'model': 'e300'
        },
        {
            'owner': {'username': 'Adrianna'},
            'make': 'Renault',
            'model': 'Laguna'
        }
    ]
    return render_template('index.html', title='Home', user=user, cars=cars)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)