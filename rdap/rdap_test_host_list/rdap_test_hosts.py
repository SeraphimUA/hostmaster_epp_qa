import pytest
import requests
# from rdap.readfile import Textfile

class Textfile:
    def __init__(self, filename):
        f = open(filename, 'r')
        entities_list = f.readlines()
        self.entities_list = []
        for d in entities_list:
            self.entities_list.append(d.strip())
        f.close()

    def print_list(self):
        print(self.entities_list)

url = 'https://rdap.hostmaster.ua/nameserver/'
f1 = Textfile('rdap\\rdap_test_host_list\\rdap_test_host1_list.txt')
testdata = []
for h in f1.entities_list:
    testdata.append((h, 200))

f2 = Textfile('rdap\\rdap_test_host_list\\rdap_test_host2_list.txt')
testdata_notexists = []
for h in f2.entities_list:
    testdata_notexists.append((h, 404))

# wrongtestdata = [('漢人', 400), ('xxx', 404)]
# randomstrings = ['G%%f*$f$D&hy_Sx.!', '9_mAThl_=B?uc^lB', 'E33F7T6F%=R$vyZb', '9uME+6KGz!FEvFsX', 'DxV)j?z~lUte8_(I', '(j.yg&^AbWt#GSWQ', 'KUfiSbvtcXG#x&dy', 'U2km-Tf!GC^eNd-+', 's8IE$XWkn+Vz43Vi', 'd$lW9t7xkZjvRh%%e']
# for randstr in randomstrings:
#     wrongtestdata.append((randstr, 400))

@pytest.mark.rdap
@pytest.mark.parametrize("host,status_code", testdata)
def test_rdap(host, status_code):
    r = requests.get(url + host)
    assert r.status_code == status_code

@pytest.mark.rdap
@pytest.mark.parametrize("host,status_code", testdata_notexists)
def test_rdap_wrong(host, status_code):
    r = requests.get(url + host)
    assert r.status_code == status_code
