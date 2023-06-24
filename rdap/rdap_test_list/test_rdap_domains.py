import pytest
import requests
from rdap.readfile import Textfile

url = 'https://rdap.hostmaster.ua/domain/'
f = Textfile('rdap\\rdap_test_list\\rdap_test_list.txt')
testdata = []
for d in f.entities_list:
    testdata.append((d, 200))

wrongtestdata = [('漢人', 400), ('mon.gov.ua', 404), ('ad_at.ua', 400), ('cnn.com', 400)]
randomstrings = ['Ny758UzT(q*BwCQ4d-L*(L@&', 'pa)xUe5!69uDe2+&MR1t3Skl', 'V=V43VKOxPCFa18d1*?UM5wW', '!B44@LMO!P2LBYX@*z-!-8&j', 'g4egX0x($gE7C6b9cVvQxN-L', '^ACU_Yts*kQ7zNxzN4H.JPR.', 'sOl*~y1oh?ivz$zmom^Y^2OH', 'o%ltzt&BBfAwrk.1gG8t1EIN', 'xWF%CnScPV9*Usmi&JSNW4%%b', '_I?s40#*0i+-$KNF*PkHf7Cl']
for randstr in randomstrings:
    wrongtestdata.append((randstr, 400))

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", testdata)
def test_rdap(domain, status_code):
    r = requests.get(url + domain)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("domain,status_code", wrongtestdata)
def test_rdap_wrong(domain, status_code):
    r = requests.get(url + domain)
    assert r.status_code == status_code
