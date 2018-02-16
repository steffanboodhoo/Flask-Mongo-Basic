from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost',27017)

db = client['fishdb']

collection = db.['fisherman']
