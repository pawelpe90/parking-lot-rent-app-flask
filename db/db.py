from flask import Blueprint, request, redirect, session, url_for, flash, render_template
from utils.db_utils import get_connection, get_parking_lot_number
from utils.methods import validate_dates
import sqlite3
from pydantic import ValidationError
from models import User
from werkzeug.security import generate_password_hash
from exceptions import *

database_bp = Blueprint('database_endpoints', __name__, template_folder='db_templates')


@database_bp.route('/reserve', methods=['GET', 'POST'])
def reserve_parking_lot():
    username = session.get('username')
    parking_lot_id = int(request.form['id'])
    parking_lot_number = int(request.form['number'])

    conn = get_connection()
    c = conn.cursor()

    c.execute("""UPDATE "parking_lots" SET "taken" = 1, "taken_by" = ? WHERE "id" = ?""", (username, parking_lot_id))
    conn.commit()

    return render_template('reservation_confirm.html', parking_lot_number=parking_lot_number)


@database_bp.route('/lease', methods=['GET', 'POST'])
def lease_parking_lot():
    username = session.get('username')
    lease_from = request.form['from']
    lease_to = request.form['to']
    parking_lot_number = get_parking_lot_number(username)['parking_lot_number']

    try:
        validate_dates(lease_from, lease_to)
    except DateToIsBeforeDateFrom:
        flash(f'BŁĘDNE DANE. Data zakończenia nie może być wcześniej niż data rozpoczęcia!')
        return redirect(url_for('reservations_endpoints.rent_to_someone'))
    except DateFromIsBeforeToday:
        flash(f'BŁĘDNE DANE. Data rozpoczęcia nie może być starsza od daty dzisiejszej!')
        return redirect(url_for('reservations_endpoints.rent_to_someone'))
    except ValueError:
        flash('BŁĄD. Podaj poprawne dane.')
        return redirect(url_for('reservations_endpoints.rent_to_someone'))

    conn = get_connection()

    query = """INSERT INTO "parking_lots" ('parking_lot_number', 'taken_by', 'start_date', 'end_date') 
    VALUES (?, ?, ?, ?)"""
    params = (parking_lot_number, '', lease_from, lease_to)

    try:
        conn.execute(query, params)
        conn.commit()

        return render_template('lease_confirm.html', lease_from=lease_from, lease_to=lease_to)

    except sqlite3.IntegrityError:
        return redirect('/rent_to')


@database_bp.route('/drop', methods=['GET', 'POST'])
def drop_parking_lot():
    parking_lot_id = int(request.form['id'])
    parking_lot_number = int(request.form['number'])

    conn = get_connection()
    c = conn.cursor()

    c.execute("""UPDATE "parking_lots" SET "taken" = 0, "taken_by" = '' WHERE "id" = ?""", (parking_lot_id,))
    conn.commit()

    return render_template('drop_confirm.html', parking_lot_number=parking_lot_number)


@database_bp.route('/create_user_account', methods=['GET', 'POST'])
def create_user_account():
    data_from_user = {
        'name': request.form.get('name'),
        'surname': request.form.get('surname'),
        'username': request.form.get('username'),
        'email': request.form.get('email'),
        'phone': request.form.get('phone'),
        'password': request.form.get('password'),
        'parking_lot_number': request.form.get('parking_lot_number')
    }

    try:
        user = User.model_validate(data_from_user)
    except ValidationError as e:
        for error in e.errors():
            location = error['loc']
            message = error['msg']
            flash(f'Zła wartość w polu: {location[0]}. Wskazówka: {message}')

        return redirect(url_for('account_endpoints.create_account'))

    hashed_password = generate_password_hash(user.password)

    query = """INSERT INTO "users" ('username', 'password', 'name', 'surname', 'parking_lot_number', 'email', 'phone')
    VALUES (?, ?, ?, ?, ?, ?, ?)"""
    params = (user.username, hashed_password, user.name, user.surname, user.parking_lot_number, user.email, user.phone)

    conn = get_connection()

    try:
        conn.execute(query, params)
        conn.commit()

        return render_template('create_account_confirm.html', username=user.username)

    except sqlite3.IntegrityError:
        return redirect('/create_account')
