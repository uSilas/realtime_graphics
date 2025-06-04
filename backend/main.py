from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

DATA_FILE = 'data.csv'

if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=['points', 'time_without_dying'])
    df.to_csv(DATA_FILE, index=False)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    points = data.get('points')
    time_without_dying = data.get('time_without_dying')

    if points is None or time_without_dying is None:
        return jsonify({'error': 'Missing data'}), 400

    new_data = pd.DataFrame([[points, time_without_dying]], columns=['points', 'time_without_dying'])
    new_data.to_csv(DATA_FILE, mode='a', header=False, index=False)

    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
