from flask import Blueprint, redirect, render_template, session, url_for

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/signIn')
def signIn():
    return render_template('signIn.html')


@views.route('/signUp')
def signUp():
    return render_template('signUp.html')

@views.route('/dashboard')
def dashboard():
    # Check if user is loggedin
    if 'loggedin' in session:
        userId = session['userId']
        userRole = session['userRole']
        username = session['username']
        return render_template('dashboard.html', userId = userId, userRole=userRole, username=username)
    else:
        # User is not loggedin redirect to login page
        return redirect(url_for('signIn'))
    
@views.route('/dashboard/customerList')
def userList():
    # Check if user is loggedin
    if 'loggedin' in session:
        userRole = session['userRole']
        username = session['username']
        return render_template('customerList.html', userRole=userRole, username=username)
    else:
        # User is not loggedin redirect to login page
        return redirect(url_for('signIn'))
    
@views.route('/dashboard/itemList')
def itemList():
    # Check if user is loggedin
    if 'loggedin' in session:
        userRole = session['userRole']
        username = session['username']
        return render_template('itemList.html', userRole=userRole, username=username)
    else:
        # User is not loggedin redirect to login page
        return redirect(url_for('signIn'))