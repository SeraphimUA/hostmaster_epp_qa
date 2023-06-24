import pytest
import requests

url1 = 'https://epp.hostmaster.ua/'
url2 = 'https://epp-web.hostmaster.ua/'

@pytest.mark.epp
def test_epp_massrequest():
    request_time_array = []
    for i in range(200):
        r = requests.get(url1)
        request_time_array.append(r.elapsed.total_seconds())
    print(f"Min = {min(request_time_array)} sec")
    print(f"Max = {max(request_time_array)} sec")
    print(f"Avg = {sum(request_time_array)/len(request_time_array)} sec")

@pytest.mark.epp
def test_eppweb_massrequest():
    request_time_array = []
    for i in range(200):
        r = requests.get(url2)
        request_time_array.append(r.elapsed.total_seconds())
    print(f"Min = {min(request_time_array)} sec")
    print(f"Max = {max(request_time_array)} sec")
    print(f"Avg = {sum(request_time_array)/len(request_time_array)} sec")
