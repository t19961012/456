# -*- coding: utf-8 -*-
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('ceNnESXwkKiUB5yfzIS0YaeA3BrsV9CYkNQFhT1LHt8vXbz5J10KBl/IJpw2Q7NgjjxsUGRfJluRlzGZOUMJnHmRXBlN4aLFgaDa7OzTCNSdSLfyBFC+8bwK+SCilB2qfkySsDHTrl+XM0Jmv+nAwwdB04t89/1O/w1cDnyilFU=')
# Channel access token (long-lived)
handler = WebhookHandler('d5843f95a89a5b52e0275baf5dffce1a')
# Channel secret 



@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)