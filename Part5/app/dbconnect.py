import mysql.connector

def connection():
    # Edited out actual values
    conn = mysql.connector.connect( host='dbhost',
                            port=3306,
                            database=db_name,
                            user=db_user,
                            password=db_pass)
    c = conn.cursor()

    return c, conn