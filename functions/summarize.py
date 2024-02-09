# functions/summarize.py
from summarizer import get_summary

def handler(event, context):
    data = event['body-json']
    text = data['text']

    if not text:
        return {'statusCode': 400, 'body': 'Please enter some text to summarize.'}

    summary = get_summary(text, num_sentences=3)
    return {'statusCode': 200, 'body': {'summary': summary}}
