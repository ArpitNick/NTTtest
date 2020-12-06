###########################
# Developed by : Arpit Jain
# Maintained by : Arpit Jain
############################

import requests



def test_py_script():
    url = 'http://127.0.0.1:5000/api?interface=FastEthernet3/15'
    url_all = 'http://127.0.0.1:5000/api?interface=all'

    resp = requests.get(url)
    resp_all = requests.get(url_all)

    print("for particular interface :", resp.json())
    print("For all interface :", resp_all.json())


test_py_script()
