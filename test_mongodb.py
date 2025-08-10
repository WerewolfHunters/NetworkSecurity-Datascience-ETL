from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://awwabmahimi0074:<your_db_password>@cluster0.5wyko16.mongodb.net/"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You have been successfully connected to MongoDB")
except Exception as e:
    print(e)