from flask import render_template, flash, redirect, url_for, request
from tkrtxt import db, app
from tkrtxt.site import bp
from tkrtxt.models import User
from tkrtxt.site.forms import EditProfileForm
from datetime import datetime
from flask_login import current_user, login_required


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


# Landing page
@bp.route('/')
def index():
    return render_template('home.html')
# Donation page


@bp.route('/donate')
def donate():
    return render_template('donate.html')




# Dashboard
@bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
   
    return render_template('dashboard.html', title='Dashboard')


# User Profile
@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user is current_user:

        return render_template('user.html', user=user)

    return render_template('user.html', user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.', 'success')
        return redirect(url_for('site.user', username=current_user.username))
    elif request.method == 'GET':
        form.about_me.data = current_user.about_me
        return render_template('edit_profile.html', title='Edit Profile', form=form)
