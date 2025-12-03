# main.py
import sqlite3
import os

def execute_sql_file(filename, connection):
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    cursor = connection.cursor()
    try:
        cursor.executescript(sql_script)
        connection.commit()
        print("SQL file executed successfully")
        return True
    except Exception as e:
        print(f"Error executing SQL file: {e}")
        return False

def main():
    db_file = 'school.db'
    if os.path.exists(db_file):
        os.remove(db_file)
    
    conn = sqlite3.connect(db_file)
    
    try:
        sql_file = 'school_queries.sql'
        if not os.path.exists(sql_file):
            print(f"File '{sql_file}' not found!")
            return
        
        execute_sql_file(sql_file, conn)
            
    finally:
        conn.close()
        print(f"Database created: {db_file}")

if __name__ == "__main__":
    main()