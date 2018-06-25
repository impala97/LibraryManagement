from library import library as app
from flask import url_for, redirect, request
from ..model.chat import chat


@app.route('/index', methods=['POST'])
def rtchat():
    if request.method == 'POST':
        chat_data = dict()
        chat_data['name'] = str(app.config['user_name'])
        chat_data['message'] = str(request.form['message_txt'])
        if chat().addchat(**chat_data):
            return redirect(url_for('rtindex'))
        else:
            return "due to some error you have been logout."


