from bottle import run, get, post, request
import paho.mqtt.publish as publish
import json

#Test page
@get('') # or @route('/login')
def login_form():
    return '''  <!doctype html>

                <html lang="en">
                <head>
                <meta charset="utf-8">

                <title>OpenHome</title>
                <meta name="description" content="The web interface for your OpenHome!">
                <meta name="author" content="OpenHome">

                <link rel="stylesheet" href="css/styles.css?v=1.0">

                </head>

                <body>
                <script src="index.js"></script>
                <div class="body">
                    Welcome to OpenHome <br />
                    <div class="forms">
                        <form name="terminal">
                            <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/>
                            <input id="publish" type="submit" value="publish" onclick="return publishCMD()">
                        </form>
                    </div>
                </div>
                </body>
                </html> '''

#Say handle
@get('/say')
def login_form():
    return '''<form method="POST" action="/say">
                <input name="say"     type="text" />
                <input type="submit" />
              </form>'''

@post('/say') # or @route('/login', method='POST')
def login_submit():
    say = request.forms.get('say')
    publish.single("hermes/tts/say", json.dumps({"text": text, "siteId": "default"}))
    return '''<form method="POST" action="/say">
                <input name="say"     type="text" />
                <input type="submit" />
              </form>'''

if __name__ == '__main__':
    run(host='localhost', port=8080)