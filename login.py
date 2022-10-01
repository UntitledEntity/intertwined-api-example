import requests

data = { "type": "init", "appid" : "APPIDHERE" }

init_ret = requests.post("https://intertwined.solutions/api/", data=data)
json = init_ret.json()

if json['success'] == False:
    print("Unable to initiate.")
    exit()

sid = json['sessionid']
print("Session ID: ", sid)

username = input('Username: ')
password = input('Password: ')

data = { "type": "login", "sid" : sid, "user" : username, "pass" : password }

login_ret = requests.post("https://intertwined.solutions/api/", data=data)
json = login_ret.json()

if json['success'] == False:
    data = { "type": "close", "sid" : sid }
    close_ret = requests.post("https://intertwined.solutions/api/", data=data)
    print("Login Error: ", json['error'])
    exit()

print("Successfully logged in!")

print("User data: ", json['data'])

data = { "type": "close", "sid" : sid }
close_ret = requests.post("https://intertwined.solutions/api/", data=data)

exit()
