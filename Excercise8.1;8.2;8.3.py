#Write a program that asks the user to enter the ICAO code
# of an airport. The program fetches and prints out the corresponding
# airport name and location (town)
# from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.#

import mysql.connector

def find_airport(ICAO):
    sql=f"SELECT name,municipality from airport WHERE airport.ident='{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"The airport name and the municipality: \n {result}")
    return

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='konstantinkovalev',
         password='password',
         autocommit=True,
         collation = 'utf8mb4_general_ci',
         charset='utf8mb4'
         )

ICAO=input("Enter the ICAO code of an airport")
find_airport(ICAO)

#Write a program that asks the user to enter the area code
# (for example FI) and prints out the airports located in that country
# ordered by airport type. For example, Finland has 65 small airports,
# 15 helicopter airports and so on.

user_input=input("Enter airport's area code:")
def airport(airports):
    sql=f"select name from airport where airport.iso_country='{user_input}' order by type"
    cursor=connection.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    if cursor.rowcount > 0:
        for i in result:
            print(i)
    return
airport(user_input)

#Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

from geopy.distance import geodesic
ICAO_1=input("Please enter the ICAO code of the 1st airport")
sql=f"select latitude_deg,longitude_deg from airport where airport.ident='{ICAO_1}'"
cursor=connection.cursor()
cursor.execute(sql)
coordinates1=cursor.fetchall()
ICAO_2=input("Please enter the ICAO code of the 2nd airport")
sql=f"select latitude_deg,longitude_deg from airport where airport.ident='{ICAO_2}'"
cursor=connection.cursor()
cursor.execute(sql)
coordinates2=cursor.fetchall()
distance = geodesic(coordinates1, coordinates2).kilometers
if cursor.rowcount>0:
    print(f"the distance between these 2 airports is {distance:.2f}  km.")