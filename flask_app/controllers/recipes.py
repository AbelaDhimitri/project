from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new.html', user= User.get_by_id(data))


@app.route('/show/')
def show():
    return render_template('show.html')


@app.route('/edit/')
def edit():
    return render_template('edit.html')


      