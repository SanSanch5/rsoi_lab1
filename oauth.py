from flask import Flask, redirect, request
import requests
import requests.auth
import json
application = Flask(__name__)

client_id = r"AeMm_oSd9X3-M3eLB_d8UoFcRx_h0OI-8YYCF1889-QFjkjb7HIpYI5QZe3fsWknSDnBJvj0LvvzOZRT"
secret_key = r"EMN0p2OMPBDyPS0Ta1C0qDy4vjDgaXICKUVsMPoL4Jzq7BwdkkVC9Y6tEaN8I7X0LtwQEHX6Yp3va5u6"

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
    print(access_token)
    url = r"https://api.sandbox.paypal.com/v1/identity/openidconnect/userinfo/?schema=openid"
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}


    response = requests.get(url=url, headers=headers)
    if response.status_code // 100 != 2:
        print(response.status_code)
        return "Internal request error"

    text = response.text
    return text

if __name__ == "__main__":
    application.run()

