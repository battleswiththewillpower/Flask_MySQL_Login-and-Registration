from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

# Naming convenction to use for mutiple projects. just change the string name to the proper scema
DATABASE = 'login_reg_db'

# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name= data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create_user(cls, data:dict):
        #query the string
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        #contact the database
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    #want to be able to update whichever user we select by id thro the DB since each id is unique to the user
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # #edit the user and update the information
    # @classmethod
    # def update(cls, data):
    #     # query = "UPDATE users SET name=%(name)s, email=%(email)s, description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
    #     # make sure theres no spaces inbetwwen each comma
    #     query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,password=%(password)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # checking to make sure there arent any errors
        if results:
        # Create an empty list to append our instances of friends
            users = []
            # Iterate over the db results and create instances of friends with cls.
            for user in results:
                users.append( cls(user) )
            return users
        return False

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters!")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("I told you at least 2 characters!")
# Email - valid Email format, does not already exist in the database, and that it was submitted
        if 'email' not in user:
            is_valid = False
            flash("try again")
# Password - at least 8 characters, and that it was submitted
# Password Confirmation - matches password
        # if len(user['password']) < 3:
        #     is_valid = False
        #     flash("You really don't listen HUH?")
            
        return is_valid