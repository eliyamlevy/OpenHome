from bottle import run, get, post, request
import paho.mqtt.publish as publish
import json

#Splash page
@get('/')
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
                            <div class="header">
                                <h2> Welcome to OpenHome </h2>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/> <br>
                                    <input id="publish" type="submit" value="publish">
                                </form>'
                            </div>
                        </div>
                    </body>
                </html> '''

@post('/')
def login_form():
    cmd = request.forms.get('terminalInput')
    print(cmd)
    #publish.single("openhome/controller", cmd)
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
                            <div class="header">
                                <h2> Welcome to OpenHome </h2>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/> <br>
                                    <input id="publish" type="submit" value="publish">
                                </form>'
                            </div>
                        </div>
                    </body>
                </html> '''

#Say handle
@get('/say')
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
                            <div class="header">
                                <h2> Welcome to OpenHome </h2>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <input type="submit" />
                                </form>'
                            </div>
                        </div>
                    </body>
                </html> '''

@post('/say') # or @route('/login', method='POST')
def login_submit():
    say = request.forms.get('say')
    publish.single("hermes/tts/say", json.dumps({"text": say, "siteId": "default"}))

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
                            <div class="header">
                                <h2> Welcome to OpenHome </h2>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <input type="submit" />
                                </form>'
                            </div>
                        </div>
                    </body>
                </html> '''

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080)
