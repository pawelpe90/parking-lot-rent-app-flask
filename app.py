from flask import Flask, render_template, session
from utils.db_utils import get_parking_lot_number, get_user_reservations, get_parking_lot_number_status
from config import Config
from db.db import database_bp
from login.login import login_bp
from reservations.reservations import reservations_bp
from account.account import account_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(database_bp)
app.register_blueprint(login_bp)
app.register_blueprint(reservations_bp)
app.register_blueprint(account_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home_panel')
def home():
    username = session.get('username')

    # Numer własny miejsca parkingowego
    owned_parking_lot = get_parking_lot_number(username)['parking_lot_number']

    # Status własnego miejsca parkingowego (czy ktoś go zarezerwował)
    try:
        owned_parking_lot_status = get_parking_lot_number_status(owned_parking_lot)['taken']
    except TypeError:
        owned_parking_lot_status = 2

    # Własne rezerwacje innych miejsc parkingowych
    reservations = get_user_reservations(username)

    context = {"username": username,
               "owned_parking_lot": owned_parking_lot,
               "owned_parking_lot_status": owned_parking_lot_status,
               "reservations": reservations}

    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
