import missiontomars
from flask_pymongo import PyMongo
from flask import Flask, jsonify, render_template

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsapp"
mongo = PyMongo(app)

#collection = db.marsdb.marscollection

@app.route("/")
def home():
   # Find data
    marsdata = mongo.db.collection.find()
    # return template and data
    return render_template("index.html", marsdata=marsdata)


@app.route("/scrape")
def scrape():
    
    marsdata = missiontomars.scrape()
    mongo.db.collection.insert_one(marsdata)

  #  collection.insert_one(scraped_data)
  #  data = collection.find_one({})
  #   print(data)
    return render_template('index.html',marsdata=marsdata)

if __name__ == "__main__":
    app.run(debug=True)