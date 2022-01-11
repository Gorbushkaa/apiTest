import pytest
import requests
from http import HTTPStatus
import os.path
from datetime import date, timedelta

import test_data.urls as URLS
import test_data.currency_ids as CUR


@pytest.mark.parametrize("cur_id, ondate ,response_code", [(CUR.RUB_ID, date.today() - timedelta(365), HTTPStatus.OK),
                                                           (0, date.today() - timedelta(365), HTTPStatus.NOT_FOUND),
                                                           (CUR.RUB_ID, date.today(), HTTPStatus.NOT_FOUND),
                                                           (CUR.RUB_ID, 'today', HTTPStatus.BAD_REQUEST),
                                                           ("One", date.today() - timedelta(365), HTTPStatus.BAD_REQUEST)])
def test_rates(cur_id, ondate, response_code):
    response = requests.get(url=os.path.join(URLS.RATES_API_URL, str(cur_id)), params={"ondate": str(ondate)})
    assert response.status_code == response_code
    if response_code == HTTPStatus.OK:
        assert response.json()['Cur_ID'] == cur_id
