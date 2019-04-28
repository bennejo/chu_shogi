import requests

url = "http://chu-server.herokuapp.com"

def join_game(username):
    payload = {'key':'chu-client', 'user':username}
    result = requests.post(url + "/join", json=payload)
    return result._content

def send_move(username, move):
    move_url = url + "/game/" + username
    payload = {'key':'chu-client', 'move':move}
    result_raw = requests.post(move_url, json=payload)
    result = result_raw._content
    if result[:14] == 'Submitted move':
        return True
    else:
        return False

def get_move(username):
    move_url = url + "/game/" + username
    result_raw = requests.get(move_url)
    result = result_raw._content
    if result[:5] == 'move:':
        return result[:6]
    else:
        return False

# test request result=requests.post("http://chu-server.herokuapp.com/join", json={'key':'chu-client', 'user':'test'})