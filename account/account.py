from flask import Blueprint, render_template, request, get_flashed_messages

account_bp = Blueprint('account_endpoints', __name__, template_folder='account_templates')


@account_bp.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'GET':
        messages = get_flashed_messages()
        return render_template('create_account.html', messages=messages)

    if request.method == 'POST':
        return render_template('create_account.html')
