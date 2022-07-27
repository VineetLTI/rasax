import requests

def api_banking():
    
    api_address='https://e4cw4re4t0.execute-api.us-west-2.amazonaws.com/test-sg/balance-info'
    json_data = requests.get(api_address).json()
    format_msg = "Hey, " + json_data['message'] + "  It is " + json_data['balance'].strip("Current balance ")
    # print("Hey, " + json_data['message'] + "  It is " + json_data['balance'].strip("Current balance ")) 
    print(format_msg)
    return format_msg