from flask import Flask, render_template, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from werkzeug.urls import quote
import os
import logging

app = Flask(__name__, static_folder='templates')

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
  logging.debug("Rendering index.html")
  return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']

    if not text:
        return jsonify({'summary': 'Please enter some text to summarize.'})

    summary = get_summary(text, num_sentences=3)  # Summarize within 50 words (approx. 3 sentences)
    return jsonify({'summary': summary})

def get_summary(text, num_sentences):
    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join(str(sentence) for sentence in summary)

# Manually specify the port number
port = int(os.environ.get('PORT', 3000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
