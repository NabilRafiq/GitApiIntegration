from flask import Flask, redirect, request, jsonify
import requests
import base64
from urllib.parse import parse_qs

app = Flask(__name__)
GITHUB_CLIENT_ID = GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET = GITHUB_CLIENT_SECRET
GITHUB_REDIRECT_URI = 'http://localhost:8000/callback'
token_url = 'https://github.com/login/oauth/access_token'
authorize_url = 'https://github.com/login/oauth/authorize'
params = {
    'client_id': GITHUB_CLIENT_ID,
    'response_type': 'code',
    'redirect_uri': GITHUB_REDIRECT_URI,
    'scope': 'user-read-private user-read-email',
    'state': 'asdfasfsaf'
}

@app.route('/')
def home():
    authorization_url = f"{authorize_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code:
        auth_header = base64.b64encode(f"{GITHUB_CLIENT_ID}:{GITHUB_CLIENT_SECRET}".encode()).decode()
        headers = {
            'Authorization': f"Basic {auth_header}"
        }

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': GITHUB_REDIRECT_URI
        }

        response = requests.post(token_url, data=data, headers=headers)

        # Parse the URL-encoded response
        parsed_response = parse_qs(response.text)

        # Extract the access token
        access_token = parsed_response.get('access_token', [''])[0]

        if access_token:
            return jsonify({"Access Token": access_token,'Authorization Token':code})
        else:
            return jsonify({"error": "Access token not found in the response."})
    else:
        return jsonify({"error": "Authorization code not found."})
    
if __name__ == '__main__':
    app.run(port=8000)
