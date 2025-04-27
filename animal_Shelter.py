# Author: Kain Mason
# Course: CS 340
# Milestone: Module Six
# Description: CRUD operations for Animal collection in MongoDB

from pymongo import MongoClient, errors
from bson.objectid import ObjectId

class AnimalShelter(object):
    """
    CRUD operations class for interacting with the Animal collection in MongoDB.
    Developed by Kain Mason for CS 340 Project One.
    """

    def __init__(self, username='aacuser', password='MySecurePassword123', 
                 host='nv-desktop-services.apporto.com', port=34505, 
                 db='AAC', collection='animals'):
        """Initialize MongoDB connection."""
        try:
            # Initialize MongoDB client connection
            self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
            # Connect to specified database and collection
            self.database = self.client[db]
            self.collection = self.database[collection]
            print("Connected successfully to MongoDB.")
        except errors.PyMongoError as e:
            # Handle errors during database connection
            print(f"Error connecting to MongoDB: {e}")

    def create(self, data):
        """Insert a document into the MongoDB collection."""
        if data:
            try:
                # Insert data into collection
                self.collection.insert_one(data)
                print("Document inserted successfully.")
                return True
            except errors.PyMongoError as e:
                # Handle insertion errors
                print(f"Error inserting data: {e}")
                return False
        else:
            print("No data provided to insert.")
            return False

    def read(self, query):
        """Query documents from the MongoDB collection."""
        if query is not None:
            try:
                # Find documents matching the query
                results = list(self.collection.find(query))
                print(f"Found {len(results)} document(s) matching query.")
                return results
            except errors.PyMongoError as e:
                # Handle query errors
                print(f"Error reading data: {e}")
                return []
        else:
            print("Query was None.")
            return []

    def update(self, query, update_data):
        """Update documents in the MongoDB collection."""
        if query and update_data:
            try:
                # Perform update operation
                result = self.collection.update_many(query, {"$set": update_data})
                print(f"{result.modified_count} document(s) updated.")
                return result.modified_count
            except errors.PyMongoError as e:
                # Handle update errors
                print(f"Error updating data: {e}")
                return 0
        else:
            print("No query or update data provided.")
            return 0

    def delete(self, query):
        """Delete documents from the MongoDB collection."""
        if query:
            try:
                # Perform delete operation
                result = self.collection.delete_many(query)
                print(f"{result.deleted_count} document(s) deleted.")
                return result.deleted_count
            except errors.PyMongoError as e:
                # Handle deletion errors
                print(f"Error deleting data: {e}")
                return 0
        else:
            print("No query provided to delete.")
            return 0
