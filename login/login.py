from flask import Blueprint, request, redirect, session, url_for, flash, render_template, get_flashed_messages
from utils.db_utils import get_connection
from werkzeug.security import check_password_hash

login_bp = Blueprint('login_endpoints', __name__, template_folder='login_templates')


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('login.html', messages=messages)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        c = conn.cursor()

        result = c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = result.fetchone()

        if user_data:
            hashed_password = user_data['password']

            if check_password_hash(hashed_password, password):
                session['user_id'] = user_data['id']
                session['username'] = user_data['username']
                return redirect(url_for('home'))

        flash('błędna nazwa użytkownika lub hasło')
        return redirect(url_for('login_endpoints.login'))


@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
