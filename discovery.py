###########################
# Developed by : Arpit Jain
# Maintained by : Arpit Jain
############################

#!/usr/bin/env python
from netmiko import ConnectHandler
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def mainfunc():
    try:
        interface = request.args['interface']
        device = {
            'device_type': 'cisco_ios',
            'host': '127.0.0.1',
            'port': '10000',
            'username': '',
            'password': 'admin',

        }

        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show ip interface brief")
        print(output)

        output1 = output.split('\n')
        print(output1)

        if interface == 'all':
            result = all(output1)
        else:
            result = search(output1, interface)

    except:
        return "An error occurred with the request, Please check readme instructions again"
    else:
        return jsonify(result)


@app.errorhandler(404)
def invalid_route(e):
    return "Invalid route."


def all(output1):
    result = []
    for x in output1:
        list1 = x.split()
        print(list1)
        if list1 != []:
            if list1[4] != 'up':
                list1[4] = 'administratively down'
            dict1 = {'interface': list1[0],
                     'ip_address': list1[1],
                     'ok': list1[2],
                     'Method': list1[3],
                     'status': list1[4],
                     'protocol': list1[-1]
                     }
            result.append(dict1)
    result.pop(0)
    print(result)
    return result


def search(output2, interface1):
    result = []
    for x in output2:
        list1 = x.split()
        print(list1)
        if list1 != [] and list1[0] == interface1:
            if list1[4] != 'up':
                list1[4] = 'administratively down'
            dict1 = {'interface': list1[0],
                     'ip_address': list1[1],
                     'ok': list1[2],
                     'Method': list1[3],
                     'status': list1[4],
                     'protocol': list1[-1]
                     }
            result.append(dict1)
    return result


if __name__ == '__main__':
    app.run()
