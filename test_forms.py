import pytest
import requests


@pytest.mark.forms
@pytest.mark.parametrize('form_data,must_contain',
    [({'domainname': 'hostmaster', 'ua_public_domains': 'ua'},'domain:'),
    ({'domainname': 'pravda', 'ua_public_domains': 'com.ua'},'domain:'),
    ({'domainname': 'sdvsdvsfv', 'ua_public_domains': 'ua'},'No entries')])
def test_form_whois(form_data, must_contain):
    url = 'https://www.hostmaster.ua/?domadv'
    data_to_send = {'domadv': 1}
    data_to_send.update(form_data)
    r = requests.post(url, data_to_send)
    assert must_contain in r.text

@pytest.mark.forms
@pytest.mark.parametrize('form_data,must_contain',
    [({'nichandle': 'AB143'},'nic-handle:'),
    ({'nichandle': 'ab823'},'nic-handle:'),
    ({'nichandle': 'gergreg'},'не знайдено')])
def test_form_nichandle(form_data, must_contain):
    url = f'https://www.hostmaster.ua/?uanic={form_data["nichandle"]}'
    r = requests.get(url)
    assert must_contain in r.text
