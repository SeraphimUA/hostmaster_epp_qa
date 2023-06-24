import pytest
import requests
from rdap.readfile import Textfile

url = 'https://rdap.hostmaster.ua/entity/'
f = Textfile('rdap\\rdap_test_contact_list\\rdap_test_contact_list.txt')
testdata = []
for c in f.entities_list:
    testdata.append((c, 200))

wrongtestdata = [('漢人', 400), ('xxx', 404)]
randomstrings = ['G%%f*$f$D&hy_Sx.!', '9_mAThl_=B?uc^lB', 'E33F7T6F%=R$vyZb', '9uME+6KGz!FEvFsX', 'DxV)j?z~lUte8_(I', '(j.yg&^AbWt#GSWQ', 'KUfiSbvtcXG#x&dy', 'U2km-Tf!GC^eNd-+', 's8IE$XWkn+Vz43Vi', 'd$lW9t7xkZjvRh%%e']
for randstr in randomstrings:
    wrongtestdata.append((randstr, 400))

@pytest.mark.rdap
@pytest.mark.parametrize("contact,status_code", testdata)
def test_rdap(contact, status_code):
    r = requests.get(url + contact)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("contact,status_code", wrongtestdata)
def test_rdap_wrong(contact, status_code):
    r = requests.get(url + contact)
    assert r.status_code == status_code
