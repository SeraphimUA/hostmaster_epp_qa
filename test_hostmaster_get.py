import pytest
import requests

@pytest.mark.getquery
def test_hostmaster_enter():
    r = requests.get('https://www.hostmaster.ua/')
    assert r.status_code == 200