from flask import Flask, render_template, request
import requests
import json
import time

app = Flask(__name__)

Geoapify_Key = ""
spoonacular_api_key = ""

def get_coords_from_zip(zip):
	geocodeapi_url = "https://api.geoapify.com/v1/geocode/search?text=" + str(zip) + "&type=postcode&filter=countrycode:us,ca&format=json&apiKey=" + Geoapify_Key
	response = json.loads(requests.request("GET", geocodeapi_url).text)
	latraw = response["results"][0]["lat"]
	lat = format(latraw, ".4f")
	lonraw = response["results"][0]["lon"]
	lon = format(lonraw, ".4f")
	city = response["results"][0]["city"]
	return lat,lon,city

def get_gridpoint_forecast(lat,lon):
	points_url = "https://api.weather.gov/points/" + str(lat) + "," + str(lon)
	gridpoint_response = json.loads(requests.request("GET", points_url).text)
	forecast_url = gridpoint_response["properties"]["forecast"]
	forecast_response = json.loads(requests.request("GET", forecast_url).text)
	shortForecast = forecast_response["properties"]["periods"][0]["shortForecast"]
	return shortForecast

def vibecheck (forecast):
	if "Clear" in forecast:
		vibe = "noodles"
	elif "Cloudy" in forecast:
		vibe = "meatballs"
	elif "Rain" in forecast:
		vibe = "soup"
	else:
		vibe = "sandwich"

def get_recipe (vibe):
	spoonacular_url = "https://api.spoonacular.com/recipes/complexSearch?query="+str(vibe)+"&number=1&limitLicense=true&apiKey="+str(spoonacular_api_key)
	random_recipe_url = "https://api.spoonacular.com/recipes/random?number=1&apiKey="+str(spoonacular_api_key)
	response = json.loads(requests.request("GET", spoonacular_url).text)
	if response["totalResults"] < 1:
		response = json.loads(requests.request("GET", random_recipe_url).text)
		title = response["recipes"][0]["title"]
		image = response["recipes"][0]["image"]
		id = response["recipes"][0]["id"]
		sourceUrl = response["recipes"][0]["spoonacularSourceUrl"]
	else:
		title = response["results"][0]["title"]
		image = response["results"][0]["image"]
		id = response["results"][0]["id"]
		recipe_url = "https://api.spoonacular.com/recipes/"+str(id)+"/information"
		response = json.loads(requests.request("GET", recipe_url).text)
		sourceUrl = response["spoonacularSourceUrl"]

	return title,image,id,sourceUrl

@app.route("/", methods =["GET", "POST"])
def index():
	if request.method == "POST":
		zipcode = request.form.get("zipcode")
		lat,lon,city = get_coords_from_zip(zipcode)
		forecast = get_gridpoint_forecast(lat,lon)
		vibe = vibecheck(forecast)
		title,image,id,sourceUrl = get_recipe(vibe)
		return render_template("wireframe.html",lat=lat,lon=lon,forecast=forecast,title=title,image=image,id=id,sourceUrl=sourceUrl,city=city)
	return render_template("form.html")


app.run(host="0.0.0.0", port=5000)
