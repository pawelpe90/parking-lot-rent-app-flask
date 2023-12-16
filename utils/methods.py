from datetime import datetime
from exceptions import *


def validate_dates(lease_from: str, lease_to: str) -> None:
    today_str = datetime.now().strftime('%Y-%m-%d')
    today = datetime.strptime(today_str, '%Y-%m-%d')
    lease_from = datetime.strptime(lease_from, '%Y-%m-%d')
    lease_to = datetime.strptime(lease_to, '%Y-%m-%d')

    if lease_from > lease_to:
        raise DateToIsBeforeDateFrom
    elif lease_from < today:
        raise DateFromIsBeforeToday
