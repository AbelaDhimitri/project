from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name="recipes"
    def __init__(self, db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.network = db_data['network']
        self.release_date = db_data['release_date']
        self.action = db_data['action']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (title,network, release_date, action, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(action)s, %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results =  connectToMySQL(cls.db_name).query_db(query, data)
        return results[0] 

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(title)s, description =  %(network)s, instructions=%(release_date)s, under30=%(action)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query= "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_recipes= []
        for row in results:
            all_recipes.append(row)
        return all_recipes
    
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['title'])<3:
            flash('Title must be at least 3 characters', "recipe")
            is_valid=False
        if len(recipe['network'])<3:
            flash('Network must be at least 3 characters', "recipe")
            is_valid=False
        if len(recipe['description'])<3:
            flash('Description must be at least 3 characters', "recipe")
            is_valid=False
        if recipe['date_made'] == "":
            flash('Please enter a date', "recipe")
            is_valid=False
        return is_valid
    
    