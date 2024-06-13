import sqlite3
import sqlparse
import re
import os


db_name = 'database copy.db'


def create_records(content, debug=True):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        sql_commands = re.findall("```(.*?)```", content, re.DOTALL)

        for command in sql_commands:
            # Split the command into statements
            statements = sqlparse.split(command)
            
            for statement in statements:
                # Parse the statement
                parsed = sqlparse.parse(statement)
                
                # Check if it's an INSERT INTO statement
                if isinstance(parsed[0], sqlparse.sql.Statement) and 'INSERT OR IGNORE INTO' in str(parsed[0]):
                    if debug:
                        print(f'The following INSERT INTO statement is syntactically correct:\n{statement}\n')
                    else:
                        print(f'The following INSERT INTO statement is syntactically correct')
                    
                    # Execute the SQL command
                    c.execute(statement)
                else:
                    if debug:
                        print(f'The following statement is not a valid INSERT INTO statement:\n{statement}\n')

                    raise ValueError(f"Неправильный запрос: {statement}")


def count_records(name_of_table):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        
        # Execute the SQL command
        c.execute(f"SELECT COUNT(*) FROM {name_of_table}")
        
        # Fetch the result
        result = c.fetchone()
        
        return result[0]

def create_tables(content):
    
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()

        # Connect to SQLite database (or create it if it doesn't exist)


        # Open and read the file
        # with open('1.txt', 'r') as f:
        #     file_content = f.read()

        # Extract SQL commands
        sql_commands = re.findall("```(.*?)```", content, re.DOTALL)

        # Check each SQL command
        for command in sql_commands:
            # Split the command into statements
            statements = sqlparse.split(command)
            
            for statement in statements:
                # Parse the statement
                parsed = sqlparse.parse(statement)
                
                # Check if it's a CREATE TABLE statement
                if isinstance(parsed[0], sqlparse.sql.Statement) and 'CREATE TABLE' in str(parsed[0]):
                    print(f'The following CREATE TABLE statement is syntactically correct:\n{statement}\n')
                    
                    # Execute the SQL command
                    c.execute(statement)
                else:
                    # print(f'The following statement is not a valid CREATE TABLE statement:\n{statement}\n')
                    raise ValueError(f"Неправильный запрос: {statement}")


def find_max_primary_key(primary_key_name, table_name):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        
        # Execute the SQL command
        c.execute(f"SELECT MAX({primary_key_name[0]}) FROM {table_name}")
        
        # Fetch the result
        result = c.fetchone()
        
        return result[0]



def find_primary_key(table_name):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        
        # Execute the SQL command
        c.execute(f"PRAGMA table_info({table_name})")
        
        # Fetch all the results
        results = c.fetchall()
        
        # Find the column(s) where 'pk' is not zero
        primary_keys = [result[1] for result in results if result[5] != 0]
        
        return primary_keys


def delete_file(filename):
    # Check if file exists
    if os.path.exists(filename):
        # Delete the file
        os.remove(filename)
        print(f"The file {filename} has been deleted.")
    else:
        print("The file does not exist.")

# Use the function



def get_table_names(db_name):

    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        # Execute the query
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")

        # Fetch all the table names
        table_names = c.fetchall()

        # Close the connection
        
        # Return the table names
        return [name[0] for name in table_names]




def get_fields_names(table_name):
    # Execute the PRAGMA statement
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        c.execute(f"PRAGMA table_info({table_name})")

        # Fetch and print all the field names
        fields = c.fetchall()
        text_fields = ""
        for field in fields:
            
            text_fields += field[1] + ": " + field[2] + ", " # field[1] contains the name of the field
        text_fields = text_fields[:-2]
        return text_fields 


def get_names_of_tables():
    names_in_db = get_table_names(db_name)
    names = ""

    # z = 1
    for name in names_in_db:
        # z+=1
        if name == 'sqlite_sequence':
            continue

        names += str(name) + ", "

    return names