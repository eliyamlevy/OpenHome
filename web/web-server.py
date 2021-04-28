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
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%;
                            }
                            h2 {
                                font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>
                    <body style="background-color:white">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000">
                                    Welcome to OpenHome
                                </h2>
                                <h3 style="font-family: Helvetica;color: black">
                                    Secure AI Voice Assistant
                                </h3>
                                <br>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" type="text" name="terminalInput" placeholder="Input commands here ..."/> <br>
                                    <input id="publish" type="submit" value="Publish">
                                </form>
                            </div>
                            <div class="links">
                                <a href="/say" style="font-family: Helvetica;color: navy">Say terminal</a>
                                <a href="/config"style="font-family: Helvetica;color: navy">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://image.freepik.com/free-vector/smart-speaker-abstract-concept-illustration_335657-3826.jpg" height="500" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold;"">
                        About OpenHome
                    </h3>
                    <h4 style="font-family: Helvetica;color: black">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </h4>
                    </center>
                </html> 
'''

# Splash Page 2
@post('/')
def index():
    cmd = request.forms.get('terminalInput')
    print(cmd)
    publish.single("openhome/controller", cmd)
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%
                            }
                            h2 {
                                font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color: white;">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000">
                                    Welcome to OpenHome 
                                </h2>
                                <h3 style="font-family: Helvetica;color: black">
                                    Secure AI Voice Assistant
                                </h3>
                                <br>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/">
                                    <input id="terminalInput" name="terminalInput" class="form-control form-control-lg" type="text" placeholder="Input commands here...">
                                    <br>
                                    <button id="publish" type="submit" class="btn btn-primary btn-lg">Publish</button>
                                </form>
                            </div>
                            <div class="links">
                                <br>
                                <a href="/say" style="font-family: Helvetica;color: navy">Say terminal</a>
                                <br>
                                <a href="/config"style="font-family: Helvetica; color: navy">OpenHome Setup</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://image.freepik.com/free-vector/smart-speaker-abstract-concept-illustration_335657-3826.jpg" height="500" alt="OpenHome Visual">
                    <br><br>
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold;">
                        About OpenHome
                    </h3>
                    <br>
                    <h4 style="font-family: Helvetica;color: black">
                        OpenHome is a open-source developer friendly alternative to corporate owned smart speakers.<br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.
                    </h4>
                    </center>
                </html>'''

#Say handle
@get('/say')
def say_form():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%;
                            }
                            h2 {
                                font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:white;">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: black">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <br>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <br>
                                    <input id="publish" type="submit" class="btn btn-primary btn-lg"/>
                                </form>
                            </div>
                            <br>
                            <div class="links">
                                <a href="/" style="font-family: Helvetica;color: navy">Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://image.freepik.com/free-vector/smart-speaker-abstract-concept-illustration_335657-3826.jpg" height="500" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: black">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html>'''

# Say Handle 2
@post('/say')
def say():
    say = request.forms.get('say')
    cmd = "resp&webserver&speak&" + say
    publish.single("openhome/controller", cmd)
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%;
                            }
                            h2 {
                                font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:white;">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000"> Welcome to OpenHome </h2>
                                <h3 style="font-family: Helvetica;color: black">
                                    Secure AI Voice Assistant
                                </h3>
                            </div>
                            <div class="forms">
                                <form method="POST" action="/say">
                                    <input name="say" type="text" /> <br>
                                    <br>
                                    <input id="publish" type="submit" class="btn btn-primary btn-lg"/>
                                </form>
                            </div>
                            <div class="links">
                                <a href="/" style="font-family: Helvetica;color: navy">Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://image.freepik.com/free-vector/smart-speaker-abstract-concept-illustration_335657-3826.jpg" height="500" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: black">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html>'''

#Config Page
@get('/config')
def config():
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%;
                            }
                            h2 {
                              font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color: white;">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000">
                                    OpenHome Setup Page
                                </h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: black">Weather App Setup</h4>
                                <form method="POST" action="/config/weather/success">
                                    <input name="location" type="text" placeholder="Location"/> <br>
                                    <br>
                                    <input id="submit" type="submit" class="btn btn-primary btn-lg"/>
                                    <br>
                                </form>
                                <br>
                                <h4 style="font-family: Helvetica;color: navy">Hue Bridge Setup</h4>
                                <p style="font-family: Helvetica;color: navy">Please input the ip address of your Hue bridge and press the center button on the bridge before pressing submit</p>
                                <form method="POST" action="/config/hue/success">
                                    <input name="IP Address" type="text" placeholder="Enter location"/> <br>
                                    <br>
                                    <input id="submit" type="submit" class="btn btn-primary btn-lg"/>
                                </form>
                            </div>
                            <div class="links">
                                <br><br>
                                <a href="/" style="font-family: Helvetica;color: navy">Return Home</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://image.freepik.com/free-vector/smart-speaker-abstract-concept-illustration_335657-3826.jpg" height="500" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold;">
                        About OpenHome
                    </h3>
                    <h4 style="font-family: Helvetica;color: black">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Weather config success
@post('/config/weather/success')
def weather_success():
    location = request.forms.get('location')
    cmd = "resp&webserver&config&weather&" + location
    publish.single("openhome/controller", cmd)
    return '''  <!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                                border-radius: 50%;
                            }
                            h2 {
                                font-size: xx-large;
                            }
                        </style>

                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color:white">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000">OpenHome Setup Page</h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: black">Weather App Setup</h4>
                                <p style="font-family: Helvetica;color: balck">Your Location has been set. Thank You!</p>
                            <div class="links">
                                <a href="/config">Back</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://cdn.dribbble.com/users/372537/screenshots/2065624/icons_km_weather.gif" height="200" alt="OpenHome Visual">
                    <h3 style="font-family: Helvetica;color: black; font-weight: bold">
                        About OpenHome
                    </h3>
                    <p style="font-family: Helvetica;color: black">
                        Open-source developer friendly alternative to corporate owned smart speakers.<br></br>
                        It’s easy to expand with widgets and plugins and helps keep your data secure.<br></br>
                    </p>
                    </center>
                </html> '''

#Hue config success
@post('/config/hue/success')
def hue_success():
    ip = request.forms.get('ip_address')
    cmd = "resp&webserver&config&light&" + ip
    publish.single("openhome/controller", cmd)
    return '''<!DOCTYPE html>
                <html lang="en">
                    <center>
                    <head>
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                        <style>
                            img {
                              border-radius: 50%;
                            }
                            h2 {
                              font-size: xx-large;
                            }
                        </style>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>OpenHome</title>
                        <meta name="description" content="The web interface for your OpenHome!">
                        <meta name="author" content="OpenHome">
                    </head>

                    <body style="background-color: white);">
                        <script src="index.js"></script>
                        <div class="body">
                            <div class="header">
                                <br>
                                <h2 style="font-family: Helvetica;color: black; font-weight: bold; font-size: 1000">
                                    OpenHome Setup Page
                                </h2>
                            </div>
                            <div class="forms">
                                <h4 style="font-family: Helvetica;color: black">Hue App Setup</h4>
                                <p style="font-family: Helvetica;color: black">Your Hue Bridge has been connected. Thank You!</p>
                            <div class="links">
                                <a href="/config" style="font-family: Helvetica;color: navy">Back</a>
                            </div>
                        </div>
                    </body>
                    <br></br>
                    <img src="https://media4.giphy.com/media/pylpD8AoQCf3CQ1oO2/200w.gif?cid=82a1493bgros9ctztz9z4z63arib3oxn7ogvofrlebwqoa9j&rid=200w.gif" height="200" alt="OpenHome Visual">
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
'+
