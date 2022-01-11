import pytest
import requests
from http import HTTPStatus
import os.path

import test_data.urls as URLS
import test_data.currency_ids as CUR


@pytest.mark.parametrize("cur_id, response_code", [(CUR.RUB_ID, HTTPStatus.OK),
                                                   (0, HTTPStatus.NOT_FOUND),
                                                   ('One', HTTPStatus.BAD_REQUEST)])
def test_currencies(cur_id, response_code):
    response = requests.get(url=os.path.join(URLS.CURRENCIES_API_URL, str(cur_id)))
    assert response.status_code == response_code
    if response_code == HTTPStatus.OK:
        assert response.json()['Cur_ID'] == cur_id
