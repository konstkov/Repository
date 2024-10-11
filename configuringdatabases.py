import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='local_user',
         password='password',
         autocommit=True,
         collation='utf8mb4_unicode_ci'
         )

def get_airport_by_identity(identity):
    sql = f"select * from airport where ident='{identity}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='dbuser',
         password='pAs5w_0rD',
         autocommit=True
         )

last_name = input("Enter last name: ")
get_employees_by_last_name(last_name)