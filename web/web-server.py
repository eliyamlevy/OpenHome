from bottle import run, get, post, request
import paho.mqtt.publish as publish
import json

#Splash page
@get('/')
def index():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>
                    <body style="background-color:rgb(84,134,191)">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: white">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/> <br>
                                    <input id="publish" type="submit" value="Publish">
                                </form>
                            </div>
                            <div class="links">
                                <a href="/say" style="font-family: Helvetica;color: white">Say terminal</a>
                                <a href="/config"style="font-family: Helvetica;color: white">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

@post('/')
def index():
    cmd = request.forms.get('terminalInput')
    print(cmd)
    publish.single("openhome/controller", cmd)
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: white">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/> <br>
                                    <input id="publish" type="submit" value="Publish">
                                </form>
                            </div>
                            <div class="links">
                                <a href="/say" style="font-family: Helvetica;color: white">Say terminal</a>
                                <a href="/config"style="font-family: Helvetica;color: white">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Say handle
@get('/say')
def say_form():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: white">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <input type="submit" />
                                </form>
                            </div>
                            <div class="links">
                                <a href="/" style="font-family: Helvetica;color: white">Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

@post('/say')
def say():
    say = request.forms.get('say')
    publish.single("hermes/tts/say", json.dumps({"text": say, "siteId": "default"}))
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: white">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <input type="submit" />
                                </form>
                            </div>
                            <div class="links">
                                <a href="/" style="font-family: Helvetica;color: white">Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Config Page
@get('/config')
def config():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white">OpenHome Setup Page</h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: white">Weather App Setup</h4>
                                <form method="POST" action="/config/weather/success">
                                    <input name="location" type="text" placeholder="Location"/> <br>
                                    <input type="submit" />
                                </form>
                                <h4 style="font-family: Helvetica;color: white">Hue Bridge Setup</h4>
                                <p style="font-family: Helvetica;color: white">Please input the ip address of your Hue bridge and press the center button on the bridge before pressing submit</p>
                                <form method="POST" action="/config/hue/success">
                                    <input name="IP Address" type="text" placeholder="Enter location"/> <br>
                                    <input type="submit" />
                                </form>
                            </div>
                            <div class="links">
                                <a href="/" style="font-family: Helvetica;color: white">Return Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: /Users/pecchio/Desktop/OpenHome Website/WeatherSuccess.htmlHelvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Weather config success
@post('/config/weather/success')
def weather_success():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                                border-radius: 50%;
                            }
                        </style>

                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white">OpenHome Setup Page</h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: white">Weather App Setup</h4>
                                <p style="font-family: Helvetica;color: white">Your Location has been saved, Thank You!</p>
                            <div class="links">
                                <a href="/config">Back</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Hue config success
@post('/config/hue/success')
def hue_success():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <style>
                            img {
                              border-radius: 50%;
                            }
                        </style>
                        <meta charset="utf-8">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:rgb(84,134,191);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: white">OpenHome Setup Page</h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: white">Hue App Setup</h4>
                                <p style="font-family: Helvetica;color: white">Your Hue Bridge has been connected, Thank You!</p>
                            <div class="links">
                                <a href="/config" style="font-family: Helvetica;color: white">Back</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://i.pinimg.com/originals/f9/f0/3f/f9f03f866e01bdf1220ab4a1f361723a.png" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: white">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: white">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

if __name__ == '__main__':
    run(host='0.0.0.0', port=7070)
