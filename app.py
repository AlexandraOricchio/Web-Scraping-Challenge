from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the collection and drop any existing data
mars_db = mongo.db.mars_db
mars_db.drop()

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    mars_results = mars_db.find_one()
    return render_template("index.html", mars_results=mars_results)

# # Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Insert the results into the database
    mars_db.insert_one(mars_data)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
