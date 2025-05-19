import pytest
import requests

f = open('authdata.txt', 'r')
authdata = f.readlines()

url1 = 'https://epp.hostmaster.ua/'
url2 = 'https://epp-web.hostmaster.ua/'
nickname = authdata[0]
pword = authdata[1]
authdata = {'username': nickname, 'password': pword}


@pytest.fixture
def session_epp():
    session = requests.Session()
    r = session.post(f"{url1}auth/", data=authdata)
    cookies = session.cookies.get_dict()

    yield session

    session.close()


@pytest.fixture
def session_eppweb():
    session = requests.Session()
    r = session.post(f"{url2}auth/", data=authdata)
    cookies = session.cookies.get_dict()

    yield session

    session.close()
