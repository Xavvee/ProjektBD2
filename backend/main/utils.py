from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        self.client = MongoClient('mongodb://admin:admin@localhost:27017/')
        self.db = self.client['db_project']

    def insert_one(self, collection_name, data):
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return result.inserted_id

    def find_all(self, collection_name):
        collection = self.db[collection_name]
        return collection.find()

    def find_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def update_one(self, collection_name, query, new_data):
        collection = self.db[collection_name]
        return collection.update_one(query, {"$set": new_data})

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def add_table(self, game_id, capacity):
        game = self.db['Games'].find_one({'gameId': game_id})

        if game:
            tables = game.get('tables', [])
            table_id = len(tables) + 1  # Next number based on tables array size
            reserved_dates = []  # Empty list by default

            # Create new table data
            new_table = {'tableId': str(table_id), 'capacity': capacity, 'reservedDates': reserved_dates}
            tables.append(new_table)
            self.update_one('Games', {'gameId': game_id}, {'tables': tables})
        else:
            print(f"Game {game_id} not found.")
