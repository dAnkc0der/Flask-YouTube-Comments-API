from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

BASE_URL = "https://app.ylytic.com/ylytic/test"

@app.route('/search', methods=['GET'])
def search_comments():
    search_author = request.args.get('search_author')
    at_from = request.args.get('at_from')
    at_to = request.args.get('at_to')
    like_from = request.args.get('like_from')
    like_to = request.args.get('like_to')
    reply_from = request.args.get('reply_from')
    reply_to = request.args.get('reply_to')
    search_text = request.args.get('search_text')

    params = {}
    if search_author:
        params['search_author'] = search_author
    if at_from:
        params['at_from'] = at_from
    if at_to:
        params['at_to'] = at_to
    if like_from:
        params['like_from'] = like_from
    if like_to:
        params['like_to'] = like_to
    if reply_from:
        params['reply_from'] = reply_from
    if reply_to:
        params['reply_to'] = reply_to
    if search_text:
        params['search_text'] = search_text

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
