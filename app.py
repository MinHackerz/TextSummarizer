# app.py
from flask import Flask, render_template, request, jsonify
from summarizer import get_summary  # Import get_summary function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']

    if not text:
        return jsonify({'summary': 'Please enter some text to summarize.'})

    summary = get_summary(text, num_sentences=3)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=False)
