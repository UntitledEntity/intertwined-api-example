import requests

data = { "type": "init", "appid" : "APPIDHERE" }

init_ret = requests.post("https://intertwined.solutions/api/", data=data)
json = init_ret.json()

if json['success'] == False:
    print("Unable to initiate.")
    exit()

sid = json['sessionid']
print("Session ID: ", sid)

username = input("Username:")
license = input("License:")

data = { "type": "upgrade", "sid" : sid, "user" :  username, "license" : license }

upgrade_ret = requests.post("https://intertwined.solutions/api/", data=data)
json = upgrade_ret.json()

print(json)