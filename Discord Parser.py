from flask import Flask, request, make_response, render_template, redirect
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    if request.method == "GET":
        return render_template('home.html')

@app.route("/result", methods=['POST'])
def submitJson():
    if request.method == "POST":

        valid = None
        data = request.form['json']
        try:
            chat = []
            data = json.loads(request.form['json'])
            for message in data:
                #print(f"{message['author']['username']} : {message['content']}\n")

                attachment = None
                if len(message['attachments']) > 0:
                    attachment = message['attachments'][0]['url']

                chat.append([message['author']['username'], message['content'], attachment])
                valid = True
        except Exception as e:
            print(e)

        print(valid)
        return render_template("result.html",
                                valid=valid,
                                chat=chat,
                                data=data)

if __name__ == "__main__":
    app.run(port=6800, debug=True)