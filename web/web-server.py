from bottle import run, get, post, request
import paho.mqtt.publish as publish
import json

#Splash page
@get('/')
def index():
    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
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
                                </form>
                            </div>
                            <div class="links">
                                <a href="/say">Say terminal</a>
                                <a href="/config">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                </html> '''

@post('/')
def index():
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
                                </form>
                            </div>
                            <div class="links">
                                <a href="/say">Say terminal</a>
                                <a href="/config">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                </html> '''

#Say handle
@get('/say')
def say_form():
    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
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
                                </form>
                            </div>
                            <div class="links">
                                <a href="/">Home</a>
                            </div>
                        </div>
                    </body>
                </html> '''

@post('/say')
def say():
    say = request.forms.get('say')
    publish.single("hermes/tts/say", json.dumps({"text": say, "siteId": "default"}))

    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
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
                                </form>
                            </div>
                            <div class="links">
                                <a href="/">Home</a>
                            </div>
                        </div>
                    </body>
                </html> '''

#Config Page
@get('/config')
def config():
    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body>
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2> OpenHome Setup Page </h2>
                            </div>
                            <div class="forms">
                                <h4>Weather App Setup</h4>
                                <form method="POST" action="/config/weather/success">
                                    <input name="location" type="text" placeholder="Location"/> <br>
                                    <input type="submit" />
                                </form>
                                <h4>Hue Bridge Setup</h4>
                                <p>Please input the ip address of your Hue bridge and press the center button on the bridge before pressing submit</p>
                                <form method="POST" action="/config/hue/success">
                                    <input name="IP Address" type="text" placeholder="Location"/> <br>
                                    <input type="submit" />
                                </form>
                            </div>
                            <div class="links">
                                <a href="/">Return Home</a>
                            </div>
                        </div>
                    </body>
                </html> '''

#Weather config success
@post('/config/weather/success')
def weather_success():
    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body>
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2> OpenHome Setup Page </h2>
                            </div>
                            <div class="forms">
                                <h4>Weather App Setup</h4>
                                <p>Your Location has been saved, Thank You!</p>
                            <div class="links">
                                <a href="/">Return Home</a>
                            </div>
                        </div>
                    </body>
                </html> '''

#Hue config success
@post('/config/hue/success')
def hue_success():
    return '''  <!doctype html>

                <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body>
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2> OpenHome Setup Page </h2>
                            </div>
                            <div class="forms">
                                <h4>Hue App Setup</h4>
                                <p>Your Hue Bridge has been connected, Thank You!</p>
                            <div class="links">
                                <a href="/">Return Home</a>
                            </div>
                        </div>
                    </body>
                </html> '''

if __name__ == '__main__':
    run(host='0.0.0.0', port=7070)
