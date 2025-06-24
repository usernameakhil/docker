from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

entries = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entries', methods=['GET', 'POST'])
def journal_entries():
    if request.method == 'POST':
        data = request.get_json()
        entry = {
            "date": data.get("date"),
            "content": data.get("content")
        }
        entries.append(entry)
        return jsonify({"message": "Entry saved!"}), 201
    return jsonify(entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
