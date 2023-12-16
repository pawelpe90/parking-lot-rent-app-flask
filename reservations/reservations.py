from flask import Blueprint, request, session, render_template, get_flashed_messages
from utils.db_utils import get_free_parking_lots, get_user_reservations

reservations_bp = Blueprint('reservations_endpoints', __name__, template_folder='reservations_templates')


@reservations_bp.route('/rent_from', methods=['GET', 'POST'])
def rent_from_someone():
    # Parametr username przekazywany, aby nie wyświetlać własnego miejsca
    username = session.get('username')
    parking_lots = get_free_parking_lots(username)
    context = {"parking_lots": parking_lots}
    return render_template('rent_from.html', **context)


@reservations_bp.route('/rent_to', methods=['GET', 'POST'])
def rent_to_someone():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('rent_to.html', messages=messages)

    if request.method == 'POST':
        return render_template('rent_to.html')


@reservations_bp.route('/drop_reservation', methods=['GET', 'POST'])
def drop_reservation():
    username = session.get('username')
    reservations = get_user_reservations(username)
    context = {"reserved_parking_lots": reservations}
    return render_template('drop_reservation.html', **context)