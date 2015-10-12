from flask import Flask, redirect, request
import requests
import requests.auth
import json
application = Flask(__name__)

client_id = r"AasGhRDDdldHbebf_8vpMjQGQW7ejunpyr9KEJE2-39ruztvgMWRczvPJfpB"
secret_key = r"ELcdKxBW53TZj8iqVR8nbBJpDA98eKnO0--71Eog0MoN3ZBamCQaUPy7l0bf"

redirect_uri = r"http://127.0.0.1:5000/app"

@application.route("/")
def index():
    url = r"https://www.sandbox.paypal.com/webapps/auth/protocol/openidconnect/v1/authorize"
    resp_type = "code"
    scope = "openid"
    reqtext = url + "?" + "client_id=" + client_id + "&response_type=" + resp_type + "&scope=" + scope + "&redirect_uri=" + redirect_uri
    return redirect(reqtext, 302)

@application.route("/app", methods=['GET'])
def app():
    code = request.args.get('code')
    if code is None:
        return "bad request"

    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    url = r'https://api.sandbox.paypal.com/v1/identity/openidconnect/tokenservice'
    params = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': redirect_uri}

    response = requests.post(url=url, auth=auth, data=params)
    if response.status_code // 100 != 2:
        return "Wrong auth"

    access_token = response.json()["access_token"]
    url = r"https://api.sandbox.paypal.com/v1/identity/openidconnect/userinfo/?schema=openid"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    response = requests.get(url=url, headers=headers)
    if response.status_code/100 != 2:
        return "Internal request error"

    text = response.text
    d = json.loads(text)
    return d["user_id"]

if __name__ == "__main__":
    application.run()

