from methods import validate_dates
import pytest
from exceptions import *


def test_positive():
    lease_from = '2023-12-14'
    lease_to = '2023-12-15'

    validate_dates(lease_from, lease_to)


@pytest.mark.parametrize('lease_from, lease_to', (
        ('2023-12-13', '2023-12-15'),
        ('2023-12-12', '2023-12-13'),
        ('2023-11-12', '2023-12-13'),
        ('2022-11-12', '2023-12-13')
))
def test_invalid_dates_lease_from_is_in_the_past(lease_from, lease_to):
    with pytest.raises(DateFromIsBeforeToday):
        validate_dates(lease_from, lease_to)
