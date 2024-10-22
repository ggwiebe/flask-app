from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/data')
def get_api_data():
    # Make a GET request to the external API
    api_url = "https://api.example.com/data"
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the data as JSON
        return jsonify(data)
    else:
        # Handle errors
        return jsonify({"error": "Failed to fetch data from API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)