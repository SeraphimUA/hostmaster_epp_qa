import pytest
import requests

url = 'https://epp-web.hostmaster.ua/'

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

f_dom = Textfile('rdap\\rdap_test_list\\rdap_test_list.txt')
testdata_dom = []
for d in f_dom.entities_list:
    testdata_dom.append((d, 3))

f_con = Textfile('rdap\\rdap_test_contact_list\\rdap_test_contact_list.txt')
testdata_con = []
for c in f_con.entities_list:
    testdata_con.append((c, 3))

@pytest.mark.eppauth
@pytest.mark.parametrize("domain,elapsetime", testdata_dom)
def test_epp_auth_whois_domain(domain, elapsetime, session_eppweb):
    whoisdata = {'object_type': 'domain', 'object_name': domain}
    r_whois = requests.get(f"{url}whois.php", params=whoisdata)
    assert r_whois.elapsed.total_seconds() <= elapsetime

@pytest.mark.eppauth
@pytest.mark.parametrize("contact,elapsetime", testdata_con)
def test_epp_auth_whois_contact(contact, elapsetime, session_eppweb):
    whoisdata = {'object_type': 'contact', 'object_name': contact}
    r_whois = requests.get(f"{url}whois.php", params=whoisdata)
    assert r_whois.elapsed.total_seconds() <= elapsetime

@pytest.mark.eppauth
def test_epp_auth_registrators(session_eppweb):
    request_time_array = []
    for i in range(200):
        r = requests.get(f"{url}registrators/")
        request_time_array.append(r.elapsed.total_seconds())
    print(f"Min = {min(request_time_array)} sec")
    print(f"Max = {max(request_time_array)} sec")
    print(f"Avg = {(sum(request_time_array)/len(request_time_array)):.6f} sec")

@pytest.mark.eppauth
def test_epp_auth_profile(session_eppweb):
    request_time_array = []
    for i in range(200):
        r = requests.get(f"{url}profile.php")
        request_time_array.append(r.elapsed.total_seconds())
    print(f"Min = {min(request_time_array)} sec")
    print(f"Max = {max(request_time_array)} sec")
    print(f"Avg = {(sum(request_time_array)/len(request_time_array)):.6f} sec")
