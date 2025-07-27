from pymongo import MongoClient

MONGO_URI = "mongodb+srv://tejasreddyis9999:Teja12399@resume-scanner.gsgmxva.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client['user_db']
user_collection = db['users']
