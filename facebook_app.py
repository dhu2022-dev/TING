from flask import Flask, jsonify, request, redirect, url_for, render_template
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN') #Access token expires EVERY HOUR, data expires EVERY 3 MONTHS

@app.route('/')
def index():
    return render_template('index.html')

page_id = 'ARTIST_PAGE_ID'

def get_page_info(page_id):
    url = f'https://graph.facebook.com/v12.0/{page_id}'
    params = {
        'fields': 'name,genre,fan_count,location,events',
        'access_token': FACEBOOK_ACCESS_TOKEN
    }
    response = requests.get(url, params=params)
    return response.json()

data = get_page_info(page_id)
print("Artist Page Data: " + data)

@app.route('/api/user-insights', methods=['GET'])
def get_facebook_user_insights():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    url = f'https://graph.facebook.com/v20.0/{user_id}/insights?access_token={FACEBOOK_ACCESS_TOKEN}'
    response = requests.get(url)
    
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from Facebook'}), response.status_code

    data = response.json()
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    user_id = request.form['user_id']
    return redirect(url_for('get_facebook_user_insights', user_id=user_id))

if __name__ == '__main__':
    app.run(debug=True)
