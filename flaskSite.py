from flask import Flask,request,url_for,redirect
from flask import render_template
from weather import *

#everything flask needs is in this directory
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        location = request.form["location"]
        return redirect(url_for("show_weather",location=location))
    else:
        return render_template("index.html")

@app.route("/<location>",methods=["POST","GET"])
def show_weather(location):
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        api_instance = create_api_instance()
        forecast = get_forecast(api_instance,location)
        return render_template("weather_forecast.html",high=forecast["high"], low=forecast["low"],wind_mph=forecast["wind_mph"],current_temp=forecast["current_temp"],
                            local_time=forecast["local_time"], text=forecast["text"],pic=forecast["picture"])

app.run(host="0.0.0.0",port=80)