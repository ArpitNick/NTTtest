###########################
# Developed by : Arpit Jain
# Maintained by : Arpit Jain
############################

This is flask based application to provide web service api for obtaining functionality to connect the cisshgo router and provide results as per request
This application contains 2 scripts
1 - discovery.py contains flask application to run commands on router and fetch json response based on request
2 - pytest.py script to perform unit test on discovery script


To test the response,Please use below api's after running cisshgo script and discovery.py script
1 - http://127.0.0.1:5000/api?interface=FastEthernet3/15
    To look for a particular interface please edit the interface value in {} and run it without {}
    http://127.0.0.1:5000/api?interface={interface_value}

2 - http://127.0.0.1:5000/api?interface=all
    Use this api url to fetch entire data parsed as json object from browser  directly

once the set up for cisshgo is done you can run discovery.py (After installing all the dependencies) and test it using pytest.py script which will provide you the json response as expected.
