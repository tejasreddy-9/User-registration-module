from pymongo import MongoClient

MONGO_URI = "mongodb+srv://tejasreddyis9999:Teja12399@resume-scanner.gsgmxva.mongodb.net/user_registration?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)
    db = client["user_registration"]
    user_collection = db["users"]
    print("✅ MongoDB connection established successfully.")
except Exception as e:
    print(f"❌ Error connecting to MongoDB: {e}")
