from pymongo import MongoClient

cluster = MongoClient(f"<mongoclient link here>")

db = cluster["<database name here>"]
collection = db["<collection name here>"]

username = input("Enter username: ")
password = input("Enter password: ")

collection.insert_one({"username":username, "password":password})

username = input("Enter username: ")
password = input("Enter password: ")

check = collection.find_one({"username":username, "password":password})

if check:
    print("User detected")
else:
    print("User not detected")
