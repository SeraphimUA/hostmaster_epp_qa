import pytest
import requests
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import readfile

url = 'https://rdap.hostmaster.ua/domain/'
url_a = 'https://rdap-a.hostmaster.ua/domain/'
url_s = 'https://rdap-s.hostmaster.ua/domain/'
url_i = 'https://rdap-i.hostmaster.ua/domain/'
f = readfile.Textfile('rdap\\rdap_test_list\\rdap_test_list.txt')
testdata = []
for d in f.entities_list:
    testdata.append((d, 200))

wrongtestdata = [('漢人', 400), ('mon.gov.ua', 501), ('ad_at.ua', 400), ('cnn.com', 400)]
randomstrings = ['Ny758UzT(q*BwCQ4d-L*(L@&', 'pa)xUe5!69uDe2+&MR1t3Skl', 'V=V43VKOxPCFa18d1*?UM5wW', '!B44@LMO!P2LBYX@*z-!-8&j', 'g4egX0x($gE7C6b9cVvQxN-L', '^ACU_Yts*kQ7zNxzN4H.JPR.', 'sOl*~y1oh?ivz$zmom^Y^2OH', 'o%ltzt&BBfAwrk.1gG8t1EIN', 'xWF%CnScPV9*Usmi&JSNW4%%b', '_I?s40#*0i+-$KNF*PkHf7Cl']
for randstr in randomstrings:
    wrongtestdata.append((randstr, 400))

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", testdata)
def test_rdap(domain, status_code):
    r = requests.get(url + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", testdata)
def test_rdap_a(domain, status_code):
    r = requests.get(url_a + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", testdata)
def test_rdap_s(domain, status_code):
    r = requests.get(url_s + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", testdata)
def test_rdap_i(domain, status_code):
    r = requests.get(url_i + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", wrongtestdata)
def test_rdap_wrong(domain, status_code):
    r = requests.get(url + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", wrongtestdata)
def test_rdap_a_wrong(domain, status_code):
    r = requests.get(url_a + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", wrongtestdata)
def test_rdap_s_wrong(domain, status_code):
    r = requests.get(url_s + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", wrongtestdata)
def test_rdap_i_wrong(domain, status_code):
    r = requests.get(url_i + domain)
    assert r.status_code == status_code
