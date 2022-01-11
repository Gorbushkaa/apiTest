import pytest
import requests
import os.path
from datetime import date, timedelta

import test_data.urls as URLS
import test_data.currency_ids as CUR


@pytest.mark.parametrize("cur_id, start_date, end_date, list_is_empty",
                         [(CUR.RUB_ID, date.today() - timedelta(365), date.today() - timedelta(360), False),
                          (0, date.today() - timedelta(365), date.today() - timedelta(360), True),
                          (CUR.RUB_ID, date.today() - timedelta(360), date.today() - timedelta(365), True)
                          ])
def test_rates_dynamics(cur_id, start_date, end_date, list_is_empty):
    response = requests.get(url=os.path.join(URLS.DINAMICS_API_URL, str(cur_id)), params={"startdate": str(start_date),
                                                                                          "enddate": str(end_date)})
    if list_is_empty:
        assert response.json() == []
    else:
        assert response.json()[0]['Cur_ID'] == cur_id
